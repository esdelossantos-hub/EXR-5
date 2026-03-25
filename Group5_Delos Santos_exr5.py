print("Length of string:", len(text)) 

count = 0
for ch in text:
    count = count + 1
print("Number of characters:", count)

if len(text) > 0:
    first_char = text[0]
    rest = text[1:]
    replaced_text = first_char + rest.replace(first_char, '$')  
    print("String after replacement:", replaced_text)
else:
    print("No string to process.")

str_a = "Python"
str_b = "Coding"

new_str_a = str_b[:2] + str_a[2:]  
new_str_b = str_a[:2] + str_b[2:]  
print("After swapping first 2 chars:", new_str_a + " " + new_str_b)

v1 = "I"
v2 = "love"
v3 = "Python"
v4 = "programming"
sentence = v1 + " " + v2 + " " + v3 + " " + v4
print("Concatenated sentence:", sentence)

str1 = "Good"
str2 = "Morning"
print("Concatenated strings:", str1 + " " + str2)

name = "Nash"
age = "19"
print("Paragraph:", "My name is " + name + " and I am " + age + " years old.")
