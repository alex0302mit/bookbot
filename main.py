from stats import count_words, count_letters, sort_character_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file: # opens the file and reads it
        return file.read() # returns the text of the file

def print_report(book_path, num_words, sorted_chars):
    """
    Prints a formatted report of the book analysis.
    
    Args:
        book_path (str): Path to the book file
        num_words (int): Total word count
        sorted_chars (list): Sorted list of character dictionaries
    """
    # Print header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Print character count section
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print alphabetic characters (skip spaces, punctuation, etc.)
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print footer
    print("============= END ===============")
def main():
    """
    Main function that reads and prints the contents of Frankenstein book.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Define the relative path to the Frankenstein text file
    book_path = sys.argv[1]
    
    # Get the book text using our function
    book_text = get_book_text(book_path)
    
    # Count the words in the book
    num_words = count_words(book_text)
    # Count the letters in the book
    char_counts = count_letters(book_text)
    # Sort the character counts from greatest to least
    sorted_char_counts = sort_character_counts(char_counts)
    
    # Print the formatted report
    print_report(book_path, num_words, sorted_char_counts)
# Call the main function when the script is run
if __name__ == "__main__":
    main()