sentence='Python is fun and Python is easy to learn'
vowels='aeiou'
mod_sen=""

for char in sentence:
    if char.lower()in vowels:
        mod_sen += char.upper()
    else:
        mod_sen += char
print(mod_sen)
    

