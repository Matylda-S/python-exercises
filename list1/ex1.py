# -*- coding: utf-8 -*-


def main():
    try:
        num = int(input("Enter number: "))
        if num%2==0:
            print("The number is even.")
        else:
            print("The number is odd.")
    except ValueError:
        print("The input is not an integer.")

if __name__ == "__main__":
    main()