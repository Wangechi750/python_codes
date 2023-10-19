def palindrome(word):
    word=word.replace(" ","").lower()
    word==word[::-1]
    return "the word is palindrome"
print (palindrome("mum"))
