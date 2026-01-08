import math

#display the menu for the user to make their choice
menu='''                    MENU
Please choose what you want:
                            Choose:investment, bond or stop
1.Investment-to calculate the amount of intrestnyou will earn on your investment.
2.Bond-to calculate the amount you will pay foron your home loan.
3.Stop-to cancel
'''
#prompts user to enter a number between 1 and 10 to start the process
#used while loop to make sure l get a numeric value between 1 and 10


while True:
    
    try:
        user_num=int(str(input("Welcome to Hyperion Financial Company!.Please enter any number between 1 and 10: ")))
        if user_num >=1 and user_num <= 9:
            
            print(menu)
        
        else:
             print("Error ,Try again.")
        SystemExit
                 
    
        break

    except ValueError:

        print("Invalid Entry, Try Again")

    SystemExit
 
#ask user to choose between bond, investment or stop

user_choice=str(input("Please enter investment, bond or stop: "))
user_choice=user_choice.lower()
if user_choice!="bond" and user_choice != "investment" and user_choice != "stop":
        print("Invalid Entry!!,Try Again.")


if user_choice=="investment":
#Getting input from the user on deposit money,interest rate and the number of years they want to invest.
#user has to choose the interest type they want
    deposit_money=float(input("How much do you want to deposit?: \n"))
    interest_rate= float(input("Enter your interest rate as a number for example 5, 8,4 etc: \n"))
    num_yrs=float(input("Please enter the number of years you are planning on investing: \n"))
    interest_type=(input("Choose if you want compound interest or simple intrest: \n"))
    interest_type=interest_type.lower()
    print(interest_type)
    
#rounding the totals to 2 decimal place
    if interest_type=="simple":
        total_simp=round(deposit_money*(1 +(interest_rate/100)*num_yrs),2)
        print(f"The total amount you will earn is ${total_simp} after investing for {num_yrs} years at an interest rate of {interest_rate}%.")
    
    elif interest_type=="compound":
        total_comp=round(deposit_money*math.pow(1 + (interest_rate/100),num_yrs ),2)
        print(f"The total amount you will earn is ${total_comp} after investing for {num_yrs} years at an interest rate of {interest_rate}%")

#Getting input from user on their house value, interest rate they want and the number of months they want to repay.
if user_choice=="bond":
        house_val=float(input("Please enter the value of the house: \n"))
        intrate_mon= float(input("Please enter your monthly interest rate: \n"))
        num_months=float(input("Please enter the number of months you want to repay: \n"))
        monthly_repay= round((intrate_mon/100/12 * house_val) / (1 - math.pow((1+ intrate_mon/100/12), (-1 * num_months))), 2)
        print(f"Your monthly repayment for your home loan is ${monthly_repay}. \n")

if user_choice=="stop":
    print("Thank you, see you next time.")