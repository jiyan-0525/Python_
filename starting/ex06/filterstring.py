import sys

from Starting.ex06.ft_filter import ft_filter

def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: python filterstring.py <string>")
            sys.exit(1)

        input_string = sys.argv[1]

        try:
            n = int(sys.argv[2])
        except (IndexError, ValueError):
            raise AssertionError("the argument are bad.")
        
        words = input_string.split()
        results = ft_filter(lambda word: len(word) > n, words)
        print(results)
        
    except AssertionError as e:
        print(e)
        sys.exit(1)
        
if __name__ == "__main__":
    main()