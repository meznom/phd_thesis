all:
	#cd plots; ./makeplots.sh; cd ..
	cd tex; \
	pdflatex phd_thesis.tex; \
	bibtex phd_thesis; \
	makeglossaries phd_thesis; \
	pdflatex phd_thesis.tex; \
	pdflatex phd_thesis.tex; \
	cd ..; \
	mv tex/phd_thesis.pdf .

clean:
	cd tex; \
	rm -f \
		*.aux \
		phd_thesis.bbl \
		phd_thesis.blg \
		phd_thesis.log \
		phd_thesis.toc \
		phd_thesis.out; \
	cd ..
	#cd plots; rm -f *.eps *.pdf *.tex; cd ..

