savat = []
while True:
    savol = input("Mahsulot nomini kiriting : ")
    savat.append(savol)
    javob = input("Yana mahsulot qo'shasizmi (ha\yo'q) : ")
    if javob == 'yo\'q':
        break
print(f"Sizning buyurtmalaringiz {savat}")
    