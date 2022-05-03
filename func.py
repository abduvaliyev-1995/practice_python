
# def salom():
#     """Salom berguvchi funksiya"""
#     print("Assalomu alaykum!")
# salom()

# def salom(ism): #ism dasturchilar nazdida parametr, foydalanuvchi esa argument deb qaraydi
#     """Salom berguvchi funksiya"""
#     print(f"Assalomu alaykum! {ism.title()}")
#     return f"Assalomu alaykum! {ism.title()}"
# salom('hasan')
# sa = salom('jumavoy')
# print(sa)

# def toliq_ism(ism,familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism.title()} {familiya.title()} {otasining_ismi.title()}"
#     else:
#         toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
# print(toliq_ism('hasan','salimov')) #bunda natijani chop etyapti
# #Endi returndan qaytgan natijani chop etish uchun f-yani biror o'zgaruvchiga yuklash lozim
# t_ism = toliq_ism('kaim','lazizov')
# t_ism2 = toliq_ism('kaim','lazizov','husanovich')
# print(t_ism)
# print(t_ism2)

def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto={
        'kompaniya':kompaniya,
        'model':model,
        'rangi':rangi,
        'korobka':korobka,
        'yili':yili,
        'narxi':narxi
    }
    return avto
# avto1=avto_info("GM",'Malibu',"Oq","Avto",2018,12000)
# avto2=avto_info("GM",'Tico',"Ko'k","mexanik",1995)
# avtolar = [avto1,avto2]
# print(f"Onlayn bozordagi mavjud avtomashinalar: {avtolar}")
# for avto in avtolar:
#     if avto['narxi']:
#         narxi=avto['narxi']
#     else:
#         avto['narxi']="Noma'lum"
#     print(f"""{avto['rangi']} {avto['model']}. Narxi:{avto['narxi']}""")

# def oraliq(min,max,qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min = min + qadam
#     return sonlar
# print(oraliq(10,16,2))
# print(list(range(10,16,2)))

# def avto():
#     print("saytimizdagi avtolar ro'yxatini shakllantiramiz: ")
#     avtomobillar = []
#     ishora = True
#     while ishora:
#         print("Quyidagi ma'lumotlarni kiriting: ", end=' ')
#         kompaniya = input("Ishlab chiqaruvchi: ")
#         model = input("Modeli: ")
#         rangi = input("Rangi: ")
#         korobka = input("Korobka turi: ")
#         yili = input("Ishlab chiqarilgan yili: ")
#         narxi = input("Narxi: ")
#         avtomobillar.append(avto_info(kompaniya,model, rangi, korobka, yili, narxi))
#
#         ishora2=True
#         while ishora2:
#             savol = input("Yana ma'lumot kiritasizmi?(ha/yo'q): ")
#             if savol == 'ha' or savol == "yo'q":
#                 if savol != 'ha':
#                     ishora2=False
#             else:
#                     ishora2=True
#                 # return "Siz faqat ha/yo'q deb yozishingiz mumkin!"
#                     print("Siz faqat ha/yo'q deb yozishingiz mumkin!")
#     print(avtomobillar)
# avto()




