print("This application requests your favorite book and outputs them to the console")
book = "Enter your favorite book"
book += " (write the word 'stop' to stop the program) : "
answer = ''
while answer != 'stop':
    answer = input(book).lower()
    if answer != 'stop':
        print(answer.title())
print("Program completed")    
        