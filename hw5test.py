
f = open("test_checker.txt", "r")
fileName = open("test_dictionary.txt", "r")

from spellChecker import *

text_file_lines = f.readlines()
print text_file_lines
#creates empty list called word_list
word_list = []
#splits each word based on whitespace, new lines, tabs and creates a list
for each_line in text_file_lines:
    print each_line
    #splits each line according to empty space
    text_file_words = each_line.split()
    print text_file_words
    print len(text_file_words)
    
    #stores the output as a list in a list
    word_list.append(text_file_words)
#length of word_list
count = len(word_list)
#sets an iteration value of 0
iteration = 0
#runs a while loop that states that as long as the iteration value
#is still within the count, basically defines the range
dictionary_list = []
dictionary_words = []
while iteration < count:
    #loops through all the values in the dictionary list
    for dictionary_list in word_list:
        #pulls out each word from the dictionary list
        count_2 = len(dictionary_list)
        iteration_2 = 0
        while iteration_2 < count_2:
            for dictionary_word in dictionary_list:
                dictionary_words.append(dictionary_word)
                iteration_2 = iteration_2 + 1
        iteration = iteration + 1






"""
text_file_lines = f.readlines()
word_list =[]
for each_line in text_file_lines:
    words = each_line.split()
    word_list.append(words)

print word_list
"""
"""
word = "H,,EL,Per,"
word = word.lower()

    #for ch in word:
        #if ch == ",":
            #word_list = word.split(",")
            #count = len(word_list)
            #iteration = count - 1
            #while iteration > 0:
                #word = word_list[0] + word_list[count - iteration]
                #iteration = iteration - 1
            
for ch in word:
        if ch == ",":
            word = word.replace(",","")
        if ch == ";":
            word = word.replace(";","")
        if ch == "?":
            word = word.replace("?","")
        if ch == "!":
            word = word.replace("!","")
        if ch == ":":
            word = word.replace(":","")
        if ch == ".":
            word = word.replace(".","")  
            


from spellChecker import *
dictionary = create_file_list(fileName)

#print in_dictionary
word = "Animals"
word = ignoreCaseAndPunc(word)
in_dictionary = False
count = len(dictionary)
iteration = 0
while iteration < count:
    for dictionary_word in dictionary:
        dictionary_word = dictionary[0+iteration][0]
        dictionary_word = ignoreCaseAndPunc(dictionary_word)
        if dictionary_word == word:
            print ""
        iteration = iteration + 1
"""
"""
print ""
print ""
print ""

n = 1
word = "save"

l_word = len(word)
length_1 = l_word + n
length_2 = l_word - n
iteration = 0
word_list = []
dictionary = create_file_list(fileName)
for dictionary_word in dictionary:
    dictionary_word_c = len(dictionary_word)
    for iteration in range(0,n):
        if (dictionary_word_c == (length_1-iteration) or dictionary_word_c == (length_2+iteration)
            or dictionary_word_c == l_word):
            word_list.append(dictionary_word)
        iteration = iteration + 1
    

print word_list
"""
"""
word = "Afples"
n = 2
#gets the length of the word
l_word = len(word)
#constrains n to the length of the word
if n > l_word:
    n = l_word
#creates a list out of the input file
dictionary = create_file_list(fileName)
#creates a word_list to store the words
word_list = []
check = False
#for each word in the list
for dictionary_word in dictionary:
    #iterates from 0 through n-1
    for iteration in range(0, n):
        #print dictionary_word
        #print len(dictionary_word)
        if n <= len(dictionary_word):
            #print dictionary_word
            #print iteration
            if word[iteration] == dictionary_word[iteration]:
                #print dictionary_word[iteration]
                check = True
            else:
                check = False

            if check == False:
                break
        else:
            check = False
        print check
    if check == True:
        word_list.append(dictionary_word)
        
print word_list
"""
"""
word = "Thane"
n=3
dictionary = create_file_list(fileName)
word_ch = []
#takes each character from the input word and adds it to the mepty list
for ch in word:
    word_ch.append(ch)
#converts the list into a unique set
word_ch = set(word_ch)
#creates an empty list
word_list = []
#goes through all words in the loaded list
for dictionary_word in dictionary:
    #takes each word and creates a set of unique characters
    dictionary_word_ch = []
    ch_list = []
    for d_word_ch in dictionary_word:
        dictionary_word_ch.append(d_word_ch)
        dictionary_word_ch_set = set(dictionary_word_ch)
    #as long as the minumum required number of common characters is not greater than the word itself
    if len(dictionary_word_ch) >= n:
        #loops through each character in the set
        for char in dictionary_word_ch_set:
            #checks to see if each character is in the set made from the word
            if char in word_ch:
                #adds the character to a list 
                ch_list.append(char)
        #if the amount of characters is equal to or greater than the required amount the
        #loaded list word is added to a new list
        if len(ch_list) >= n:
            word_list.append(dictionary_word)
"""
"""
def whatDoesThisFunctionDo(x,y):
    if x[-1] < y[-1]: return -1
    elif x[-1] == y[-1]: return 0
    return 1
 
data = [['arv','Penn', 33], ['fed', 'West Point', 45],
        ['Ben', 'Cornell', 25], ['Steven', 'UVA', 24]]
 
data.sort(whatDoesThisFunctionDo)

print data
"""
"""
tupleList = [("A", 0), ("alpha", 3), ("C", 0)]
new_list = []
for a_tuple in tupleList:
    new_list.append(a_tuple[0])

print new_list
"""
"""
#imports the math module
import math
word = "Affable"
commonPercent = 30
fileName = "test_dictionary.txt"
n = 5

#finds the length of the given word
l_word = len(word)
#print l_word
#uses the commonPercent that was input to determine the amount of letters that should be matched
commonPercent = (commonPercent/100.0) * l_word
#print commonPercent
#uses math.ceil to raise the value to the higher integer so that the threshold is preserved
commonPercent = math.ceil(commonPercent)
#print commonPercent
#returns commonPercent to an integer
commonPercent = int(commonPercent)
#print commonPercent
#creates an empty list in which the final words will be stored
word_list = []
#uses the input word, the dictionary and the length argument to generate a list of
#words that satisfy the given arguments
length_list = getWordsOfSimLength(word, fileName, n)
print length_list
#same as above except for commonPercent argument
common_letter_list = getWordsWithCommonLetters(word, fileName, commonPercent)
print common_letter_list
#opens the file
fileName = open(fileName, "r")
#creates a list of words from the file
database = create_file_list(fileName)
#records the length of the database
database_length = len(database)
#loops through words in the length_list and checks if they are in the common_letter_list
#if so, adds these words to the new word_list
for a_word in length_list:
    if a_word in common_letter_list:
        word_list.append(a_word)

print word_list
"""
"""
word = "Appleplate"
fileName = "test_dictionary_2.txt"
n = 3
topN = 2
length_list = getWordsOfSimLength(word, fileName, 1)
print length_list
#opens the file
fileName = open(fileName, "r")
#creates a list of words from the file
database = create_file_list(fileName)
#print database
start_list = getWordsWithSameStart(word, database, n)
print start_list
reverse_word = word[-1::-1]
#print reverse_word
new_database = []
for dictionary_word in database:
    reverse_dictionary_word = dictionary_word[-1::-1]
    #print reverse_dictionary_word
    new_database.append(reverse_dictionary_word)
end_list = getWordsWithSameStart(reverse_word, new_database, n)
new_end_list = []
for end_words in end_list:
    reverse_end_word = end_words[-1::-1]
    new_end_list.append(reverse_end_word)
print new_end_list
word_list = []
for a_word in start_list:
    if a_word in new_end_list and a_word in length_list:
        word_list.append(a_word)
print word_list
final_list = getBestWords((getSimilarityDict(word, word_list)), topN)

print final_list
"""
"""
lst = ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"]
iteration = 1
while iteration <= len(lst):
    for a_word in lst:
        print str(iteration)+".", a_word
        iteration = iteration + 1
        """
"""
def main():
    
    #print corr_user_file
    corr_user_file_w = open("corr_user_file.txt", "w")
    user_file = open("test_checker_copy.txt", "r")
    dictionary = open("test_checker_dictionary.txt", "r")
    user_file_list = create_file_list(user_file)
    
    #print user_file_list
    for word in user_file_list:
        dictionary = open("test_checker_dictionary.txt", "r")
        check = findWordInDictionary(word, dictionary)
        print check
        if check == True:
            corr_user_file_w.write(word)
        dictionary.close()
    dictionary.close()
    user_file.close()
    corr_user_file_w.close()
    
if __name__ == '__main__':
    main()
"""
