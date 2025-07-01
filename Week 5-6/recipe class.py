class Recipe:
    def __init__(self, recipe_id, name, ingredients, description):
        self.recipe_id = recipe_id
        self.name = name
        self.ingredients = ingredients
        self.description = description

    def display(self):
        print(f"Recipe ID: {self.recipe_id}")
        print(f"Name: {self.name}")
        print("Ingredients:", ", ".join(self.ingredients))
        print(f"Description: {self.description}")
        print("-" * 30)


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def display_all_recipes(self):
        if not self.recipes:
            print("No recipes in the recipe book.")
        for recipe in self.recipes:
            recipe.display()


# Program to take user input and use the classes
recipe_book = RecipeBook()

num = int(input("How many recipes do you want to add? "))

for i in range(num):
    print(f"\nEnter details for Recipe {i+1}:")
    recipe_id = int(input("Enter recipe ID: "))
    name = input("Enter recipe name: ")
    ingredients_input = input("Enter ingredients : ")
    ingredients = ingredients_input.split(",")  #
    for i in range(len(ingredients)):
        ingredients[i] = ingredients[i].strip()
    description = input("Enter description: ")

    # Create Recipe object
    recipe = Recipe(recipe_id, name, ingredients, description)

    # Add to RecipeBook
    recipe_book.add_recipe(recipe)

# Display all recipes
print("\nAll Recipes in the Recipe Book:\n")
recipe_book.display_all_recipes()
