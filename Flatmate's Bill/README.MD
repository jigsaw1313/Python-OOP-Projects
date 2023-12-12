# Flatmates Bill

## Description

Flatmates Bill is an app that calculates and divides a bill among flatmates based on the number of days each flatmate stayed in the house during a specific period. Additionally, it generates a PDF report detailing each flatmate's name, the bill period, and the amount they need to pay.

## Objects

### Bill
- **Amount:** Total amount of the bill.
- **Period:** Timeframe for the bill.

### Flatmate
- **Name:** Name of the flatmate.
- **Days_in_house:** Number of days the flatmate stayed in the house during the bill period.
- **pays():** Method to calculate the share of the bill a flatmate needs to pay.

### Pdf Report
- **Filename:** Name of the PDF file.
- **Generate(flatmate1, flatmate2, bill):** Method to generate a PDF report with details of flatmates' shares and bill period.

## Usage

1. Input the bill amount and period.
2. Enter details for each flatmate, including their name and the number of days they stayed in the house.
3. The app calculates and displays the amount each flatmate needs to pay.
4. A PDF report is generated and opened in your default web browser, providing a detailed breakdown of the bill.

**Note**: You can try this app by using this [link](https://replit.com/@mrmhmdi93/flatmate?embed=1)

## How to Run

1. Clone the repository.
2. Run `main.py` in your Python environment.
3. Follow the prompts to input bill details and flatmates' information.

## Dependencies

- fpdf
- webbrowser
- filestack

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
