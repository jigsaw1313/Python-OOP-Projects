from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

# receives data of bill from user
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2023 ")

name1 = input("What is your name? :")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is your flatmate's name? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

# create classes objects
bill_ = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)
print(f"{name1} Pays: ", flatmate1.pays(bill_, flatmate2))
print(f"{name2} Pays: ", flatmate2.pays(bill_, flatmate1))

# generate pdf report of flatmate's bill
pdf_report = PdfReport(f"{bill_.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill_)

# file sharer to generate reports via web.
file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
