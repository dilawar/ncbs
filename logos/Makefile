all : logo

logo : ncbs.svg

ncbs.svg : ncbs.dvi
	dvisvgm $<

ncbs.dvi : ncbs.tex
	latex --shell-escape $<

ncbs.tex : ./analyze.py
	python $<

