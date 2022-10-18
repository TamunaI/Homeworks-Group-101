# my_sentence = "aa {0} bb {1} cc {2}".format("zz", "yy", "xx")
# print(my_sentence)


# მომხმარებელს ტერმინალიდან შემოატანინეთ ორი რიცხვი, თუ მათი ნამრავლი > 100, დაპრინტეთ "xxx", 
# თუ არა და დაპრინტეთ "yyy".
# a = int(input("enter a here: "))
# b = int(input("enter b here: "))

# product = a * b

# if product > 100:
#     print("xxx")
# else:
#     print("yyy")


# მომხმარებელს ტერმინალიდან შემოატანინეთ სამი რიცხვი, დაპრინტეთ კენტი რიცხვების ჯამი:
# a = int(input("enter a here: "))
# b = int(input("enter b here: "))
# c = int(input("enter c here: "))

# sum = 0

# if a % 2 == 1:
#     sum += a
# if b % 2 == 1:
#     sum += b
# if c % 2 == 1:
#     sum += c
# else:
#     print("x")

# print("the sum of odd numbers is {} ".format(sum))



# my_name ="Darejani"

# for char in my_name:
#     print(char)

# for i in range(10):
#     print(i)

# for i in range(10):
#     print(str(i) + "ა")

# for i in range(3,10,2 ):   3-დან 10-მდე ყოველი მე-2 (start,finish,step)
#     print("Tamuna")

# ამ შემთხვევებში char და i არის საიტერაციო ცვლადები



# მომხმარებელს ტერმინალიდან შემოატანინეთ ორი სახელი და ის დაპრინტეთ რომელშიც მეტი ხმოვანია:
# name_1 = input("enter name1 here: ")
# name_2 = input("enter name2 here: ")

# vowels_in_name_1 = 0
# vowels_in_name_2 = 0

# for char in name_1:
#     if char in "aeiou":
#         vowels_in_name_1 += 1

# for char in name_2:
#     if char in "aeiou":
#         vowels_in_name_2 += 1

# if vowels_in_name_1 > vowels_in_name_2:
#     print(" more vowels in name_1 and it contains {} vowels".format(vowels_in_name_1))
# elif vowels_in_name_2 > vowels_in_name_1:
#     print(" more vowels in name_2 and it contains {} vowels".format(vowels_in_name_2))
# else:
#     print("they have equal number of vowels")



# name1 ="Darejani"
# name2 = "Luka"

# if name1 == "Darejani":
#     print("Darejani is incomparable")
# else:
#     if len(name1)> len(name2):
#         print("The first one is longer")
#     elif len(name2)> len(name1):
#         print("The second one is longer")
#     else:
#         print("They are even")


# მომხმარებელს ტერმინალიდან შემოატანინეთ ორი სახელი და ის დაპრინტეთ რომელშიც მეტი თანხმოვანია:
# name1 = input("enter name1 here: ")
# name2 = input("enter name2 here: ")

# consonants_in_name1 = 0
# consonants_in_name2 = 0

# for char in name1:
#     if char not in "aeiou":
#         consonants_in_name1 +=1
       
# for char in name2:
#     if char not in "aeiou":
#         consonants_in_name2 +=1

# if consonants_in_name1>consonants_in_name2:
#     print("The number of consonants in name1 is more and it equals {} consonants".format(consonants_in_name1))
# elif consonants_in_name1<consonants_in_name2:
#     print("The number of consonants in name2 is more and it equals {} consonants".format(consonants_in_name2))
# else:
#     print("They have equal number of consonants")


# while loop:
# i = 0
# while i<5:
#     print("tamuna")
#     print(i)
#     i +=1 

# full_name = "Tamuna Iosava"
# i = 0
# while i < len(full_name):
#     print(full_name[i])
#     i +=1


# a = "qwerty"
# b = "asdfgh"

# i =0
# while i < len(a):
#     print(a[i]+b[i])
#     i +=1


# if 10>5 and 3<7:       and-ის შემთხვევაში ორივე მხარე უნდა იყოს სწორი
#     print("cool") 

# if 10>5 or 3>5:        or-ის შემთხვევაში ერთ-ერთი მხარე უნდა იყოს სწორი
#     print("true")
     
# i = 0

# while i < 10:
#     print(str(i)+" Tamuna")
#     if i ==5:
#         break
#     i +=1


# ინფუთით შეიტანეთ სახელი და გვარი და ინდექსით გამოიტანეთ რომელ ადგილას არის ხმოვნები:
# name = input("enter name here: ")

# i = 0

# while i < len(name):
#     if name[i] in "aeiou":
#         print(name[i] + " - " + str(i))
#     i +=1

# x =0
# for i in range(5):
#     for j in range(4):
#         print(str(x) + " tamuna")
#         x +=1                       for i და for j range-ის ნამრავლი გვექნება შედეგად output-ში.


# total = 0
# for i in range(5):
#     age_of_user = int(input("enter users ages here: "))
#     if age_of_user >3:
#         total +=100
# print(total)

# იგივე ამოცანა while loop-ით:

# total = 0
# i = 0
# while i <5:
#     age_of_user = int(input("enter users ages here: "))
#     if age_of_user>3:
#         total +=100
#     i +=1
# print(total)



