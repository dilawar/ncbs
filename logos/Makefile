all : ./ncbs_logo_byhand.pdf

%.pdf : %.tex
	pdflatex $<

logo : ncbs.pdf

ncbs.svg : ncbs.dvi
	dvisvgm $<

ncbs.pdf : ncbs.tex ./path1.txt
	pdflatex $<

ncbs.dvi : ncbs.tex analyze
	latex --shell-escape $<

analyze path1.txt : ./analyze.py
	python $<


