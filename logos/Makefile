all : logo

logo : ncbs.pdf

ncbs.svg : ncbs.dvi
	dvisvgm $<

ncbs.pdf : ncbs.tex
	pdflatex $<

ncbs.dvi : ncbs.tex analyze
	latex --shell-escape $<

analyze: ./analyze.py
	python $<

