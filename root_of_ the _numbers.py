savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    user = float(qiymat)
    if user >= 0:
        print(f"{user} ning ildizi {user**0.5} ga teng")
    elif user < 0:
        print("Musbat son kiriting !")
print("Dastur tugallandi !")