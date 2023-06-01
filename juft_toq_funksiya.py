#Foydalanuvchidan ikkita son olib, 
#ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
#Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def katta_kichik(number1,number2):
    '''Sonlarni taqqoslaydigan funksiya'''
    if number1 > number2:
        print(f"{number1} > {number2}")
    elif number1 < number2:
        print(f"{number2} > {number1}")
    else:
        print(f"{number1} = {number2}")

katta_kichik(1,-10)




































































