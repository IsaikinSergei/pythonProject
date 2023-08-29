
# УСЛОВНЫЕ ОПЕРАТОРЫ:

# user_data = int(input("Введите число: "))
# isHappy = True
# if not isHappy:
#     print("I'am happy")
# elif user_data == 5:
#     print("Good job!")
# else:
#     print("User is unhappy")

# Тернарный оператор:

# data = input()
#
# number = 5 if data == "Five" else 0

# if data == "Five":
#     number = 5
# else:
#     number = 0
# print(number)

# ЦИКЛЫ И ОПЕРАТОРЫ:

# for i in range(6):
#     print(i)

# count = 0
# word = "Hi, Sergei!"
# for i in word:
#     if i == "i":
#         count += 1
#
# print(count)

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

found = None
for i in "Hello":
    if i == "l":
        found = True
        break
    else:
        found = False
print(found)


