def main():
    import random
    random_string = " "
    table_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    number_of_character = int(input("How much character do you want for your random string ? : ")) 
    number_for_index = 0
    table_result =[]
    while number_for_index < number_of_character:
        random_index1 = random.randrange(1,26) - 1
        random_index2 = table_characters[random_index1]
        table_result.append(random_index2)
        number_for_index = number_for_index + 1

    number_of_character_loop = 1
    random_string = table_result[0]
    while number_of_character_loop < number_of_character:
        random_string = random_string + table_result[number_of_character_loop]
        number_of_character_loop = number_of_character_loop + 1 
    print(random_string)
