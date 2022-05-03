
# def arithmetic(a,b,arg):
#     a = int(input("Биринчи сонни киритинг: "))
#     b = int(input("Иккинчи сонни киритинг: "))
#     arg = str(input("Арифметик (+,-,*,/) амални киритинг: "))
#     if arg == "+":
#         return a+b
#     elif arg == "-":
#         return a-b
#     elif arg == "*":
#         return a*b
#     elif arg == "/":
#         return a/b
#     else:
#         return "Неизвестная операция"
# print(arithmetic(5,10,"*"))


# def is_year_leap(year):
#     year = int(input("Yilni kiriting:"))
#     if year%2==0 and year%4==0:
#         return True
#     else:
#         return False
# print(is_year_leap(2022))

# def square(a):
#     c = list()
#     per = 4*a
#     s = a*a
#     diag = (a*a + a*a)**(1/2)
#     c.append(per)
#     c.append(s)
#     c.append(diag)
#     c = tuple(c)
#     return c
# print(square(4))
# print(square(3))
# print(square(5))
# def square2(b):
#     return (b*4, b*b, b*(2)**(1/2))
# print(square2(5))

# def season(x):
#     if x==12 or 1<=x<=2:
#         return "Qish fasli"
#     elif (3<=x<6):
#         return "Bahor fasli"
#     elif 6<=x<9:
#         return "Yoz fasli"
#     elif (x>=9 and x<=11):
#         return "Kuz fasli"
#     else:
#         return "Son kiritishda xatolik"
# print(season(1))
# print(season(2))
# print(season(3))
# print(season(4))
# print(season(5))
# print(season(6))
# print(season(7))
# print(season(8))
# print(season(9))
# print(season(10))
# print(season(11))
# print(season(12))
# print(season(121))

# def bank(a,years):
#     a = int(input("Pul miqdorini kiriting(so'mda): "))
#     years = int(input("Necha yilga qo'ymoqchisiz: "))
#     years = years+1
#     for i in range(1,years):
#         a += a*0.1
#     return a
# print(bank(1,10))

# def is_prime(a):
#
#     f=True
#     for i in range(2,int(a**0.5)):
#         if a%i==0:
#             f=False
#     return(f)
# b = int(input("N son kiritng: "))
# print(is_prime(b))


# from cmath import sqrt
#
# def is_prime(number):
#     # Все четные числа кроме 2 непростые
#     if number % 2 == 0 and number != 2:
#         return False
#     # 0 и 1 не являются простыми
#     if number == 0 or number == 1:
#         return False
#     # Перебираем числа от 3 до корня из введенного, шаг - 2
#     for n in range(3, int(sqrt(number).real) + 1, 2):
#         if number % n == 0:  # Если число делится нацело, то оно непростое
#             return False
#     return True  # Остальные числа простые

print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
savol = "Istalgan son kirting "
savol += "dasturni to'xtatish uchun 'exit' deb yozing  "
# qiymat = ''
# practice qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi")
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        continue
        # break
        # ishora=False
    else:
        print(float(qiymat)**2)
print("Dastur tugadi")