# my_list = ["khinkali", "mtsvadi", "lobiani", "khachapuri","wyali"]
# for food in my_list:
#     print(food)
# prices = [2, 10, 5, 20, 7]
# weird_list = ["tamuna","tamuna1", [1, 2, 3], "tamuna4", "tamuna5"]
# print(weird_list[2][2])


# my_list = ["khinkali", "mtsvadi", "lobiani", "khachapuri","wyali"]
# prices = [2, 10, 5, 20, 7]

# i =0
# while i < len(my_list):
#     print(my_list[i] + " ღირს " + str(prices[i]) + " ლარი")
#     i +=1

# my_arr = ["banana", 1, "True", [1,2,3], "tamuna", "tamuna1"]
# print(my_arr[1:6:2])
# print(my_arr[:5])
# print(my_arr[-1])

# menu = ["khinkali", "mtsvadi", "lobiani", "khachapuri","wyali"]

# if "lobiani" in menu:
#     print("lobiani gvaqvs")

# menu[1] = "BBQ"   
# print(menu)
# menu[2:4] = ["aa","bb","cc"]
# print(menu)


# my_name = "Tamuna"

# new_name = ""

# for i in range(len(my_name)):
#     if i ==2 or i ==3:
#         new_name += "x"
#     else:
#         new_name += my_name[i]
# print(new_name)



# menu = ["khinkali", "mtsvadi", "lobiani", "khachapuri","wyali"]
# menu.insert(3, "nayini")    ჩასვამს კონკრეტულ ადგილზე - insert
# print(menu)

# menu.append("cecxli")     დაამატებს ბოლოში - append
# print(menu)


# menu = []
# menu.append("pizza")
# print(menu)


# მომხმარებელს შემოატანინეთ 5 საჭმელი, 
# სიაში შეიტანეთ ისინი, რომლებიც შეიცავენ მინიმუმ 2 "ა"-ს.

# menu = []

# i = 0

# while i<5:
#     foods = input("enter foods here: ")
#     if foods.count("a") >=2:
#         menu.append(foods)
#     i +=1

# print(menu)


# menu = ["khinkali", "mtsvadi", "lobiani", "khachapuri","wyali"]
# menu.remove("wyali")
# print(menu)


# მენიუდან წაშალეთ ის ელემენტები, რომლებშიც მეორე ასო არის ა.
# menu = ["khinkali", "banana", "mtsvadi", "lobiani", "khachapuri","wyali"]
# new_menu = []
# for food in menu:
#     if food[1] != "a":
#         new_menu.append(food) ამ ყველაფერს ვერ ვიზამთ remove() მეთოდით. ციკლი და remove ერთად არ მუშაობს.

# print(new_menu)


# scores = [20, 23, 40, 15, 65, 10, 5]
# print(max(scores))
# ან მეორენაირად
# scores = [20, 23, 40, 15, 65, 10, 5]
# scores.sort()
# print(scores[-1])

# დაასორტირეთ scores, sort() მეთოდის და max ფუნქციიხ გამოყენების
# გარეშე დამიბრუნეთ ყველაზე დიდი რიცხვი.

# scores = [20, 23, 40, 15, 65, 10, 5]
# print(max(scores)) 1-ლი მეთოდით

# scores.sort()      მე-2 მეთოდით
# print(scores[-1])

# მე-3 მეთოდით, for loop-ით.
# max_num = scores[0]

# for score in scores:
#     if score > max_num:
#         max_num = score
# print(max_num)

# მე-4 მეთოდით, while loop-ით.
# max_num = scores[0]
# i = 0
# while i < len(scores):
#     if scores[i] > max_num:
#         max_num = scores[i]
#     i +=1
# print(max_num)


# სია შეატრიალეთ უკუღმა sort და reverse მეთოდის გარეშე. 
# students = ["tamuna", "luka", "aka", "gio", "levani", "ana"]

# new_list = []
# i = len(students)
# while i > 0:
#     new_list.append(students[i-1])
#     i -=1
# print(new_list)      


# name = "tamuna"
# scores = [20, 23, 40, 15, 65, 10]

# print(len(name))
# print(len(scores))

# i = 0
# while i < len(name):
#     print(name[i] + " - " + str(scores[i]))
#     i +=1

# ფუნქციონალური პროგრამირება - functional programming

# def wish_a_good_day(name, day):
#     print(name + " karg dghes gisurveb " + str(day) + "oqtombers")

# wish_a_good_day("tamo", 16)
# wish_a_good_day("luka",16)

# names = ["tamo","gio", "luka", "aka"]
# for name in names:
#     wish_a_good_day(name, 16)

# შექმენით ფუნქცია, დაარქვით შეკრება - addition, არგუმენტად ჩაუწერეთ 
# ორი რიცხვი და პრინტავდეს მათ ჯამს.
# def addition(num1, num2):
#     print(num1 + num2)

# addition(5,8)


# def calculate_max(scores):
#     max_num = scores[0]
#     for score in scores:
#         if score > max_num:
#             max_num = score
#     print(max_num)

# scores = [5, 10,100,95,50,42,57,]
# calculate_max(scores) 
# calculate_max([20, 23, 40, 15])
# calculate_max([40, 15, 65, 10])

# def pair_sum(arr1,arr2):
#     for i in range(len(arr1)):
#         print(arr1[i] + arr2[i])

# pair_sum([2,4,10,17], [30,35,10,12])





