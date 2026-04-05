#Count vowels , consonants in a string
name = 'programming'
vowels=['a', 'e', 'i', 'o', 'u']
cons = 0
vowel = 0
for i in name:
    if i in vowels:
        vowel +=1
    else:
        cons +=1
print("Vowels: ", vowel)
print("Consonants: ", cons)