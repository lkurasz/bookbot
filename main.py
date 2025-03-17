from stats import count_words
from stats import characters_count
from stats import get_list_of_dictionaries
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_worlds = count_words(text)
    print(f"Found {num_worlds} total words")
    print("--------- Character Count -------")
    result = get_list_of_dictionaries(characters_count(text))
    for item in result:
        print(f'{item["name"]}: {item["num"]}')
    print("============= END ===============")

main()




