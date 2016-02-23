
f = open("test_checker.txt", "r")
def create_file_list(text_file):
    """takes an input file and splits it into a list of words"""
    #outputs a list with each line separated by the \n
    text_file_lines = text_file.readlines()
    #creates empty list called word_list
    word_list = []
    #splits each word based on whitespace, new lines, tabs and creates a list
    for each_line in text_file_lines:
        #splits each line according to empty space
        text_file_words = each_line.split()
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
            #sets a count for how many values are in the list
            count_2 = len(dictionary_list)
            #sets another iteration value to go through that list
            iteration_2 = 0
            while iteration_2 < count_2:
                #pulls out each word from each list and appends it to a new list
                for dictionary_word in dictionary_list:
                    dictionary_words.append(dictionary_word)
                    iteration_2 = iteration_2 + 1
            iteration = iteration + 1
    return dictionary_words

def ignoreCaseAndPunc(word):
    """
        removes capitalization and punction from an input word
        and outputs the adjusted word
    """
    #lowers all letters in word
    word = word.lower()
    #checks each character and replaces "bad characters" with nothing
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
    return word

def findWordInDictionary(word, fileName):
    """
        checks to see if a word is present in the dictionary (fileName)
        after applying the ignoreCaseandPunc function
    """
    #opens the specified file if not already open
    if type(fileName) != file:
        fileName = open(fileName, "r")
    #runs ignoreCaseAndPunc on the word
    word = ignoreCaseAndPunc(word)
    #runs create_file_list on the opened file
    dictionary = create_file_list(fileName)
    #sets an initial value to false
    in_dictionary = False
    for dictionary_word in dictionary:
        #removes any punctuation fromt he dictionary_Word
        dictionary_word = ignoreCaseAndPunc(dictionary_word)
        #if the words match changes the in_dictionary value to true
        if dictionary_word == word:
            in_dictionary = True
    return in_dictionary
        

def getWordsOfSimLength(word, fileName, n):
    """
        finds words with similar length +/- (n) to word
        from the dictionary (fileName), returns list
    """
    #opens specified file
    fileName = open(fileName, "r")
    #gets the length of the word
    l_word = len(word)
    #defines the upper bound
    length_1 = l_word + n
    #defines the lower bound
    length_2 = l_word - n
    word_list = []
    #creates a list from the fileName
    dictionary = create_file_list(fileName)
    #scans through words in the dictionary list
    for dictionary_word in dictionary:
        #counts the length of each list
        dictionary_word_c = len(dictionary_word)
        iteration = 0
        #iterates within the specified range n
        while iteration < n:
            #checks the length of the words against the specified range and appends them to word_list
            if (dictionary_word_c == (length_1-iteration) or dictionary_word_c == (length_2+iteration)):
                word_list.append(dictionary_word)
            iteration = iteration + 1
        if dictionary_word_c == l_word:
            word_list.append(dictionary_word)
        
    return word_list

def getWordsWithSameStart(word, wordList, n):
    """
        Given a word and a list of specific words, returns a
        list that match the first n characters
    """
    #gets the length of the word
    l_word = len(word)
    #constrains n to the length of the word
    if n > l_word:
        n = l_word
    dictionary = wordList[:]
    #creates a word_list to store the words
    word_list = []
    check = False
    #for each word in the list, iterate
    for dictionary_word in dictionary:
        #iterates through indices 0 through n-1
        for iteration in range(0, n):
            #only checks words that can actually match the character amounts
            if n <= len(dictionary_word):
                #returns true value if a character matches
                if word[iteration] == dictionary_word[iteration]:
                    check = True
                else:
                    check = False
                #if at any time a non-matching character appears, ends the iteration
                #this avoids the last character matching and giving a True value
                if check == False:
                    break
            #if no characters match check = False
            else:
                check = False
        #only if check = True for all the characters will a word be added to the list
        if check == True:
            #appends the word from wordList to the word_list list
            word_list.append(dictionary_word)
    return word_list
        
def getWordsWithCommonLetters(word, wordList, n):
    """
        returns a list with words that have n amount or more letters in common
        ignores repeat letters
    """
    dictionary = wordList[:]
    #creates an empty list
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
        dictionary_word_ch = []
        ch_list = []
        #takes each word and creates a set of unique characters
        for d_word_ch in dictionary_word:
            dictionary_word_ch.append(d_word_ch)
            dictionary_word_ch_set = set(dictionary_word_ch)
        #as long as the minumum required number of common characters is not greater than the word itself
        if len(dictionary_word_ch) >= n and n != 0:
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
    return word_list
            

