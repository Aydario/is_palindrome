"""This program checks whether the entered text is a palindrome.
When the condition is met, the function prints: “This is a palindrome”,
and if not executed: “This is not a palindrome.\""""


def check_for_palindrome(text):
    # Converting the entered text to lowercase.
    text = text.lower()
    # Exclusion of all characters except numbers and Latin letters in lower case.
    text = ''.join(text[i] for i in range(len(text)) if ord(text[i]) not in range(0, 48) and ord(text[i]) not in
                   range(58, 97) and ord(text[i]) not in range(123, 128))
    # Checking.
    if text[0:] == text[::-1]:
        print('It is a palindrome.')
    else:
        print('It is not a palindrome.')


def main():
    start = input('Press "1" and "Enter" to start: ')
    while start != '1':
        print('To start checking, you need to click on "1"')
        start = input('Press "1" and "Enter" to start: ')
    while start == '1':
        check_for_palindrome(input('Enter the text and press "Enter": '))
        print('*' * 75)
        start = input('Press:\n* "1" and "Enter" - check again;\n* "any key" and "Enter" to finish: ')
        if start != '1':
            print('The End.')



if __name__ == '__main__':
    main()
