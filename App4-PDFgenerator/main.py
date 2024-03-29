from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)  # RGB - 100, 100, 100 - grey colour
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # set the footer
    pdf.ln(265)  # adds empty break lines
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
