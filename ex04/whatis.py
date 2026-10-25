import sys

def main():
    if len(sys.argv) ==1:
        return
    if len(sys.argv) > 2:
        raise ValueError("Too many arguments")
    try:
        num = int(sys.argv[1])
    except(ValueError):
        raise ValueError("Argument is not an integer")

    if (num % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()