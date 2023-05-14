def find_anagrams(file_path):
    anagrams = {}

    with open(file_path, 'r') as file:
        for word in file:
            word =word.strip()
            sorted_word = ''.join(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

    anagram_pairs = [words for words in anagrams.value() if len(words) > 1]

    return anagram_pairs