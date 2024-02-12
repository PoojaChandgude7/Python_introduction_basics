'''
per = float(input('Enter percentage you get:'))
if 40 <= per < 49:
    print('Pass class')
elif 50 <= per < 59:
    print('2nd class')
elif 60 <= per < 69:
    print('1st class')
elif 70 <= per <= 100:
    print('Distinction')
elif per > 100:
    print('Enter valid marks')
else:
    print('fail')

#ATM PIN program by using if statement
print("Welcome to State bank of India")
x = int(input('Enter 4 digit ATM PIN:-'))
amount = 100000
if x == 1800:
    print("1-Withdraw")
    print("2-Balance Enquiry")
    print("3-Fast Cash")
    y = int(input("Please choose transactions: "))
    if y == 1:
        z = int(input("Enter withdraw amount: "))

        if z < amount and z % 100 == 0:
            print("Please take your amount:", z)
        else:
            print("Invalid cash")

    elif (y == 2):
        print("Your available amount : ", z)

    elif (y == 3):
        print("1->20,000")
        print("2->40,000")
        print("3->60,000")
        print("4->80,000")
        f = int(input("Enter fast cash option: "))
        if (f == 1 and 20000 < z):
            print("please take cash 20000")
        elif (f == 2 and 40000 < z):
            print("please take cash 40000")
        elif (f == 3 and 60000 < z):
            print("please take cash 60000")
        elif (f == 4 and 80000 < z):
            print("please take cash 80000")
        else:
            print("Invalid fast cash option")

    else:
        print("Wrong pin number")

#Lottery Program using ‘if’ statement.
print ("Welcome to Pooja Lottery")
l = int (input("Enter Your 4 digit Lucky Coupon Number: "))
if (l== 1900) or (l==3745) or (l==4077):
    print ("you wan Car:")
elif (l==6677) or (l==7075) or (l==8097):
    print ("you Won a Bike")
elif (l==2267) or (l==2948) or ( l==8990):
    print("You Won A Gift Coupon")
else:
    print("You Are Not A Winner")
    print("Better Luck Next TIme")
'''

