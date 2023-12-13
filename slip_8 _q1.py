#slip 8 q1 
def count_upper_lower(input_str):
    upper_count = sum(1 for char in input_str if char.isupper())
    lower_count = sum(1 for char in input_str if char.islower())

    print("Number of uppercase alphabets:", upper_count)
    print("Number of lowercase alphabets:", lower_count)

# Take user input
user_input = input("Enter a string: ")

# Call the function to count upper and lower case alphabets
count_upper_lower(user_input)
