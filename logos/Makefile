all : pattern ./ncbs_logo.pdf 

%.pdf : %.tex
	pdflatex $<

pattern : ./analyze_pattern.py
	python3 $<
