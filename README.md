# My PhD thesis: Characterizing quantum-dot cellular automata

## Overview

This repository contains everything related to my PhD thesis:

* Latex source files (directory `tex`)
* Graphics (directory `gfx`)
* Graphs (directory `plots`)
* Numerical data to produce the graphs (directory `experiments`)
* IPython notebooks which generate the graphs from the data (directory `notebooks`)
* Corrections from my committee (directory `corrections`)
* Different versions of the thesis for printing and viewing (files `*.pdf`)
* Makefile

## Variants

The following variants of the thesis exist:

* onesided: One-sided.
* twosided: Two-sided.
* print: Suitable for printing, no coloured links.
* fgsr: Complies with the University of Alberta's FGSR guidelines. One-sided,
  no coloured links, and an ugly title page (as required by the FGSR).

For reading on a screen, `phd_thesis_onesided.pdf` is the preferred variant; for
printing the preferred variant is `phd_thesis_twosided_print.pdf`. The final
version as submitted to the University of Alberta's FGSR is
`Ritter_Burkhard_201407_PhD.pdf`, equivalent to `phd_thesis_fgsr.pdf` but
converted to PDF/A format (using a trial version of Adobe Acrobat).

## Reproducing data and graphs

It should be possible to reproduce all data and graphs. The "numerical"
experiments in `experiments` contain not only the data, but also Python run
scripts to produce the data. My Python packages [coma][] and [qca][] are
required to run the simulations. Both are available under an open license. All
analysis and graphs are in the IPython notebooks in `notebooks`. Again, the
Python packages coma and qca are required to run those notebooks.

[coma]: https://github.com/meznom/coma
[qca]: https://github.com/meznom/qca

## Latex

The Makefile will build all the different versions of the thesis. E.g.
```
make
```

There is also a make target "nicenames" to get more verbosely named pdf files.
```
make nicenames
```

Most of the used Latex packages are pretty standard, with the possible exception
of "glossaries", which, on Ubuntu, is in the package "texlive-latex-extra".

The main latex file is "tex/phd_thesis.tex". Different variants are built from
"tex/phd_thesis_[variant].tex" and simply set some flags and then include the
main "phd_thesis.tex" file. 

---
Burkhard Ritter <burkhard@ualberta.ca>  
September 2014
