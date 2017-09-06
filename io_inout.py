def reverse(text):
    return text[::-1]
def is_palindrome(text):
    text = text.lower()
    #text = text.upper()
    forbidden = ('.', ',', ' ', '!', '?')

    for i in text:
        if i in forbidden:
            text = text.replace(i, '')

    print(text)
    return text == reverse(text)

something = input("Enter text: ")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")