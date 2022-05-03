#
# print("Do'stlaringiz ismlari ro'yxatini tuzamiz:")
# ismlar = []
# n=1
# practice True:
#     savol = f"{n}-do'stingiz ismini kiritng: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takror = input("Yana ism qo'shasizmi?(ha/yo'q): ")
#     n += 1
#     if takror != 'ha':
#         break
#
# print(f"Do'stlaringiz ro'yxati{ismlar}")


# print("Do'stlaringiz ismlari ro'yxatini tuzamiz:")
# dostlar = {}
# n=1
# ishora =True
# practice ishora:
#     savol = f"do'stingiz ismini kiritng: "
#     ism = input(savol)
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#     takror = input("Yana ism qo'shasizmi?(ha/yo'q): ")
#     n += 1
#     if takror != 'ha':
#         ishora=False
# print(f"Do'stlaringiz ro'yxati ")
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['tico','malibu','tico','nexia','tico','nexia','malibu','damas']
# car = 'tico'
# practice car in cars:
#     cars.remove(car)
# print(cars)
students = ['karim','salim','olim','naim']
baholanganlar = {}

while students:
    talaba = students.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholanganlar[talaba]=int(baho)

for talaba,baho in baholanganlar.items():
    print(f"{talaba.title()}ning bahosi-{baho}")





