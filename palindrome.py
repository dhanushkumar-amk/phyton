
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
    
string_to_check = input("Enter a string: ")
if is_palindrome(string_to_check):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")