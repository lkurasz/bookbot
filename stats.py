def count_words(text):
    words = text.split()
    return len(words)

def characters_count(text):
    dictionary = {}
    for character in text:
        char_lower = character.lower()
        if char_lower in dictionary.keys():
            text = dictionary[char_lower]
            text = text + 1
            dictionary[char_lower] = text
        else:
            dictionary[char_lower] = 1
    return dictionary

def sort_on(dictionary):
    return dictionary["num"]

def get_list_of_dictionaries(dictionary):
    #Utworzenie listy z slownikami
    list_of_dict = []
    for key in dictionary.keys():
        if key.isalpha():
            list_of_dict.append({"name" : key, "num": dictionary[key]})
    
    list_of_dict.sort(reverse=True, key=sort_on)   
    return list_of_dict