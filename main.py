"""
Notepad v1.0
By Patrick Bruso

This is a program that is coded from scratch using various
resources to create a notepad program for opening text files,
reading text files, and writing to text files.
"""


def main():
    new_text()


def new_text():
    user_text = input("Text: ")
    print(user_text)


def open_text():
    open = input("Open file (Y/N)? ")
    if open.lower == "y":
        print("cool")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
