# have user import there name
# will capitilize the first letters of name
user_name_import = input('Please enter your full name: ').title()
print(user_name_import)

# prints out username in all uppercase
results_upper_username = user_name_import.upper()
print(results_upper_username)

# prints out username in all lowercase
results_lower_username = user_name_import.lower()
print(results_lower_username)

# total number of characters (excluding spaces)
total_chars_username = len(user_name_import.replace(" ",""))
print(total_chars_username)

# reverse the name
reverse_username = user_name_import[::-1]
print(reverse_username)


