# son = int(input("Juft son kiring: "))
# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas.")
#

# yosh = int(input("Yoshingizni kiriting: "))

# if yosh <= 4 or yosh >= 60:
#     print("Sizga kirish bepul")
# elif yosh < 18:
#     print("Sizga kirish 10000 so'm")
# else:
#     print("Sizga kirish 20000 so'm")

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
#
# if a < b:
#     print("Ikkinchi son katta")
# elif a > b:
#     print("Birinchi son katta")
# else:
#     print("Sonlar teng")


# login = input("Login ismingizni kiriting: ")
#
# if login == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")

# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
#
# if x == y:
#     print("Sonlar teng ekan")
# else:print("Sonlar teng emas")

# son = int(input("Istalgan son kiriting: "))
#
# if son < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

# son = int(input("Son kiriting: "))
#
# if son >= 0:
#     print(son ** 0.5)
# else:
#     print("Musbat son kiriting")

# mahsulotlar = ["olma", "uzum", "anor", "behi", "nok", "banan", "o'rik", "shaftoli", "gilos", "xurmo"]
# savat = []
#
#
# for n in range(5):
#     meva = input(f"Savatga {n+1}-mahsulotni qo'shing: ")
#     savat.append(meva)
#
#
# for meva in savat:
#     if meva in mahsulotlar:
#         print(f"Do'konimizda {meva} bor")
#     else:
#         print(f"Do'konimizda {meva} yo'q")


# mahsulotlar = ["olma", "uzum", "anor", "behi", "nok", "banan", "o'rik", "shaftoli", "gilos", "xurmo"]
# bor_mahsulotlar = []
# mavjud_emas = []
#
# for n in range(5):
#     meva = input(f"Savatga {n+1}-mahsulotni qo'shing: ")
#     if meva in mahsulotlar:
#         bor_mahsulotlar.append(meva)
#     else:
#         mavjud_emas.append(meva)

# if len(mavjud_emas) == 0:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:", mavjud_emas)