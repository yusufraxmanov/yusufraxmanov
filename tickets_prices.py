
price1 = 2000
price2 = 3000
price3 = 10000
price4 = 0 
age = "Enter your age"
age += " (write the word 'quit' or 'exit' to stop the program) : "
while True:
    user = input(age)
    if user == 'exit' or user == 'quit':
        break
    user1 = int(user)
    if user1 <= 7:
        print(f"Ticket's price is {price1} so'm")
    elif user1 >= 7 and user1 <= 18:
        print(f"Ticket's price is {price2} so'm")
    elif user1 >= 18 and user1 <= 65:
        print(f"Ticket's price is {price3} so'm")
    elif user1 >= 65:
        print(f"Ticket's price is {price4} so'm")
print("Program completed !")
