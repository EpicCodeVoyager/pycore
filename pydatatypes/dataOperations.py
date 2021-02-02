"""
dir(variable)
help(variable)
help(variable.attribute)

Operations on string
"""

'''
Chapter : String 

capitalize()   Converts the first character to upper case
casefold()     Converts string into lower case
center()       Returns a centered string
count()        Returns the number of times a specified value occurs in a string
encode()       Returns an encoded version of the string
endswith()     Returns true if the string ends with the specified value
expandtabs()   Sets the tab size of the string
find()         Searches the string for a specified value and returns the position of where it was found
format()       Formats specified values in a string
format_map()   Formats specified values in a string
index()        Searches the string for a specified value and returns the position of where it was found
isalnum()      Returns True if all characters in the string are alphanumeric
isalpha()      Returns True if all characters in the string are in the alphabet
isdecimal()    Returns True if all characters in the string are decimals
isdigit()      Returns True if all characters in the string are digits
isidentifier() Returns True if the string is an identifier
islower()      Returns True if all characters in the string are lower case
isnumeric()    Returns True if all characters in the string are numeric/ includes all languages.
isprintable()  Returns True if all characters in the string are printable
isspace()      Returns True if all characters in the string are whitespaces
istitle()      Returns True if the string follows the rules of a title
isupper()      Returns True if all characters in the string are upper case
join()         Joins the elements of an iterable to the end of the string
ljust()        Returns a left justified version of the string
lower()        Converts a string into lower case
lstrip()       Returns a left trim version of the string
maketrans()    Returns a translation table to be used in translations
partition()    Returns a tuple where the string is parted into three parts
replace()      Returns a string where a specified value is replaced with a specified value
rfind()        Searches the string for a specified value and returns the last position of where it was found
rindex()       Searches the string for a specified value and returns the last position of where it was found
rjust()        (width, fillchar=' ', /) Return a right-justified string of length width.
rpartition()   Returns a tuple where the string is parted into three parts
rsplit()       Splits the string at the specified separator, and returns a list
rstrip()       Returns a right trim version of the string
split()        Splits the string at the specified separator, and returns a list
splitlines()   Splits the string at line breaks and returns a list
startswith()   Returns true if the string starts with the specified value
strip()        Returns a trimmed version of the string
swapcase()     Swaps cases, lower case becomes upper case and vice versa
title()        Converts the first character of each word to upper case
translate()    Returns a translated string
upper()        Converts a string into upper case
zfill()        Fills the string with a specified number of 0 values at the beginning
                         

'''
sentence = "the art is a lie which brings you close to truth. art has become essential to appreciate life. art " \
           "is art. "
print(f"Orignal : {sentence}")
print(f"upper() : {sentence.upper()}")
print(f"lower() : {sentence.lower()}")
print(f"capitalize() : {sentence.capitalize()}")
print("rsplit(\"art\") : {}".format(sentence.rsplit("art")))
print("split(\"art\") : {}".format(sentence.split("art")))
print("rpartition(\"art\") : {}".format(sentence.rpartition("art")))
print("partition(\"art\") : {}".format(sentence.partition("art")))
print("count(\"art\") : {}".format(sentence.count("art")))
print("find(\"art\") : {}".format(sentence.find("art")))
print("rfind(\"art\") : {}".format(sentence.rfind("art")))
print("rindex(\"art\") : {}".format(sentence.rindex("art")))
print("index(\"art\") : {}".format(sentence.index("art")))


# Find all occurence of art and replace it with comedy without using replace method.

def find_all_words_indexes(sentance, word, start=0):
    f_index = sentance.find(word, start)
    if f_index != -1:
        yield from find_all_words_indexes(sentance, word, f_index + 1)
    if f_index != -1:
        yield f_index


def custom_replace(sentence, to_be_replaced, replacement):
    art_indexes = find_all_words_indexes(sentence, to_be_replaced)
    for index in art_indexes:
        #              <left_portion>   + <replacement> + <right_portion>
        new_sentence = sentence[:index] + replacement + sentence[index + len(to_be_replaced):]
        sentence = new_sentence
    return sentence


# Basically implement replace feature.
n_sentence = custom_replace(sentence, "art", "comedy")
print("custom_replace(sentence, \"art\", \"comedy\") : {}".format(n_sentence))


def make_uppercase_by_index(sentence, index):
    char_to_be_replaced = sentence[index]
    replacement = char_to_be_replaced.upper()
    return sentence[:index] + replacement + sentence[index + 1:]

upper_by_index = make_uppercase_by_index(sentence, 4)
print("make_uppercase_by_index(sentence, 4) : {}".format(upper_by_index))

sentence_2 = "1211"
sentence_3 = "123.11"


def custom_is_float(sentence):
    return sentence.replace(".", "", 1).isnumeric()


print("\"1211\".isnumeric() : {}".format("1211".isnumeric()))
print("\"123.11\".isnumeric() : {}".format("123.11".isnumeric()))
print("custom_is_float(\"123.11\") : {}".format(custom_is_float("123.11")))
print("\"abdDadfDDAd\".isalpha() : {}".format("abdDadfDDAd".isalpha()))
print("\"abdDadfDDAd123\".isalnum() : {}".format("abdDadfDDAd".isalnum()))

# Reversing the sentence
print("Reverse : sentence[::-1]> :{}".format(sentence[::-1]))