def getSimilarityMetric(word1, word2):
    """
        Returns two measures of similarity given two words and returns an average.
        These are numbers of letters that match up going from left to right and
        right to left.
    """
    #empty lists to hold characters
    ch_word1 =[]
    ch_word2 = []
    #maps characters from each word to lists
    for ch in word1:
        ch_word1.append(ch)
    for ch2 in word2:
        ch_word2.append(ch2)
    #records lengths for each word
    count1 = len(ch_word1)
    count2 = len(ch_word2)
    #sets iteration value to 0
    iteration = 0
    score_left = 0
    #sets while loop to iterate until all the letters have been compared
    while iteration < count1 and iteration < count2:
        #as long as the letters match a score value will be increased by one
        if ch_word1[iteration] == ch_word2[iteration]:
            score_left = score_left + 1
            iteration = iteration + 1
        else:
            iteration = iteration + 1
    #reverses the lists so can be read from right to left
    rt_ch_word1 = ch_word1[-1::-1]
    rt_ch_word2 = ch_word2[-1::-1]
    iteration = 0
    score_right = 0
    #same as above except records score for right to left
    while iteration < count1 and iteration < count2:
        if rt_ch_word1[iteration] == rt_ch_word2[iteration]:
            score_right = score_right + 1
            iteration = iteration + 1
        else:
            iteration = iteration + 1
    #calculates the similarity
    similarity = ((score_left + score_right) / 2.0)
    return similarity
    

def getSimilarityDict(word, wordList):
    """
        creates a dictionary of similar words, uses getSimilarityMetric to
        create values that have keys which are in wordList
    """
    dictionary = wordList
    #creates empty dictionary
    word_dict = {}
    for dictionary_word in dictionary:
        score = getSimilarityMetric(word, dictionary_word)
        word_dict[dictionary_word]=score
    return word_dict

def sortIn2D(tup1, tup2):
    """takes two tuples and compares the second component"""
    #compares the last component of each tuple and outputs different values
    #based on the arguments
    if tup1[-1] < tup2[-1]:
        return -1
    elif tup1[-1] == tup2[-1]:
        return 0
    else:
        return 1

def getListOfFirstComponents(tupleList):
    """takes in a list of tuples and returns a list with just the first components"""
    #creates a list to store the new values
    new_list = []
    #removes the first value from each tuple in the tupleList and adds it to the new_list
    for a_tuple in tupleList:
        new_list.append(a_tuple[0])
        
    return new_list
    
def getBestWords(SimilarityDictionary, n):
    """Uses a similarity dictionary and outputs a list of the top n terms by sorting."""
    list_of_tuples = SimilarityDictionary.items()
    list_of_tuples.sort(sortIn2D, reverse=True)
    return getListOfFirstComponents(list_of_tuples)[0:n]

def getWordSuggestionsV1(word, fileName, n, commonPercent, topN):
    """
        If the input word is incorrect returns a list of suggested words
        based on a +/i n argument (length) and having at least commonPercent
        in common.  The topN (number) of suggestions are returned.
    """
    
    #imports the math module
    import math
    #finds the length of the given word
    l_word = len(word)
    #uses the commonPercent that was input to determine the amount of letters that should be matched
    commonPercent = (commonPercent/100.0)*l_word
    #uses math.ceil to raise the value to the higher integer so that the threshold is preserved
    commonPercent = math.ceil(commonPercent)
    #returns commonPercent to an integer
    commonPercent = int(commonPercent)
    #creates an empty list in which the final words will be stored
    word_list = []
    #uses the input word, the dictionary and the length argument to generate a list of
    #words that satisfy the given arguments
    length_list = getWordsOfSimLength(word, fileName, n)
    #opens the file
    fileName = open(fileName, "r")
    #creates a list of words from the file
    database = create_file_list(fileName)
    #same as above except for commonPercent argument
    common_letter_list = getWordsWithCommonLetters(word, database, commonPercent)
    #records the length of the database
    database_length = len(database)
    #loops through words in the length_list and checks if they are in the common_letter_list
    #if so, adds these words to the new word_list
    for a_word in length_list:
        if a_word in common_letter_list:
            word_list.append(a_word)
    #new list called final_list
    final_list = []
    #defines indices that will be added to the final list with given boundary conditins
    if topN - 1 < len(word_list):
        for index in range(0, topN):
            final_list.append(word_list[index])
    #if the top words returned don't exist to the topN degree returns all words
    else:
        final_list = word_list[:]
        
    return final_list
        

