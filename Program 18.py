# Write a Python Program to Print the Fibonacci sequence.
def palindrome(str):
    str1=str[::-1]
    if str==str1:
        print("Palindrome")
    else:
        print("Not a Palindrome")
palindrome(input("Enter the String "))