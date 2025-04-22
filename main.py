import sys
from stats import (
    get_num_words,
    get_char_dict,
    get_sorted_dict,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    char_sorted_list = get_sorted_dict(char_dict)
    print_report(book_path, num_words, char_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        char = item["character"]
        num = item["number"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")


main()
