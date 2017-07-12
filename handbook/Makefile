all : ./handbook.pdf ./student_handbook.markdown.pdf 
	
handbook.pdf : handbook.tex 
	pdflatex --shell-escape $<

student_handbook.markdown.pdf : student_handbook.markdown
	~/Scripts/markdown_to_pdf.sh $<
