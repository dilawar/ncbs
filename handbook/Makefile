all : ./handbook.tex 
	pdflatex --shell-escape $<

doc : ./student_handbook.markdown
	~/Scripts/markdown_to_pdf.sh $<
