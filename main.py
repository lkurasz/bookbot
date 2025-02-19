def count_words(value):
    words = value.split()
    return len(words)

def characters_count(value):
    dictionary = {}
    for character in value:
        char_lower = character.lower()
        if char_lower in dictionary.keys():
            value = dictionary[char_lower]
            value = value + 1
            dictionary[char_lower] = value
        else:
            dictionary[char_lower] = 1
    return dictionary

def report(words_cnt, char_dict):
    print("--- Begin report of books/frankestein.txt ---")
    print(f"{words_cnt} words found in the document")
    for char in char_dict.keys():
        print(f"The '{char}' character was found {char_dict[char]} times")
        pass
    print("--- End report ----")
    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words_cnt = count_words(file_contents)
    char_dict = characters_count(file_contents)
    
    report(words_cnt, char_dict)


main()




