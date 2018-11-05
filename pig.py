print("     Welcome to the Pig Latin Translator!   ")
pyg = "ay"
# the code starts here.
original = input("Enter a word: ")
if len(original) > 0 and original.isalpha() == True:
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]


     print(original)
elif original.isalpha()==False:
    print("Make sure you don't include numbers in your Input...please try again")
else:
    print("You have not entered anything!")
