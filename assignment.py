#Question 1
#The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of a sphere with radius 5.
#Make sure the program enters the radius from the keyboard and provides the answer in 2 decimal places.

#solution
radius = float(input("Enter the radius of the sphere:"))
volume =float((4/3)*(22/7)*radius**2)
print(f"The volume of a sphere with radius{radius} is: {volume:.2f}")

#Question 2
#create a program to calculate the area of a triangle (1/2*base*height).Base and height
# should entered using the keyboard.

#solution
base =int(input("Enter the base of a triangle:"))
height=int(input("Enter the height of a triangle:"))
area = (1/2*base*height)
print(f"The area of a triangle with base {base} and height {height} is :{area}")


# question three
#WITI has tasked you to automate a simple grading system.As apython student , write a program to
#display the grades that the students will be receiving based on the mark scored in a subject. The grade are;
#90%-100% Grade is A
#80%-89% Grade is B
#70%-79% Grade is C
#60%-69% Grade is D
#50%-59% Grade is E
#< 50% Fail

#solution
def calculate__the_grade():

    print("\n...studentgrade;")
    mark = int(input("Enter student mark :\t"))

    if mark >= 90 and mark<=100:
        print("Grade is A")

    elif  mark >= 80 and mark<=89:
        print("Grade is B")

    elif mark>= 70 and mark <=79:
        print("Grade is C")

    elif mark >= 60 and mark <=69:
        print("Grade is D")

    elif mark>=50 and mark <=59:
         print("Grade is E")

    else:
        print("fail") 
calculate__the_grade()        


#WITI Academy is proposing a Sacco to help students save their money.Design a platform that will do 
# the following .
#Welcome to WITIAcademy Sacco.
#1.Deposit Money
#2. withdraw Money
#3.check balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#If the student selects 2, money should be withdrawn and aminimum withdrawal is 500.
#If the student selects 3, the actual balance should be displayed.

# solution.
def witi_sacco_transactions():

 account_balance = 0
 run = 1

 while run == 1:
     print("\nwelcome to WITI Academy Sacco.")

     print("1.Deposit Money")
     print("2.withdraw Money")
     print("3.Check balance") 

     student_choice = int(input("Enter your selection(1,2,or 3):"))

     if student_choice == 1:
         print("\n...processing a deposit...")

         deposit_amount= int(input("Enter amount to be deposited: "))

         #if the deposit amount is< 1000
     else:
         deposit_amount<1000
     print("\n minimum deposit is 1000")
             
 account_balance += deposit_amount
 print(f"Dear student, you have deposited {deposit_amount:,} and your new account balance is {account_balance:,}")

 if student_choice == 2:
  print("\n processing withdraw amount...")
  withdraw_amount= int(input("Enter amount to be withdrawn : "))
 if account_balance == 0:
             print("your account balance is 0)")
 elif withdraw_amount < 500:
             print("minimum withdraw amount is 500")

 elif withdraw_amount > account_balance:
             print(f" withdraw failed ,insufficient funds.")

 else:
             account_balance-=withdraw_amount
             print(f"Dear student you have withdrawn{withdraw_amount:,} and your new account balance is {account_balance :}")
              
 if student_choice == 3:
         
         print(f"Your account balance is {account_balance:,}")
         
 else:
         print("You entered a wrong choice !! Please select 1,2.or 3\n ")

         run = int(input("Enter 1 to continue and any number to exit:"))

         if run!= 1:
          print("Thank you for using our sacco.")
          
witi_sacco_transactions()        