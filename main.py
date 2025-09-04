import sys
from stats import (
    get_word_count, 
    get_char_count, 
    sort_on
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    get_word_count(file_path)
    print("--------- Character Count -------")
    char_count = get_char_count(file_path)
    sort_on(char_count)
    print("============= END ===============")
    
    # get_char_count("books/frankenstein.txt")

if __name__ == "__main__":
    main()