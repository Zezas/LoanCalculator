# write your code here
import math
import argparse
import sys

error_msg = "Incorrect parameters"
strange_error_msg = "not supposed to come here"

# first we parse the arguments and build the rules for it
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="choose annuity or diff")
parser.add_argument("--payment", help="monthly payment amount, a float, can only be used with --type=annuity")
parser.add_argument("--principal", help="loan principal amount, a float")
parser.add_argument("--periods", help="number of months, an int")
parser.add_argument("--interest", help="interest rate, a float, specified without a percent sign, it must always be provided")

args = parser.parse_args()

# Incorrect Parameters known combinations
if (args.type == "diff" and args.payment is not None) or (args.type != "annuity" and args.type != "diff") or args.interest is None or len(sys.argv) < 5:
    print(error_msg)

# number of monthly payments
elif args.type == "annuity" and args.payment is not None and args.principal is not None and args.periods is None:
    loan_principal = float(args.principal)
    monthly_payment = float(args.payment)
    nominal_interest_rate = float(args.interest) / (12 * 100)

    # may have error
    number_of_months = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest_rate * loan_principal), 1 + nominal_interest_rate))
    years = number_of_months // 12
    months = number_of_months % 12
    if years == 0 and months == 1:
        print(f"It will take {months} month to repay this loan!")
    elif years > 1 and months == 0:
        print(f"It will take {years} year to repay this loan!")
    elif years == 1 and months == 1:
        print(f"It will take {years} year and {months} month to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")

    overpayment = int((monthly_payment * number_of_months) - loan_principal)
    if overpayment > 0:
        print(f"Overpayment = {overpayment}")

# annuity monthly payment amount
elif args.type == "annuity" and args.payment is None and args.principal is not None and args.periods is not None:
    loan_principal = float(args.principal)
    number_of_months = int(args.periods)
    nominal_interest_rate = float(args.interest) / (12 * 100)

    # may have error
    monthly_payment = math.ceil(loan_principal * ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, number_of_months)) / (math.pow(1 + nominal_interest_rate, number_of_months) - 1)))
    print(f"Your annuity payment = {monthly_payment}!")

    overpayment = int((monthly_payment * number_of_months) - loan_principal)
    if overpayment > 0:
        print(f"Overpayment = {overpayment}")

# loan principal
elif args.type == "annuity" and args.payment is not None and args.principal is None and args.periods is not None:
    monthly_payment = float(args.payment)
    number_of_months = int(args.periods)
    nominal_interest_rate = float(args.interest) / (12 * 100)

    # may have error
    loan_principal = int(monthly_payment / ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, number_of_months)) / (math.pow(1 + nominal_interest_rate, number_of_months) - 1)))
    print(f"Your loan principal = {loan_principal}!")

    overpayment = int((monthly_payment * number_of_months) - loan_principal)
    if overpayment > 0:
        print(f"Overpayment = {overpayment}")

elif args.type == "diff" and args.payment is None and args.principal is not None and args.periods is not None:
    loan_principal = float(args.principal)
    number_of_months = int(args.periods)
    nominal_interest_rate = float(args.interest) / (12 * 100)

    # counter
    total_diff_payment = 0

    for num_month in range(1, number_of_months + 1):
        payment = math.ceil((loan_principal / number_of_months) + nominal_interest_rate * (loan_principal - ((loan_principal * (num_month - 1)) / number_of_months)))
        total_diff_payment += payment
        print(f"Month {num_month}: payment is {payment}")

    overpayment = int(total_diff_payment - loan_principal)
    if overpayment > 0:
        print(f"\nOverpayment = {overpayment}")

# Incorrect Parameters unknown combinations
else:
    print(strange_error_msg)
