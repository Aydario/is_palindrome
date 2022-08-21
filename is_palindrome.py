"""This program checks whether the entered text is a palindrome.
When the condition is met, the function prints: “This is a palindrome”,
and if not executed: “This is not a palindrome.\""""


def palindrome(text):
    text = text.lower()
    text = ''.join(text[i] for i in range(len(text)) if ord(text[i]) not in range(0, 48) and ord(text[i]) not in
                   range(58, 97) and ord(text[i]) not in range(123, 128))
    if text[0:] == text[::-1]:
        print('It is a palindrome.')
    else:
        print('It is not a palindrome.')


def main():
    palindrome(input('Enter the text and press "Enter": '))


if __name__ == '__main__':
    main()
