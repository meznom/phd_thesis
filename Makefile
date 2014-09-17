version = $(shell git describe --always)

all: onesided twosided onesided_print twosided_print fgsr

nicenames: all
	cp phd_thesis_onesided.pdf PhD_Thesis_Burkhard_Ritter_onesided.$(version).pdf
	cp phd_thesis_twosided.pdf PhD_Thesis_Burkhard_Ritter_twosided.$(version).pdf
	cp phd_thesis_onesided_print.pdf PhD_Thesis_Burkhard_Ritter_onesided_print.$(version).pdf
	cp phd_thesis_twosided_print.pdf PhD_Thesis_Burkhard_Ritter_twosided_print.$(version).pdf
	cp phd_thesis_fgsr.pdf PhD_Thesis_Burkhard_Ritter_FGSR.$(version).pdf
	cp Ritter_Burkhard_201407_PhD.pdf PhD_Thesis_Burkhard_Ritter_FGSR_PDFA_as_submitted.$(version).pdf

onesided:
	cd tex; \
	pdflatex phd_thesis_onesided.tex; \
	bibtex phd_thesis_onesided; \
	makeglossaries phd_thesis_onesided; \
	pdflatex phd_thesis_onesided.tex; \
	pdflatex phd_thesis_onesided.tex; \
	cd ..; \
	mv tex/phd_thesis_onesided.pdf .

twosided:
	cd tex; \
	pdflatex phd_thesis_twosided.tex; \
	bibtex phd_thesis_twosided; \
	makeglossaries phd_thesis_twosided; \
	pdflatex phd_thesis_twosided.tex; \
	pdflatex phd_thesis_twosided.tex; \
	cd ..; \
	mv tex/phd_thesis_twosided.pdf .

onesided_print:
	cd tex; \
	pdflatex phd_thesis_onesided_print.tex; \
	bibtex phd_thesis_onesided_print; \
	makeglossaries phd_thesis_onesided_print; \
	pdflatex phd_thesis_onesided_print.tex; \
	pdflatex phd_thesis_onesided_print.tex; \
	cd ..; \
	mv tex/phd_thesis_onesided_print.pdf .

twosided_print:
	cd tex; \
	pdflatex phd_thesis_twosided_print.tex; \
	bibtex phd_thesis_twosided_print; \
	makeglossaries phd_thesis_twosided_print; \
	pdflatex phd_thesis_twosided_print.tex; \
	pdflatex phd_thesis_twosided_print.tex; \
	cd ..; \
	mv tex/phd_thesis_twosided_print.pdf .

fgsr:
	cd tex; \
	pdflatex phd_thesis_fgsr.tex; \
	bibtex phd_thesis_fgsr; \
	makeglossaries phd_thesis_fgsr; \
	pdflatex phd_thesis_fgsr.tex; \
	pdflatex phd_thesis_fgsr.tex; \
	cd ..; \
	mv tex/phd_thesis_fgsr.pdf .

clean:
	cd tex; \
	rm -f \
		*.aux \
		phd_thesis*.acn \
		phd_thesis*.acr \
		phd_thesis*.alg \
		phd_thesis*.glg \
		phd_thesis*.glo \
		phd_thesis*.gls \
		phd_thesis*.ist \
		phd_thesis*.lof \
		phd_thesis*.lot \
		phd_thesis*.nlg \
		phd_thesis*.not \
		phd_thesis*.ntn \
		phd_thesis*.bbl \
		phd_thesis*.blg \
		phd_thesis*.log \
		phd_thesis*.toc \
		phd_thesis*.out \
		phd_thesis*.glsdefs; \
	cd ..
