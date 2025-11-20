from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

# Title
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Making PDF using Python", align='C', ln=1)

# Body text
pdf.set_font(family='Times', size=12)
text = (
    "Creating PDFs in Python is simple and efficient with the FPDF library. "
    "It allows you to add pages, write text, insert images, and customize layout "
    "with minimal code. FPDF is lightweight, easy to learn, and works without external "
    "dependencies. By using functions like add_page(), set_font(), and cell(), you can "
    "quickly generate clean, professional PDF documents for reports, invoices, or automation tasks."
)

pdf.multi_cell(w=0, h=18, txt=text)

pdf.output("output.pdf")

