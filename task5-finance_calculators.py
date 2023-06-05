#Financal Calculation - Import Maths

#introduction text

print("Welcome, Please Follow These Instructions:")
print("Please type Which Calulation input You Require from the list below:")
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan Enter either")

#user inputs investment or bond

input_string = input("please choose either - Investment or Bond:" "\n").lower()

user_input = input_string

#depending on input if, elif or else will divert the user to different strings 

if user_input == ("investment"):
    print("Thank your choosing Investment")
    investment = float(input("please enter the amont you wish to deposit:""\t"))
    interest = float(input("Please type the amount of interest you would like to pay, do not add '%' after ypur entry thanks:""\t"))
    no_year = float(input("please enter the length of time you plan to invest in years:""\t"))
    com_sim = input("please select with you would like either simple or compound intrest:""\t").lower()

#the inputs allow the information to be gathered so the calculations can be worked out
    total_after_simple_interest = 0.0
    if com_sim == ("simple"):
         interest_rate = (interest / 100)
         #interest needs to be calulated before final calulation can be made
         total_after_simple_interest = investment*(1 + interest_rate*no_year)
         simple_int = total_after_simple_interest - investment
         print("simple intrest is", simple_int)
         print("the total after simple interest = \t\t" + str(round(total_after_simple_interest, 2)))

         #if elif is selected a new set of calulation are used. 

    elif com_sim == ("compound"):
        total_after_compound_interest = investment * (pow((1 + interest / 100), no_year))
        Compound_int = total_after_compound_interest - investment
        print("Compound interest is", Compound_int)
        print("total after compound interest = \t\t" + str(round(total_after_compound_interest, 2)))



elif user_input == ("bond"):
    print("thank you for choosing bond")
    house_value = float(input("please enter your current house value, do not include currency symbol:" "\t"))
    annual_interest = float(input("please enter your annual interest rate:" "\t"))
    duration = float(input("please enter the number of months you wish to repay the bond:" "\t"))

    #using each individual value we can now create the calculation 

    monthly_interest_rate = (annual_interest / 100 / 12)
    repayment = (monthly_interest_rate*house_value)/(1-(1 + monthly_interest_rate)**(-duration))
    #after adding in the calculation for the bond i notices it only gave a complete total not a monthly so an addition calculation was needed
    monthly_repayment = (repayment - house_value)/duration
    print("your total repayment would be = \t\t" + str(round(repayment, 2)))
    print("your monthly repayment would be = \t" + str(round(monthly_repayment, 2)))

else:
    print("ERROR")
    print("please try again, check your spelling")

#if user writes an incorrect input or a spelling mistake this error message will show