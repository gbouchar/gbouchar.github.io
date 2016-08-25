# gbouchar.github.io #

Jekyll/Git-based Homepage,
abusing the Jekyll "blog awareness" for data storage and served at
[https://gbouchar.github.io](https://gbouchar.github.io).

When the res/bib/bouchard.bib is updated, the script bib2post.py should be launched on a server where python is installed.

First, edit res/bib/bouchard.bib, and then run:

```
./bib2post.py
git add res/bib/bouchard.bib bib/* _posts/*
git commit -m "bib changes"
git push
```


