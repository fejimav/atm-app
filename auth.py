#register
# email, names, username and password would be supplied
# generate account number

#login
# bankaccount and password

#banking operations
import random
database = {
    3232346352:["fejiro","akpomuetata", "ofejiromav@gmail.com", "fejiro1234", 0]
}

def initialize():
    isvalidoptionselected = False
    print("Welcome to Bankfeji")

    while isvalidoptionselected == False:

        selected_option = int (input("do you have an account with us  1(yes) 2(no) \n"))
    
        if selected_option==1:
            login()
            isvalidoptionselected = True
        elif selected_option==2:
            register()
            isvalidoptionselected = True
        else:
            print ("invalid option selected")


def login():
    print ("Welcome")
    print("please login")

    
    accountnumberfromuser = int(input("account number? \n"))
    password = input("your password \n")
    for accountnumber, userdetails in database.items():
        if accountnumberfromuser == accountnumber:
            if userdetails[3] == password: 
               bankoperations(userdetails) 

            else:
                print("Invalid Account number or password")
                login()

    
def register():

    print("*********Register********")

    email = input("what is your email address \n")
    first_name = input("what is your firstname\n")
    last_name = input("what is your lastname \n")
    password = input("create a password,  must be 8 digits long \n")
    accountnumber = account_generation()

    database[accountnumber] = [first_name, last_name, email, password, 0]
    print (accountnumber)

    print ("Account creation successful")
    login()
def account_generation():
    return random.randrange(1111111111,9999999999)
def bankoperations(user):
    print ("welcome %s %s" % (user[0], user[1]) )
    option = int (input ("Please select a number 1(withdrawal) 2 (deposit) 3 (complaints) 4 (logout) 5 (exit) \n"))
    if option == 1:
        withdrawal()
    elif option == 2:
        deposit()
    elif option == 3:
        complains()
    elif option == 4:
        logout()
    elif option == 5:
        exit()
    else:
        print("invalid option selected")
        bankoperations(userdetails)
def withdrawal():
    amountwithdrawn = int(input ("How much would you like to withdraw \n"))
    print("please take your cash")
    bankoperations(user)
def deposit():
    deposit = int(input ("how much would you like to deposit \n"))
    print ("your deposit is succesful")
    bankoperations(user)
def complains():
    complaints = input ("Please state your complaint \n")
    print("your complaints has been noted and sent to the appropriate unit")
    bankoperations(user)
def get_current_balance (userdetails):
    return userdetails[4]
def logout():
    print("thank you for banking with us")
    initialize()

initialize()
