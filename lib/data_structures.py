spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
     # Use a list comprehension to extract the 'name' value from each dictionary in the list
    return [food['name'] for food in spicy_foods]
print (get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
      # Use a list comprehension to filter out foods with a heat level greater than 5
    return [food for food in spicy_foods if food['heat_level'] > 5]
print (get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
     # Iterate over each dictionary in the list
    for food in spicy_foods:
         # Create a string of '🌶' emojis repeated 'heat_level' times
        heat_level_string = '🌶' * food['heat_level']
        print (f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_string}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #Iterate over each food dictionary in the list
    for food in spicy_foods:
        #Check if the food's cuisine matches the specified cuisine 
        if food['cuisine'] == cuisine:
            #Return the matching food dictionary
            return food
    return None #Return None if no matching spicy food is found
    
        

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_emoji = '🌶' * food['heat_level']
            print (f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_spicy_foods = len(spicy_foods)

    if num_spicy_foods == 0:
        return 0 # return 0 if the list is empty to avoid division by zero
    
    for food in spicy_foods:
        total_heat_level += food['heat_level']

    average_heat_level = total_heat_level / num_spicy_foods
    return int(average_heat_level)
average_heat = get_average_heat_level(spicy_foods)
print("Average Heat Level:", average_heat)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
spicy_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
updated_spicy_foods = create_spicy_food(spicy_foods, spicy_food)
print(updated_spicy_foods)
