from stats import get_num_words, get_char_count, sort_chars_count
import sys

def get_book_text(book_filepath):
    with open(book_filepath) as file:
        file_contents = file.read()
    return file_contents
    

def main(argv):
    if(len(argv) !=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = argv[1]

    book_contents = get_book_text(book_filepath)
    
    word_count = get_num_words(book_contents)
    

    char_dict = get_char_count(book_contents)
    char_count_list = sort_chars_count(char_dict)

    char = "char"
    num = "num"
    output_char_count_list = []
    for item in char_count_list:
        if item.get(char).isalpha():
            output_char_count_list.append(item)

    # Output

    # header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    
    # wordcount
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # character count
    print("--------- Character Count -------")
    for item in output_char_count_list:
        print(f"{item.get(char)}: {item.get(num)}")


main(sys.argv)