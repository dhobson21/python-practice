# 11/19/19--------------------------------------------------------------------------------

"""Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""

# My Solution
def toJadenCase(string):
    words = string.split()
    finish = []
    for word in words:
        new = word.capitalize()
        finish.append(new)
    s = " "
    return s.join(finish)


"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""

# My Solution
def spin_words(sentence):
    words = sentence.split()
    final_words = []
    for word in words:
        if len(word) >  4:
#         Slice word and reverse if word is more than 4 characters long
            rev = word[::-1]
            final_words.append(rev)
        else:
            final_words.append(word)
    s = " "
    last = s.join(final_words)

    return last