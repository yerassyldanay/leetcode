import os
import math

const_unit = {
    "kg": {
        "unit": "g",
        "mul": 1000,
    },
    "g": {
        "unit": "g",
        "mul": 1,
    },
    "l": {
        "unit": "ml",
        "mul": 1000,
    },
    "ml": {
        "unit": "ml",
        "mul": 1,
    },
    "cnt": {
        "unit": "cnt",
        "mul": 1,
    },
    "tens": {
        "unit": "cnt",
        "mul": 10,
    },
}


class Solution:
    def __init__(self):
        self.ingredients = dict()
        self.foods = dict()
        self.catalog = dict()
        self.contains = dict()

    def __convert(self, volume: int, unit: str) -> int:
        return (volume * const_unit[unit]["mul"])

    def add_ingredient(self, ingred: str, volume: int, unit: str):
        # might already be in a dict
        if ingred not in self.ingredients:
            self.ingredients[ingred] = 0

        # add
        self.ingredients[ingred] += self.__convert(volume, unit)

    def add_food(self, food: str, number: int, ingredient: str, volume: int, unit: str):
        if food not in self.foods:
            self.foods[food] = {
                "number": number,
                "ingredient": {}
            }

        # add ingred one by one
        self.foods[food]["ingredient"][ingredient] = self.__convert(volume, unit)
        self.add_ingredient(ingredient, volume * number, unit)

    def add_catalog(self, ingredient: str, price: int, volume: int, unit: str):
        self.catalog[ingredient] = {
            "price": price,
            "volume": self.__convert(volume, unit)
        }

    def add_contains(self, name: str, volume: int, unit: str, *contains):
        # each for one unit
        volume = self.__convert(volume, unit)

        self.contains[name] = {
            "belok": float(contains[0] / volume),
            "zhir": contains[1] / volume,
            "uglevod": contains[2] / volume,
            "energy": contains[3] / volume,
        }

    def buy(self) -> (int, list, list):
        fcost = 0
        fbuy = dict()
        fenergy = dict()

        # each food & ingredients
        for food, ingredients in self.foods.items():
            num_friends = ingredients["number"]

            # ingredient & contains
            for ingredient, volume_needed in ingredients["ingredient"].items():

                # calculate energy
                if food not in fenergy:
                    fenergy[food] = [0.0] * 4

                # belok
                fenergy[food][0] += self.contains[ingredient]["belok"] * volume_needed
                # zhir
                fenergy[food][1] += self.contains[ingredient]["zhir"] * volume_needed
                # uglevod
                fenergy[food][2] += self.contains[ingredient]["uglevod"] * volume_needed
                # energy
                fenergy[food][3] += self.contains[ingredient]["energy"] * volume_needed

        renergy = []
        for food, arr in fenergy.items():
            renergy.append( [ [food] + arr ] )

        rbuy = []
        for ingredient, volume in self.ingredients.items():

            # might be
            # need 500 ml -> sold as 1000 ml

            price = self.catalog[ingredient]["price"]
            volume_unit = self.catalog[ingredient]["volume"]

            needed_units = math.ceil(volume / volume_unit)

            # egg 4
            # milk 2

            rbuy.append([ingredient, needed_units])
            fcost += needed_units * price

        return fcost, rbuy, renergy

def convert(line: str) -> list:
    line = line.strip()
    return line.split(" ")

if __name__ == '__main__':

    s = Solution()

    file = open("input.txt", "r")

    # cooking these foods
    num_foods = file.readline()
    for _ in range(int(num_foods)):
        elements = convert(file.readline())

        food = elements[0]
        num = elements[1]
        num_ingreds = elements[2]

        for _ in range(int(num_ingreds)):
            ingred_line = file.readline()
            ingred_elements = ingred_line.strip().split()

            s.add_food(food, int(num), ingred_elements[0], int(ingred_elements[1]), ingred_elements[2])

    # catalog
    for _ in range(int(file.readline())):
        elements = file.readline().strip().split()
        s.add_catalog(elements[0], int(elements[1]), int(elements[2]), elements[3])

    for _ in range(int(file.readline())):
        elements = file.readline().strip().split()
        # name v unit                                               belok zhir ugle energy
        s.add_contains(elements[0], int(elements[1]), elements[2], float(elements[3]), float(elements[4]), float(elements[5]), float(elements[6]))

    from pprint import pprint
    print("foods: ", s.foods)
    print("ingredients: ", s.ingredients)
    print("catalog: ", s.catalog)
    print("contains: ", s.contains)

    print()

    cost, buy, energy = s.buy()
    print(cost)

    for elem in buy:
        print(elem)

    for elem in energy:
        print(elem[0])

    file.close()

