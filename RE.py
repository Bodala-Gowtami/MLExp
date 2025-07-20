# Original input
input_text = "Barack Obama is a prime minister of USA in the year of 2015."

# Convert to lowercase
lowercase = input_text.lower()
print(lowercase)
print("LOWERCASE = ", lowercase)

# Import regex module
import re

# REGULAR EXP1: Replace "2015" with "2025"
lowercase_re = re.sub('2015', '2025', lowercase)
print("REGULAR EXP1 = ", lowercase_re)

# REGULAR EXP2: Replace all lowercase letters from a to i with '*'
lowercase_re = re.sub('[a-i]', '*', lowercase)
print("REGULAR EXP2 = ", lowercase_re)

# REGULAR EXP3: Replace all digits with '-'
lowercase_re = re.sub(r'\d', '-', lowercase)
print("REGULAR EXP3 = ", lowercase_re)
