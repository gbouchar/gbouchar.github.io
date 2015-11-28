#!/usr/bin/env python
# vim:set ft=python ts=4 sw=4 sts=4 autoindent:

'''
Convert BibTeX-files to Jekyll posts for my personal homepage.

Author:     Pontus Stenetorp    <pontus stenetorp se>
Author:     Guillaume Bouchard <guillaume.m.bouchard gmail.com>
Version:    2015-11-27
'''

from argparse import ArgumentParser
from argparse import FileType
from datetime import date
from datetime import datetime
from os.path import join as path_join
from sys import stderr
from sys import stdin
from sys import stdout

from pybtex.database.input.bibtex import Parser as BibTeXParser
from pybtex.database import BibliographyData, Entry


### Constants
SELECTED = set((
    '2015arXiv150606100B',
    'bouchard2015approximate',
    'DBLP:journals/corr/BouchardTPG15',
    ))
# Not even nearly exhaustive, a hack.
TEX_UNESCAPES = (
        # Note: Font support is terrible for these two.
        ("\\'{c}", 'c', ),
        ('\\u{g}', 'g', ),

        ("\\'{e}", 'e', ),
        ('\\textsc{', '', ),
        ('{', '', ),
        ('}', '', ),
        )
###

def _argparser():
    argparser = ArgumentParser()

    argparser.add_argument('-posts_dir', '-posts_dir', default='_posts', help='directory for generated posts')
    argparser.add_argument('-bib', '-bib', 
            default='res/bib/bouchard.bib', type=FileType('r'),
            help='BibTeX-file to convert')

    argparser.add_argument('-i', '--input', type=FileType('r'),
            default=stdin, help='input source (default: stdin)')
    argparser.add_argument('-o', '--output', type=FileType('w'),
            default=stdout, help='output target (default: stdout)')

    return argparser

def _tex_unescape(s):
    for _from, to in TEX_UNESCAPES:
        s = s.replace(_from, to)
    return s

def _authors(s):
    for author in s.split(' and '):
        last, first = author.split(', ')
        yield '{} {}'.format(first, last)

def main(args):
    argp = _argparser().parse_args(args[1:])
    bib = argp.bib
    
    soup = BibTeXParser().parse_stream(bib)

    if len(soup.entries) < 1:
        print('WARNING: "{}" contains no entries, skipping.'.format(
            bib.name))
        exit(1)
    
    entries = soup.entries

    counts = 0
    for entry in entries:
        try:
            bib_name = 'bib/' + entry + '.bib'
            with open(bib_name, "w") as text_file:
                s = BibliographyData({entry:entries[entry]}).to_string('bibtex')
                text_file.write("{}".format(s))
        except:
            bib_name = None 

        counts += 1
        # Note: This library is really object oriented from hell.
        fields = entries[entry].fields

        try:
            year = datetime.strptime(fields['year'], '%Y').year
        except:
            print(counts)
            print("Entry " + entry + " has no year")           
            exit(1)

        try:
            month = datetime.strptime(fields['month'], '%B').month
            day = datetime.strptime(fields['day'], '%d').day
        except:
            month = 1
            day = 1
        presented = date(year=year, month=month, day=day)

        post_fname = '{}-{}.md'.format(
                presented.strftime('%Y-%m-%d'), entry.replace('/','-'))

        try:

            out = [
                '---',
                '# Note: Generated file, do not edit directly.',
                'type: publication',
                'bib: {}'.format(repr(bib_name)),
                'title: {}'.format(repr(_tex_unescape(fields['title']))),
                'authors: [{}]'.format(
                    ','.join(repr(a) for a in _authors(
                        _tex_unescape(fields['author'])))),
                ]
        except:
            print(counts)
            print("Entry " + entry + " has an error with the name, the title or the author field")           
            exit(1)


        try:
            out.append('venue_type: {}'.format(
                    repr(fields['venue_type'].lower())))
        except KeyError:
            out.append('venue_type: international')

        try:
            out.append('venue: {}'.format(
                repr(_tex_unescape(fields['booktitle']))))
        except KeyError:
            pass

        try:
            out.append('location: {}'.format(
                repr(_tex_unescape(fields['address']))))
        except KeyError:
            pass

        try:
            out.append('school: {}'.format(repr(fields['school'])))
        except KeyError:
            pass

        try:
            out.append('pdf: {}'.format(repr(fields['pdf_url'])).replace(
                # Make the URL reference local.
                'http://https://gbouchar.github.io', ''))
        except KeyError:
            pass

        try:
            out.append('slides: "{}"'.format(fields['slides_url']).replace(
                # Make the URL reference local.
                'http://https://gbouchar.github.io', ''))
        except KeyError:
            pass

        try:
            out.append('poster: "{}"'.format(fields['poster_url']).replace(
                'http://https://gbouchar.github.io', ''))
        except KeyError:
            pass

        try:
            out.append('pages: "{}"'.format(
                fields['pages'].replace('--', '-')))
        except KeyError:
            pass

        try:
            out.append('publisher: "{}"'.format(fields['publisher']))
        except KeyError:
            pass

        if entry in SELECTED:
            out.append('selected: true')

        try:
            if fields['note'].lower() == 'to appear':
                out.append('to_appear: true')
        except KeyError:
            pass

        out.append('---\n')
        
        fn = path_join(argp.posts_dir, post_fname)
        with open(fn, 'w') as post:
            post.write('\n'.join(out))
        print('file ' + fn + ' generated') 

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
