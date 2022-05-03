
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

# ====================================
# def kwargs(**kwargs):              |
#     print(kwargs)                  |
#     for key in kwargs:             |
#         print(key)                 |
#                                    |
# kwargs()                           |
# kwargs(a=2,b=4,w=12)               |
#=====================================
# def args(*args):
#     print(args)
#
# args(2,4,12,12)
# args()

# def kwargs(**kwargs):
#     print(kwargs)
#     for key,val in kwargs.items():
#         # print(key,'-->',val)
#         print("%s == %s" %(key,val))
# kwargs()
# kwargs(a=2,b=4,w=12)

# def max_num(a,b,c):
#     max = 0
#     if a>=b and a>=c:
#         max=a
#     elif b>=a and b>=c:
#         max=b
#     else:
#         max=c
#     return max
# print(max_num(23,-10,-60))
# def max_two(a,b):
#     max=0
#     if a>b:
#         max=a
#     else:
#         max=b
#     return max
# print(max_two(5,4))
# 
# def max_three(x,y,z):
#     return max_two(x,max_two(y,z))
# print(max_three(10,11,19))

# def sum_list(*args):
#     total=0
#     for i in args:
#         total +=i
#     return total
# print(sum_list(10,20,15,15,100))
# print(sum_list(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
#
# def multiply_nums(*args):
#     total = 1
#     for arg in args:
#         total *=arg
#     return total
# print(multiply_nums(10,-1,20,12))
# print(multiply_nums(10,-1,20,12,0))
#
# def rev_str():
#     text = str(input("Matn kiriting: "))
#     reverse = ''
#     index = len(text)
#     while index>0:
#         reverse += text[index-1]
#         index = index - 1
#     return reverse
# print(rev_str())
# def factorial(n):
#     calc = 1
#     if n>0:
#         if isinstance(n,int):
#             # if n>0:
#             while n>0:
#                 calc *= n
#                 n=n-1
#         else:
#             return f"{n} butun son emas"
#     else:
#         print(f"{n} noldan kichik")
#         # return f"{n} noldan kichik yoki butun son emas"
#     return calc

# print(factorial(5))
# # print(factorial(-3))
# print(factorial(1.3))
# print(factorial(1000))
#
# def in_range(n):
#     # n = input("Son kiritng: ")
#     if n in range(2,12):
#         return f"number {n} falls in s given range"
#     else:
#         return f"{n} not falls in a given range"
# print(in_range(5))
# print(in_range(-1))
#
# def calc_string():
#     matn = str(input("Biror matn kiriting: "))
#     text = list(matn)
#     index = len(text)
#     upper = 0
#     lower = 0
#     other = 0
#     while index>0:
#         index = index-1
#         if text[index].islower():
#             lower +=1
#         elif text[index].isupper():
#             upper +=1
#         else:
#             other +=1
#     return f"'{matn}' da {lower} ta kichik va {upper} ta katta harf mavjud, boshqa belgilar soni esa {other} ta"
# print(calc_string())
#
# def list_unique(*args):
#     l_set = set(args)
#     list_last = list(l_set)
#     sort = sorted(list_last, reverse=False)
#     return sort
# print(list_unique(2,2,2,2,2,1,1,1,15,0,55,5,5,5))
# print(list_unique(2,1,4,-8,9,10,-7,58,2,2,2,1,1,1,3,3,3,8,9,9,10))

# def is_prime(n):
#     if isinstance(n,int):
#         if n==2 or n==1:
#             return "Enter number greater than 2"
#         elif n%2 == 0:
#             return f"{n} is even number, even numbers can not prime"
#         elif n>2:
#             for i in range(2,n//2):
#                 if (n%i)==0:
#                     return f"{n} is not prime"
#                     # break
#             else:
#                 return f"{n} is prime"
#     else:
#         return f"{n} is not natural number"