def getWordSuggestionsV2(word, fileName, n, topN):
    """
        If the input is an incorrect word, provides a list of words from
        fileName, finds words +/- one in length.  Words that begin/end with the same
        n letters. Generates list and orders the list and returns the topN words.
    """
    length_list = getWordsOfSimLength(word, fileName, 1)
    #opens the file
    fileName = open(fileName, "r")
    #creates a list of words from the file
    database = create_file_list(fileName)
    #defines start list as a list based off of the function
    start_list = getWordsWithSameStart(word, database, n)
    #reverses the original word
    reverse_word = word[-1::-1]
    new_database = []
    #for each word in the database list, reverses the word and adds it to new_database
    for dictionary_word in database:
        reverse_dictionary_word = dictionary_word[-1::-1]
        new_database.append(reverse_dictionary_word)
    #compares the reversed word to the reversed database, effectively comparing ends
    end_list = getWordsWithSameStart(reverse_word, new_database, n)
    new_end_list = []
    #unreverses the newly created list so that it can be compared to the other lists
    for end_words in end_list:
        reverse_end_word = end_words[-1::-1]
        new_end_list.append(reverse_end_word)
    word_list = []
    #compares all the lists and creates a new list of all the common words
    for a_word in start_list:
        if a_word in new_end_list and a_word in length_list:
            word_list.append(a_word)
    #creates a final list according the the getBestWords function and a newly created Similarity dictionary
    final_list = getBestWords((getSimilarityDict(word, word_list)), topN)
    return final_list
    
def getCombinedWordSuggestions(word, fileName):
    """
        Combines V1 and V2 output lists, takes 7 from each function, uses
        75% as a threshold for the first
    """
    #stores the list outputed by function V1
    lst1 = getWordSuggestionsV1(word, fileName, 2, 75, 7)
    #stores the list outputed by function V2
    lst2 = getWordSuggestionsV2(word, fileName, 1, 7)
    #adds all the elements in lst1 to lst2
    for a_word in lst1:
        lst2.append(a_word)
    #creates a set to remove all duplicates
    new_list = set(lst2)
    #copies the set into a new list
    prerank_list = lst2[:]
    #ranks the list according tot he getBestWords function using a newly created similarity dictionary
    ranked_list = getBestWords((getSimilarityDict(word, prerank_list)), 10)
    return ranked_list

def prettyPrint(lst):
    iteration = 1
    while iteration <= len(lst):
        for a_word in lst:
            print str(iteration)+".", a_word
            iteration = iteration + 1

def docu_correction(fileName):
    #opens the file to be corrected
    fileName = open(fileName, "r")
    write_new_file = open("corrected_file.txt", "w")
    #creates a list of words from the file
    file_words = create_file_list(fileName)
    #loops through each word
    for word in file_words:
        dictionary = open("engDictionary.txt", "r")
        #removes punctuation
        new_word = ignoreCaseAndPunc(word)
        #checks to see if the new_word exists in the dictionary
        check = findWordInDictionary(word, dictionary)
        if check == True:
            write_new_file.write(new_word + " ")
        else:
            #takes the engDictionary.txt file and loops through the words to find the best match
            word_list = getCombinedWordSuggestions(new_word, "engDictionary.txt")
            if word_list != []:
            #writes the new suggested word to the file
                write_new_file.write(word_list[0]+" ")
            else:
                write_new_file.write(word + " ")
        dictionary.close()
    write_new_file.close()
    fileName.close()

