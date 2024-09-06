"""
Write Python Program to check whether an alphabet is a vowel or consonant
"""

letter = input("Enter a letter: ")

if(letter.lower()=="a" or letter.lower()=="e" or letter.lower()=="i" or letter.lower()=="o" or letter.lower()=="v"):
    
    print("vowel")
else:
    print("consonant")