CALS:=calendar_intphd.svg ./calendar_msc.svg ./calendar_phd.svg ./title.pdf
all : ./student_handbook.markdown.pdf ./student_handbook.markdown.epub
	
student_handbook.markdown.pdf : student_handbook.markdown $(CALS)
	pandoc -fmarkdown --template ./default.latex $< -o $@

student_handbook.markdown.epub : student_handbook.markdown $(CALS)
	pandoc -fmarkdown $< -o $@

%.pdf : %.tex
	pdflatex --shell-escape $<

%.svg : %.tex
	pdflatex --shell-escape $<
