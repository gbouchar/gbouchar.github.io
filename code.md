---
layout: base
title:  Code
cmeta:  "Links to repositories and homepages of some open-source software
        projects/tools that I haves been involved with."
---

I like playing around with ideas and code, I don't refer to myself as a
hacker, but I like to hack. Making myself smile, other people smile and maybe
even alleviating the troubles of others. Hacking is, to do something I do
rarely, to quote Richard Stallman: ["Playfully doing something difficult,
whether useful or not, that is hacking"][stallman_hacking].

You can find random code snippets/forks and more at [my GitHub
page][github_ninjin]. Below are some projects that I am involved in or am
running myself.

## Projects ##

* [**SimSem**][simsem] is a research project aiming to semantically
    disambiguate textual spans. In less format terms, given a string like
    "British Shorthair", the system should produce output "Cat", since the
    text most likely refers to a feline family. It does so using large-scale
    lexical resources, unlike most related work the project also attempts to
    cover vast amounts of categories as opposed to a single category such as
    "Protein" or "Person". Please see [my publications][publications] for more
    details.

* [**stav**][stav] (stav text annotation visualiser) is a tool to visualise
    textual annotations and relations between such annotations. It was created
    for the BioNLP 2011 Shared Task but has been used to visualise other kinds
    of annotations such as semantic frames and dependency structures.

* [**brat**][brat] (brat rapid annotation tool) web-based annotation tool
    based on the visualisation capabilities of stav. Used in-house at Tsujii
    Laboratory and also by several external groups.

[brat]: http://brat.nlplab.org
[publications]: /publications.html
[github_ninjin]: https://github.com/ninjin
[simsem]: https://github.com/ninjin/simsem
[stallman_hacking]: http://stallman.org/articles/on-hacking.html
[stav]: https://github.com/TsujiiLaboratory/stav
