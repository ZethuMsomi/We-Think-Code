vowels = "aeiouAEIOU"
string = input("input a string: ")
result = " "

for char in string:
    if char not in vowels:
        result += char
print(result)
