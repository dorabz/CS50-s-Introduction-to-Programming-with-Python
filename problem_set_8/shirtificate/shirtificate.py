from fpdf import FPDF

pdf = FPDF()
text = input("Text:")
pdf.add_page(orientation="portrait", format="A4")
pdf.set_font("times", size=12)
pdf.cell(txt="CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", alt_text="CS50 Shirtificate")
pdf.text(x = 0, y = 0, txt = text + "took CS50")
pdf.output("shirtificate.pdf")
