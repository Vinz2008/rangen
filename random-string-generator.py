import random
random_string = " "
table_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
number_of_character = int(input("How much character do you want for your random string")) 
number_for_index = 0
while number_for_index < number_of_character:
    print("bonjour")
    number_for_index = number_for_index + 1
#a
#random_index1 = random.randrange(len(table_characters))
#random_index2 = random.randrange(len(table_characters))
#random_index3 = random.randrange(len(table_characters))
#random_index4 = random.randrange(len(table_characters))
#random_index5 = random.randrange(len(table_characters))
#random_index6 = random.randrange(len(table_characters))
random_string = table_characters[random_index1]+table_characters[random_index2]+table_characters[random_index3]+table_characters[random_index4]+table_characters[random_index5]+table_characters[random_index6]
print(random_string)
