word = (input("Input a word: ")).lower()
vowels = "aeiou"

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

print(f'There are {count_vowels(word)} vowels in: "{word}"')
