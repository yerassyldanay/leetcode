
"""

1. Save in the database all needed ingredients


2. Save all products I have


3. Save calories

"""

def convert_to_the_same_unit(amount: int, unit: str):
    if unit == "kg":
        amount = amount * 1000
        unit = "g"
    elif unit == "l":
        amount = amount * 1000
        unit = "ml"
    elif unit == "tens":
        amount = amount * 10
        unit = "cnt"

    return amount, unit


if __name__ == '__main__':
    # import time
    # import pprint as p
    # no. food

    number = int(input())
    food_dict = {

    }
    calories_abc = "calories_abc"
    for num in range(number):
        # sandwich 7 3
        sandwitch = input()
        sandwitch = sandwitch.split(" ")
        # print("sandwitch: ", sandwitch)
        food, friends_count, ingred_count = sandwitch[0], int(sandwitch[1]), int(sandwitch[2])

        food_dict[sandwitch[0]] = {
            "calories_abc": [0.0, 0.0, 0.0, 0.0]
        }

        # getting ingredients
        # butter 10 g
        for ingr in range(ingred_count):
            butter = input()
            butter = butter.split(" ")
            ingred_input = butter[0]
            ingred_count, ingred_unit = convert_to_the_same_unit(int(butter[1]), butter[2])

            food_dict[sandwitch[0]][butter[0]] = (ingred_count * friends_count, ingred_count)

        # print("food_dict: ", food_dict)
    product_dict = {

    }

    return_product_count = {

    }
    return_price = 0

    number = int(input())
    for num in range(number):
        sandwitch = input()
        sandwitch = sandwitch.split(" ")
        # egg 61 1 tens
        # (price, amount, unit)
        temp_amount = convert_to_the_same_unit(int(sandwitch[2]), sandwitch[3])
        product_dict[sandwitch[0]] = (int(sandwitch[1]), temp_amount[0])

    product_dict_2 = {

    }
    number = int(input())
    for num in range(number):
        egg = input()
        egg = egg.split(" ")
        temp = convert_to_the_same_unit(int(egg[1]), egg[2])
        product_dict_2[egg[0]] = (temp[0], float(egg[3]), float(egg[4]), float(egg[5]), float(egg[6]))
    #
    # p.pprint(food_dict)
    # p.pprint(product_dict)
    # p.pprint(product_dict_2)
    # print("___________________________________________________________")
    # print()
    # count the number of ingredients
    for sandwitch, butter in food_dict.items():
        for butter_str, butter_count in butter.items():
            if butter_str == calories_abc:
                continue

            # print(">>> ", sandwitch, butter_str, butter_count)
            # 'butter': temp_amount = (70, 'g')
            temp_amount = product_dict[butter_str]
            temp_amount_2 = product_dict_2[butter_str]

            # print(">>>>> temp_amount_2: ", temp_amount_2)

            count = butter_count[0] / temp_amount[1]
            count2 = round(count)

            if count2 < count:
                count2 = count2 + 1

            if butter_str not in return_product_count:
                return_product_count[butter_str] = count2
            else:
                return_product_count[butter_str] = return_product_count[butter_str] + count2

            # add price
            return_price = return_price + temp_amount[0] * count2

            count = butter_count[1] / temp_amount_2[0]
            temp = food_dict[sandwitch][calories_abc]
            # print("-----------------------------------------")
            # print(sandwitch, butter_str, butter_count)
            # print(butter_count[1], temp_amount_2[0], count)
            # print(temp_amount_2)
            # print("temp: ", temp)

            temp[0] = temp[0] + count * temp_amount_2[1]
            temp[1] = temp[1] + count * temp_amount_2[2]
            temp[2] = temp[2] + count * temp_amount_2[3]
            temp[3] = temp[3] + count * temp_amount_2[4]

            food_dict[sandwitch][calories_abc] = temp

    print(return_price)
    for key, value in return_product_count.items():
        print(key, value )
    for key, value in food_dict.items():
        print(key, end=" ")
        for each in food_dict[key][calories_abc]:
            print(each, end=" ")
        print()
