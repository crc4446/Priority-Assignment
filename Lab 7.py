#This program determines which customers get priority treatment, normal treatment, or dropped.
#Created by: Chris Caponi 
while flag:
        
    name = input("Name of Customer:  ")
    amount = float(input("Amount of business customer does with us per year:  "))
    howLong = int(input("How long the customer has been with us:  "))
    payHis = input("Does the customer have a good payment history?  ")
    while payHis != "Yes" and payHis != "No":
        print("Please answer with Yes or No.")
        payHis = input("Does the customer have a good payment history?  ")
    
    if (amount >= 10000 and (howLong > 20 or payHis == "Yes")):
        print(name,"should get priority treatment.")
            
    elif ((amount < 10000 and howLong <= 20)and(payHis == "No")):
        print("Let's drop",name)
    else: 
        print(name,"should get standard treatment.")
        
    answer = input("Would you like to enter another customer? ")
    if (answer == "No"):
        flag = False
        if (answer == "Yes"):
            flag = True
    




