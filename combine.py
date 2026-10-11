vowels = ["a", "e", "i", "o", "u"]

def start(text):
    print("-" * len(text))
    print(text)
    print("-" * len(text))

def combine():
    name_1 = input("Write one of your names here: ").title()
    last_vowel_found = None
    """
    Enumerate assigns each letter in the string an index number + letter value
    E.g. 0, H
         1, e
         2, l
         3, l
         4, o
    """
    for index, letter in enumerate(name_1):
        if letter in vowels:
            last_vowel_found = index
        # for each index and letter enumerate gives, if the letter is in vowels[], last_vowel_found = current index of string
    if last_vowel_found is not None:
        name_1 = name_1[0 : last_vowel_found + 1]
        # after the string is scanned through, the name is cropped from index 0 to and including the vowel index
    
    name_2 = input("Write your other name here: ").lower()
    first_vowel_found = None
    for index, letter in enumerate(name_2):
        if letter in vowels:
            first_vowel_found = index
            break
    if first_vowel_found is not None:
        name_2 = name_2[first_vowel_found +1 : len(name_2)]
    print(name_1 + name_2)
start("Welcome to the name combiner!")
combine()
