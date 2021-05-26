#PIP INSTALL FPDF
from fpdf import FPDF
PDF=FPDF()
PDF.add_page()
PDF.set_font("Arial",size=25)
#create a cell
PDF.cell(200,10,txt="Dynamic Coding",ln =1,align='C')
PDF.cell(200,10,txt="A place For python Programmmers",ln =2 , align='C')
PDF.output("Data.pdf")