# my_list = ["khinkali", "mtsvadi", "lobiani", "qababi", "khachapuri", "tskali"]
# prices = [2, 20, 15, 10, 15, 2]

# print(len(my_list))
# print(len(prices))

# i = 0

# while i <len(my_list):
#     print(my_list[i] + " ღირს" + " " + str(prices[i]) + " lari")
#     i +=1




# menu = []
# for i in range(5):
#     food = input("enter a food here: ")
#     if food.count("a") >=2:
#         menu.append(food)

# menu = ["qababi", "khachapuri","lobiani","nayini", "tskali", "salati"]

# new_menu = []

# for food in menu:
#     if food[1] != "a":
#         new_menu.append(food)
# print(new_menu)
# scores = [5, 100, 50, 30, 120, 40, 80]
# scores.sort()
# print(scores)

# students = ["tamuna", "luka", "aka", "gio", "levani", "ana"]
# students.sort()
# print(students)
# students.sort(reverse = True)
# print(students)

students = ["tamuna", "luka", "aka", "gio", "levani", "ana"]
new_list = []
i = len(students)
while i > 0:
    new_list.append(students[i-1])
    i -=1

print(new_list)
        