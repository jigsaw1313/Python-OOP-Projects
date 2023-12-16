import webbrowser
import os
import filestack
from fpdf import FPDF


class PdfReport:
    """
    creates a pdf file that contains data about flatmates
    such as their names, due amount and period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icon
        pdf.image("files/house.png", w=30, h=30)

        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of fist flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of fist flatmate
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(f"Reports/{self.filename}")

        os.chdir('Reports')
        webbrowser.open(self.filename)


class FileSharer:
    """
    creates a link to generated report.
    """
    def __init__(self, filepath, api_key='AYCRt4NjvSZW3lXvY3xhwz'):
        self.file_path = filepath
        self.api_key = api_key

    def share(self):
        client = filestack.Client(self.api_key)
        new_filelink = client.upload(filepath=self.file_path)
        return new_filelink.url