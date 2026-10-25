import sys
def count_characters(text:str):
    """Counts upper, lower, punctuation, spaces, and digits in a given string."""
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if not char.isalnum() and not char.isspace())
    space_count = sum(1 for char in text if char.isspace())
    digit_count = sum(1 for char in text if char.isdigit())
    total_chars=len(text)
    
    print(f"The text contains {total_chars} characters:\n {upper_count} upper letters\n {lower_count} lower letters\n {punctuation_count} punctuation marks\n {space_count} spaces\n {digit_count} digits")
    
def main():
        if len(sys.argv) > 1:
            raise ValueError("Too many arguments")
        if len(sys.argv) == 1:
            try:
                text = input("What is the text to count?\n")
            except (KeyboardInterrupt, EOFError):
                return
        else:
            text = sys.argv[1]
        count_characters(text)

if __name__ == "__main__":
    main()
        