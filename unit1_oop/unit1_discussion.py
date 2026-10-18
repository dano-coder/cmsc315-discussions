

"""
CMSC 315 - Unit 1 Discussion
What's for Dinner? Recipe Manager

This program demonstrates object-oriented programming in Python
using a simple recipe management system.

The program includes:
1. A parent Recipe class and a child DinnerRecipe class.
2. Inheritance and method overriding.
3. Class and instance namespaces.
4. Shallow and deep copying of nested lists.
5. A main function that tests the program.
6. Additional features for checking groceries and
   preventing duplicate ingredients.

The project was inspired by restaurant recipe and inventory
management systems (something i would love to be able to manage better in home). It provides a starting point for a
larger program that could eventually track food inventory,
ingredient quantities, and recipe costs.

Would love an eventual app with my recipes and personal shopping needs
maybe eventually with recipe amount per person
"""

from copy import copy, deepcopy


# TODO 1: Create a parent class with basic recipe information.
class Recipe:
    category = "Home Cooking"

    def __init__(self, name, cooking_time):
        self.name = name
        self.cooking_time = cooking_time

    def display_info(self):
        print("Meal:", self.name)
        print("Cooking Time:", self.cooking_time, "minutes")


# TODO 2: Create a child class that inherits from Recipe.
class DinnerRecipe(Recipe):
    meal_type = "Dinner"

    def __init__(self, name, cooking_time, servings, difficulty):
        super().__init__(name, cooking_time)
        self.servings = servings
        self.difficulty = difficulty
        self.ingredients = []


    # Add an ingredient and the amount needed.
    def add_ingredient(self, name, amount):

        # Check whether the ingredient is already in the recipe.
        for ingredient in self.ingredients:
            if ingredient[0].lower() == name.lower():
                print(name, "is already in this recipe.")
                return

        # Add the ingredient if it is not already listed.
        self.ingredients.append([name, amount])


    # Override the parent method to show more information.
    def display_info(self):
        super().display_info()
        print("Servings:", self.servings)
        print("Difficulty:", self.difficulty)
        print("Ingredients:")

        for ingredient in self.ingredients:
            print("-", ingredient[1], ingredient[0])

    # TODO 6: My added feature checks what groceries I need.
    def grocery_check(self, pantry):
        print("\nGrocery List for", self.name)

        missing = []

        # Make pantry names lowercase so capitalization does not matter.
        pantry_items = [item.lower() for item in pantry]


        for ingredient in self.ingredients:
            if ingredient[0].lower() not in pantry_items:
                missing.append(ingredient[0])

        if len(missing) == 0:
            print("You have everything needed!")
        else:
            for item in missing:
                print("Need to buy:", item)


# TODO 3: Show how class and instance namespaces work.
def demonstrate_namespaces():
    print("\n=== Namespaces ===")

    # Create two different dinner recipes.
    first = DinnerRecipe("Chicken Curry", 40, 4, "Easy")
    second = DinnerRecipe("Tacos", 25, 2, "Easy")

    # Access the class variable in two ways.
    print("Through class:", DinnerRecipe.meal_type)
    print("Through object:", first.meal_type)

    # Add a favorite attribute to only one recipe.
    first.favorite = True

    # Show what is stored in each object and the class.
    print("First recipe:", first.__dict__)
    print("Second recipe:", second.__dict__)
    print("Class namespace:", DinnerRecipe.__dict__)


# TODO 4: Demonstrate shallow and deep copying.
def demonstrate_copying():
    print("\n=== Shallow and Deep Copying ===")

    # Create a list containing smaller ingredient lists.
    original = [
        ["Chicken", "1 pound"],
        ["Rice", "2 cups"]
    ]

    # Make a shallow copy and a deep copy.
    shallow = copy(original)
    deep = deepcopy(original)

    # Change the amount of chicken in the original list.
    original[0][1] = "2 pounds"

    # Compare the original list and the two copies.
    print("Original:", original)
    print("Shallow Copy:", shallow)
    print("Deep Copy:", deep)

    # The shallow copy changed because it shares the inner lists.
    # The deep copy stayed the same because it has separate lists.


# TODO 5: Create recipes and test all the methods.
def main():
    print("=== What's for Dinner? Recipe Manager ===")

    # Test the parent class.
    basic = Recipe("White Rice", 20)
    basic.display_info()

    print()

    # Create a chicken curry dinner.
    curry = DinnerRecipe("Chicken Curry", 40, 4, "Easy")


    # Add ingredients to the curry.
    curry.add_ingredient("Chicken", "1 pound")
    curry.add_ingredient("chicken", "2 pounds")  # Test duplicate
    curry.add_ingredient("Rice", "2 cups")
    curry.add_ingredient("Curry Roux", "1 package")
    curry.add_ingredient("Onion", "1")


    # Display the curry information.
    curry.display_info()

    # These are the ingredients I already have at home.
    pantry = ["chicken", "rice", "onion"]

    # Check which ingredients I still need to buy.
    curry.grocery_check(pantry)

    print()

    # Create another dinner recipe.
    tacos = DinnerRecipe("Tacos", 25, 2, "Easy")

    tacos.add_ingredient("Tortillas", "4")
    tacos.add_ingredient("Beef", "1 pound")
    tacos.add_ingredient("Cheese", "1 cup")

    # Display the tacos information.
    tacos.display_info()

    # Check which taco ingredients I need.
    tacos.grocery_check(pantry)

    # Run the namespace demonstration.
    demonstrate_namespaces()

    # Run the copying demonstration.
    demonstrate_copying()


# Run the program.
if __name__ == "__main__":
    main()