def main():
    print "Welcome to the Spell Checker Program!"
    #prompt for user to open the file to be corrected
    user_sel_file = raw_input("Which file would you like to correct? Please include the file extension:\n")
    #opens the selected file
    user_file = open(user_sel_file, "r")
    #records length of the file
    user_file_l = len(user_sel_file)
    #sets number to remove the last for elements
    rem_ext = user_file_l - 4
    #removes the last for elements, assumes a 4 element extension, such as .txt or .jpg
    corr_user_file = user_sel_file[0:rem_ext]
    #adds on the -chk.txt
    corr_user_file = corr_user_file + "-chk.txt"
    #opens a file with the new name to write to
    corr_user_file_w = open(corr_user_file, "w")
    #asks for a reference file to compare to
    user_sel_ref = raw_input("Which reference file would you like to use? Please Include the file extension.\nIf you would like to use the default file please type, D.\n")
    #sets D, as the defualt engDictionary otherwise uses the user input
    if user_sel_ref == "D":
        dictionary = "engDictionary.txt"
    else:
        dictionary = user_sel_ref
    #creates a list of individual words from the user file
    user_file_list = create_file_list(user_file)
    #iterates through each word in the list
    for word in user_file_list:
        #opens the selected dictionary
        dictionary_r = open(dictionary, "r")
        #checks if the word exists in the dictionary, and if it does, appends it to the writable file
        check = findWordInDictionary(word, dictionary)
        if check == True:
            corr_user_file_w.write(word + " ")
        #finds alternatives from the dictionary if the word is mispelled
        else:
            options = getCombinedWordSuggestions(word, dictionary)
            #as long as there are options
            if options != []:
                print "The word,", word, "is not spelled correctly."
                print "The following are available suggestions:"
                #converts the options to a user friendly output
                prettyPrint(options)
                #asks the user what they want to do
                user_option = raw_input("Press ""r"" for replace, ""a"" for accept as is, ""t"" for type in manually\n")
                #makes sure the input makes sense
                while user_option != "r" and user_option != "a" and user_option != "t":
                    print "You have typed an incorrect key, please try again."
                    user_option = raw_input("Press ""r"" for replace, ""a"" for accept as is, ""t"" for type in manually\n")
                #for the r-case, makes sure that the user uses a number that is allowed and then appends that to the writable file
                if user_option == "r":
                    user_option_2 = input("Select the number corresponding to the word you wish to replace:\n")
                    while user_option_2 > len(options):
                        print "You have typed an incorrect key, please try again"
                        user_option_2 = input("Select the number corresponding to the word you wish to replace:\n")
                    #adds the word to the file, note a space is added between each word    
                    corr_user_file_w.write(options[user_option_2-1] + " ")
                #accepts and adds the word to the file
                elif user_option == "a":
                    corr_user_file_w.write(word + " ")
                #takes whatever input is given by the user and adds it to the file
                elif user_option == "t":
                    user_manual = raw_input("Please type the word you would like to enter instead:\n")
                    corr_user_file_w.write(user_manual + " ")
            else:
                #similar to above with "r" option removed
                print "The word,", word, "is not spelled correctly."
                print "There are 0 suggestions in the dictinary available."
                user_option_3 = raw_input("Press ""a"" for accept as is, ""t"" for type in manually\n")
                while user_option_3 != "a" and user_option_3 != "t":
                    print "You have typed an incorrect key, please try again."
                    user_option_3 = raw_input("Press ""a"" for accept as is, ""t"" for type in manually\n")
                if user_option == "a":
                    corr_user_file_w.write(word + " ")
                elif user_option == "t":
                    user_manual = raw_input("Please type the word you would like to enter instead:\n")
                    corr_user_file_w.write(user_manual + " ")
        #closes the reference dictionary            
        dictionary_r.close()
    #closes the original user file    
    user_file.close()
    #closes the writable file
    corr_user_file_w.close()
    
if __name__ == '__main__':
    main()
    

    
"""
WHY DOES THE BELOW CAUSE THE DICTIONARY TO BECOME EMPTY UPON ITERATION?
def main():
    print "Welcome to the Spell Checker Program!"
    user_sel_file = raw_input("Which file would you like to correct? Please include the file extension:\n")
    user_file = open(user_sel_file, "r")
    user_file_l = len(user_sel_file)
    rem_ext = user_file_l - 4
    corr_user_file = user_sel_file[0:rem_ext]
    corr_user_file = corr_user_file + "-chk.txt"
    corr_user_file_w = open(corr_user_file, "w")
    user_sel_ref = raw_input("Which reference file would you like to use? Please Include the file extension.\nIf you would like to use the default file please type, D.\n")
    if user_sel_ref == "D":
        dictionary = open("engDictionary.txt", "r")
    else:
        dictionary = open(user_sel_ref, "r")
    user_file_list = create_file_list(user_file)
    
    for word in user_file_list:
        check = findWordInDictionary(word, dictionary)
        print check
        if check == True:
            corr_user_file_w.write(word)
    dictionary.close()
    user_file.close()
    corr_user_file_w.close()
    
if __name__ == '__main__':
    main()
"""    
