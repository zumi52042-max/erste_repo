# Time converter: Convert hours to seconds

# TODO: Get the number of hours from user input
number_of_hours = input("Hours: ")
int_hours = int(number_of_hours) 
# Hint: Use input() function with the prompt "Hours: "
# Remember to convert the input string to an integer

# TODO: Calculate seconds
seconds = 3600
def calculate_seconds() : 
    convert_seconds = seconds*int_hours
    return convert_seconds
# Hint: 1 hour = 60 minutes = 3600 seconds

# TODO: Print the result
print(f"Seconds: {calculate_seconds()}")
# The output should be in the format "Seconds: <value>"


"""# Time converter: Convert hours to seconds

# Get the number of hours from user input
hours = int(input("Hours: "))

# Calculate seconds (1 hour = 3600 seconds)
seconds = hours * 3600

# Print the result
print(f"Seconds: {seconds}")"""

