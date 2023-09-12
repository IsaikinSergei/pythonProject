
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

# found = None
# for i in "Hello":
#     if i == "l":
#         found = True
#         break
#     else:
#         found = False
# print(found)

# СПИСКИ, ФУНКЦИИ и их МЕТОДЫ:
# nums = [2, 10, 7, True, "Hello, Python!", 9.33, [5, 99]]
#
# nums[1] = 27
# nums[4] = False
#
# print(nums[-1][1])

# numbers = [3, 5, 10]
#
# numbers.append(100)
# numbers.insert(1, True)
#
# b = [3, 77, 9]
# numbers.extend(b)
# numbers.sort()
# numbers.reverse()
#
# numbers.pop(0)
# numbers.remove(77)
#
# #numbers.clear()
#
# #print(numbers.count(9))
# print(len(numbers))

# nums = [3, 10, 9, "50", False]
#
# for el in nums:
#     el *= 2
#     print(el)

# n = int(input("Enter lenth: "))
# i = 0
# user_list = []
#
# while i < n:
#     string = "Enter element #" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1
#
# print(user_list)

# ФУНКЦИИ СТРОК.Индексы и срезы

# word = "Football,basketball,skate"
# # print(word.count('r'))
# # print(word.capitalize())
# # print(word.upper())
# # print(word[2])
# # print(len(word))
# # print(word.find('pr'))
# hobby = word.split(',')
# # print(hobby[1])
#
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
#
# result = ",".join(hobby)
# print(result)

# word = 'Football'
#
# # print(word[0:4])
# # print(word[4:6])
# # print(word[4:])
# print(word[1:-1:2])

# list = [1,15,'bug', True, 7.22]
#
# print(list[2:5:2])
# print(list[::-1])

# КОРТЕЖИ (TUPLE)
#  кортежи в отличии от списков нельзя изменять, удалять или добавлять элемнты

# data = (3,5,9,True, 7.33, "Hi!")
# print(data[2:5])
#
# print(data.count(50))
# print(len(data))

# data = (3,5,9,True, 7.33, "Hi!")
#
# for i in data:
#     print(i)

nums = [5,7,8]
new_data = tuple(nums)
print(new_data)



