CALS:=calendar_intphd.pdf ./calendar_msc.pdf ./calendar_phd.pdf
all : ./student_handbook.markdown.pdf 
	
student_handbook.markdown.pdf : student_handbook.markdown $(CALS)
	pandoc -fmarkdown $< -o $@

%.pdf : %.tex
	pdflatex --shell-escape $<
