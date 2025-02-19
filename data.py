def string_repeat(number, string):
    return string * number

# Example usage:
result = string_repeat(2, "HawaiiPizza")
print(result)  # Output: HawaiiPizzaHawaiiPizza

def no_space(string):
    return string.replace(" ", "")

# Example usage:
result = no_space("Hawaii Pizza")
print(result)  # Output: HawaiiPizza

def number_to_string(number):
    return str(number)

# Example usage:
result = number_to_string(123)
print(result)  # Output: "123"

def boolean_to_string(boolean_value):
    return str(boolean_value)

# Example usage:
result = boolean_to_string(True)
print(result)  # Output: "True"

def abbrev_name(name):
    words = name.split()
    initials = [word[0].upper() for word in words]
    return '.'.join(initials)

# Example usage:
result = abbrev_name("Hawaii Pizza")
print(result)  # Output: H.P

def name_length(pizza_name):
    words = pizza_name.split()
    return [f"{word} {len(word)}" for word in words]

# Example usage:
result = name_length("hawaii pizza")
print(result)  # Output: ["hawaii 6", "pizza 5"]

def name_length(pizza_name):
    words = pizza_name.split()
    return list(map(lambda word: f"{word} {len(word)}", words))

# Example usage:
result = name_length("hawaii pizza")
print(result)  # Output: ["hawaii 6", "pizza 5"]

def remove_orders(orders):
    # Convert the string to a list of numbers
    order_list = orders.split(',')
    # Remove the first and last elements
    modified_list = order_list[1:-1]
    # Convert the list back to a string
    return ','.join(modified_list)

# Example usage:
result = remove_orders("1,2,3,4")
print(result)  # Output: "2,3"

def food_menu(food_items):
    return [f"{index + 1}. {item}" for index, item in enumerate(food_items)]

# Example usage:
result = food_menu(["Hawaii Pizza", "Diablo Pizza"])
print(result)  # Output: ["1. Hawaii Pizza", "2. Diablo Pizza"]
