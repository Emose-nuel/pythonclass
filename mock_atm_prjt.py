from datetime import datetime
import random

random.seed(1)

allowed_users= ['Seyi', 'Mike', 'Love', 'John', 'Samuel', 'Jerimiah']
allowed_password =[f'password{i}' for i in allowed_users]
Balance = {i:random.randrange(0, 100000) for i in allowed_users}



def check (name, password):
    userID = allowed_users.index(name)
    if (name in allowed_users) and (password == allowed_password[userID]):
            return True
    else:        
        return False

    
def check_credentials(name, password):
        
    if check (name, password):
       print(f"Welcome {name}, Logged in on {datetime.now().strftime('%B %d, %Y %H:%M:%S')} \n")               
       return True           
    else:
        print ("Invalid Credentials! \n")
        return False
                   
def transaction( name, password):    
    print ("\nWhat Would You Like To Do: \n 1. Make A Withdrawal \n 2. Cash Deposit \n 3. Submit A Complaint \n 4. Check Balance")          
    option = int(input("Please select an option: \n"))

    if option == 1:            
        withdraw = float(input("How Much Would You Like To Withdraw? \n")) 
        if withdraw <= Balance[name]:
            Balance[name] -= withdraw
            print('Please Take Your Cash!')
        else:
            print('You Have Insufficient Funds To Complete This Transaction')
    
    elif option == 2:
        print("You have selected: 2. Cash Deposit")
        deposit = float(input("How Much Would You Like To Deposit? \n")) 
        Balance[name] += deposit
        print(f"Deposit of ${deposit} was successful! \nYour Current Balance is ${Balance[name]}")
        
    elif option == 3:
        print("You have selected:  3. Submit A Complaint")
        complaint = input("What issue will you like to report? \n")
        print("\nThank you for contacting us!")
        
    elif option == 4:
        print("You have selected: 4. Check Balance \n")
        print(f"Your Available Balance is ${Balance[name]}")
        
    else :
        print("Invalid Option Selected, Please Try Again \n")
          
def mock_atm():
    name = input("Please Enter Your Name: \n")
    password = input ("Please Enter Your Password: \n")
        
    if check_credentials(name, password):        
        transaction(name, password)   
        print("\nWould You Like To Perform Another Transaction?")
        response = input("Yes or No \n").lower()
        
        while response == 'yes':
            transaction(name, password)
            print("\nWould You Like To Perform Another Transaction?")
            response = input("Yes or No \n").lower()    
        print("Do Have A Nice Day!")
    else:
        reply = input("Would You Like To Try Again? \n Enter Yes or No: \n ").lower()
        if reply == 'yes':
            mock_atm()
        else:
             print("Do Have A Nice Day!")

if __name__ == "__main__" :
    mock_atm()
