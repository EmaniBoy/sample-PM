from . import add, hello

def main():
    # tiny demo CLI behavior
    result = add(2, 3)
    print(hello("PM"))
    print("2 + 3 =", result)

if __name__ == "__main__":
    main()
