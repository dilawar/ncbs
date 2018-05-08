all : logo

logo : ncbs.svg

ncbs.svg : ncbs.dvi
	dvisvgm $<

ncbs.dvi : ncbs.tex analyze
	latex --shell-escape $<

analyze: ./analyze.py
	python $<

