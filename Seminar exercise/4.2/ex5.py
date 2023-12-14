def are_anagrams(word1, word2):

    word1 = ''.join(word1.split()).lower()
    word2 = ''.join(word2.split()).lower()

    # Проверка за анаграми
    return sorted(word1) == sorted(word2)

# Пример за използване
word1 = input("Въведете първата дума: ")
word2 = input("Въведете втората дума: ")

result = are_anagrams(word1, word2)

if result:
    print(f"{word1} и {word2} са анаграми.")
else:
    print(f"{word1} и {word2} не са анаграми.")
