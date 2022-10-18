# სია შეატრიალეთ უკუღმა sort და reverse მეთოდის გარეშე. 
# შევქმნათ custom function:

def list_reverse(my_arr):
    new_list = []
    i = len(my_arr)
    while i > 0:
        new_list.append(my_arr[i-1])
        i -=1
    print(new_list)
    
list_reverse(["tamuna", "luka", "aka", "gio", "levani", "ana"])


#  დაასორტირეთ scores,გამომიტანეთ მაქსიმალური რიცხვი,
#  შევქმნათ custom function:
def max_num(scores):
    scores.sort()
    print(max(scores))

max_num([20, 23, 40, 15, 65, 10, 5])
