"""This is a simple program that converts a string to Morse code."""
import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

def main():
    """Main function that converts a string to Morse code."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad.")
        
        test = sys.argv[1].upper()
        if not all(c.isalnum() or c.isspace() for c in test):
            raise AssertionError("the arguments are bad.")
        more_list =[]
        
        for char in test:
            if char not in NESTED_MORSE:
                raise AssertionError("the arguments are bad.")
            more_list.append(NESTED_MORSE[char])
        print(" ".join(more_list))
        
    except AssertionError as e:
        print(e)
        sys.exit(1)
        

if __name__ == "__main__":
    main()
