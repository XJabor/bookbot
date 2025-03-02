import sys
from stats import word_counting, character_count, sort_on

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_test(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_path = sys.argv[1]
    text = get_book_test(book_path)
    num_words = word_counting(text)
    characters = character_count(text)
    sorted_characters = sort_on(characters)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for char_dict in sorted_characters:
        character = char_dict["char"]
        if character.isalpha():
            count = char_dict["count"]
            print (f"{character}: {count}")
    print ("============= END ===============")
main()