#Philip Kyd

import unittest
from spellChecker import *

class test_spellChecker(unittest.TestCase):
    def setUp(self):
        self.test_file = open("test_checker.txt", "r")
        self.test_dictionary = open("test_dictionary.txt", "r")
        self.test_dictionary_2 = open("test_dictionary_2.txt", "r")

    def test_create_file_list(self):
        dictionary_words = create_file_list(self.test_file)
        #checks to make sure that the 0th element is the correct word
        self.assertEqual("Do", dictionary_words[0] )
        #checks to make sure that the 17th element is the correct word
        self.assertEqual("shouldn't", dictionary_words[17] )
        #checks to make sure the overall length of the list is exactly the number of words in the list
        self.assertEqual(36, len(dictionary_words))

    """
    WHY DOES THE FOLLOWING NOT WORK?
    
    def test_create_file_list(self):
        self.assertEqual("Do", create_file_list(self.test_file)[0][0] )
        self.assertEqual("shouldn't", create_file_list(self.test_file)[1][4] )

    """

    def test_ignoreCaseAndPunc(self):
        #tests capitalization
        self.assertEqual("help", ignoreCaseAndPunc("Help"))
        #tests another form of capitalization
        self.assertEqual("help", ignoreCaseAndPunc("HelP"))
        #tests the removal of a comma
        self.assertEqual("help", ignoreCaseAndPunc("Help,"))
        #tests the removal of a comma and semicolon
        self.assertEqual("help", ignoreCaseAndPunc("Help,;"))
        #tests the remove of additonal punctuation and punctuation location
        self.assertEqual("help", ignoreCaseAndPunc(":Help,;"))
        #tests the removal of additional punctuation and an alternative punctuation location
        self.assertEqual("help", ignoreCaseAndPunc(":He!lp,;"))
        #tests the removal of additional punctuation
        self.assertEqual("help", ignoreCaseAndPunc(":He!lp,;."))
        #tests the removal of additional punctuation
        self.assertEqual("help", ignoreCaseAndPunc(":?He!lp,;."))
        #tests the removal of repeat punctuation and a full mixture of errors
        self.assertEqual("help", ignoreCaseAndPunc(":?He!,lp,;;."))
    
    def test_findWordInDictionary(self):
        #checks to make sure a known word is recorded as in the dictionary
        self.assertEqual(True, findWordInDictionary("you", "test_dictionary.txt"))
        #checks an additional word and capitalization
        self.assertEqual(True, findWordInDictionary("Animals", "test_dictionary.txt"))
        #checks to make sure punctuation has been removed
        self.assertEqual(True, findWordInDictionary("Animals,!", "test_dictionary.txt"))
        #checks to make sure that correct values are returned when something isn't in the dictionary
        self.assertEqual(False, findWordInDictionary("rabid", "test_dictionary.txt"))
        #checks to make sure that the return value is accurate
        self.assertFalse(findWordInDictionary("table", "test_dictionary.txt"))

    def test_getWordsOfSimLength(self):
        #checks to make sure that the list produced is accurate
        self.assertEqual(["You", "Think", "Exist", "Are", "They", "Merry"], getWordsOfSimLength("done", "test_dictionary.txt", 1))
        #checks a word that has equal length to a word in the dictionary 
        self.assertEqual(["Think", "Animals", "Exist", "They", "Merry", "Affliction"], getWordsOfSimLength("Affable", "test_dictionary.txt", 3))
        #checks another extreme at the low end
        self.assertEqual(["Do", "Or", "A",], getWordsOfSimLength("I", "test_dictionary.txt", 1))
        #checks a wide range tomake sure all words are included
        self.assertEqual(["Animals", "Affliction"], getWordsOfSimLength("Happiness", "test_dictionary.txt", 3))
        #checks another word
        self.assertEqual(["Think", "Animals", "Exist", "They", "Merry", "Affliction"], getWordsOfSimLength("Affable", "test_dictionary.txt", 3))
        #checks to make sure that an empty list is returned when a word that has no matches is entered
        self.assertEqual([], getWordsOfSimLength("AppleBanananaCantelope", "test_dictionary.txt", 1))
        #checks an extreme range
        self.assertEqual(["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], getWordsOfSimLength("Happiness", "test_dictionary.txt", 15))

    def test_getWordsWithSameStart(self):
        #matches first 2 characters
        self.assertEqual(["Think", "They"], getWordsWithSameStart("Thanks!", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 2))
        #matches first character
        self.assertEqual(["Animals", "Are", "A", "Affliction"], getWordsWithSameStart("Apples", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 1))
        #makes sure that an empty list is returned if nothing matches
        #this also tests to make sure that the last character matching doesn't indicate a match
        self.assertEqual([], getWordsWithSameStart("Apples", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 4))

    def test_getWordsWithCommonLetters(self):
        #test case for 3 common letters
        self.assertEqual(["Think", "They"], getWordsWithCommonLetters("Thane!", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 3))
        #test case for 2 common letters
        self.assertEqual(["Animals", "Affliction"], getWordsWithCommonLetters("An", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 2))
        #test case for 0 common letters
        self.assertEqual([], getWordsWithCommonLetters("An", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 0))
        #test case for asking for too many common letters
        self.assertEqual([], getWordsWithCommonLetters("An", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"], 20))

    def test_getSimilarityMetric(self):
        #general test case
        self.assertEqual(2, getSimilarityMetric("Apple", "Append"))
        #defines the case where nothing matches
        self.assertEqual(0, getSimilarityMetric("xyz", "abc"))
        #defines case where everything mtches
        self.assertEqual(5, getSimilarityMetric("Apple", "Apple"))
        #general test case #2
        self.assertEqual(2, getSimilarityMetric("Joy", "Boy"))

    def test_getSimilarityDict(self):
        #tests a word with few similarities to the list
        self.assertEqual({"Do" : 0, "You" : 0, "Think" : 0, "Animals" : 1.0,
                          "Exist" : 0, "Or" : 0, "Are" : 1.0, "They" : 0, "A" : 0.5, "Merry" : 0,
                          "Affliction" : 1.0},getSimilarityDict("Apple", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"]))
        #tests a word with zero similarities to the list
        self.assertEqual({"Do" : 0, "You" : 0, "Think" : 0, "Animals" : 0,
                          "Exist" : 0, "Or" : 0, "Are" : 0, "They" : 0, "A" : 0, "Merry" : 0,
                          "Affliction" : 0},getSimilarityDict("X", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"]))
        #tests a word that is the same as one word in the dictionary
        self.assertEqual({"Do" : 2.0, "You" : 0.5, "Think" : 0, "Animals" : 0,
                          "Exist" : 0, "Or" : 0, "Are" : 0, "They" : 0, "A" : 0, "Merry" : 0,
                          "Affliction" : 0},getSimilarityDict("Do", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"]))
        
    def test_sortIn2D(self):
        #the following test cases check all the expected returns from this function
        self.assertEqual(1, sortIn2D(("A", 5), ("B", 3)))
        self.assertEqual(-1, sortIn2D(("A", 2), ("B", 7)))
        self.assertEqual(0, sortIn2D(("A", 4), ("B", 4)))

    def test_getListOfFirstComponents(self):
        #test case for standard tuple list input
        tupleList = [("A", 0), ("B", 3), ("C", 0)]
        self.assertEqual(["A", "B", "C"], getListOfFirstComponents(tupleList))
        #test case for repeated first values
        self.assertEqual(["A", "A", "C"], getListOfFirstComponents([("A", 0), ("A", 3), ("C", 0)]))
        #test case for mixed string
        self.assertEqual(["A", "alpha", "C"], getListOfFirstComponents([("A", 0), ("alpha", 3), ("C", 0)]))

    def test_getBestWords(self):
        #tests output of the first top word
        self.assertEqual(["Do"], getBestWords((getSimilarityDict("Do", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"])), 1))
        #test output of the two top words
        self.assertEqual(["Do", "You"], getBestWords((getSimilarityDict("Do", ["Do", "You", "Think", "Animals", "Exist", "Or", "Are", "They", "A", "Merry", "Affliction"])), 2))  
     
    def test_getWordSuggestionsV1(self):
        #tests a known result with topN = two values
        self.assertEqual(["Animals", "Affliction"], getWordSuggestionsV1("Affable", "test_dictionary.txt", 5, 30, 2))
        #tests to constrain the result to a lesser top value
        self.assertEqual(["Animals"], getWordSuggestionsV1("Affable", "test_dictionary.txt", 5, 30, 1))
        #tests a range outside of the total # of words available
        self.assertEqual(["Animals", "Affliction"], getWordSuggestionsV1("Affable", "test_dictionary.txt", 5, 30, 3))
        #tests an extreme range
        self.assertEqual(["Animals", "Affliction"], getWordSuggestionsV1("Affable", "test_dictionary.txt", 5, 30, 9))
        #tests a 0 constraint
        self.assertEqual([], getWordSuggestionsV1("Affable", "test_dictionary.txt", 5, 30, 0))

    def test_getWordSuggestionsV2(self):
        #tests for known word that matches
        self.assertEqual(["Animals"], getWordSuggestionsV2("Animals", "test_dictionary.txt", 2, 1))
        #test case for a 0 returned words
        self.assertEqual([], getWordSuggestionsV2("Animals", "test_dictionary.txt", 2, 0))
        #test case for more topN words than exist
        self.assertEqual(["Animals"], getWordSuggestionsV2("Animals", "test_dictionary.txt", 2, 3))
        #similar to first test, single letter
        self.assertEqual(["A"], getWordSuggestionsV2("A", "test_dictionary.txt", 1, 2))
        #test case for multiple output
        self.assertEqual(["Appelfrate", "Aperlprite"], getWordSuggestionsV2("Appleplate", "test_dictionary_2.txt", 2, 2))
        #test case for increased match, n requirement
        self.assertEqual(["Appelfrate"], getWordSuggestionsV2("Appleplate", "test_dictionary_2.txt", 3, 2))

    def test_getCombinedWordSuggestions(self):
        #checks for expected outcome
        self.assertEqual(["Appelfrate", "Aperlprite"], getCombinedWordSuggestions("Appleplate", "test_dictionary_2.txt"))
        #checks for non-existant case
        self.assertEqual([], getCombinedWordSuggestions("Apple", "test_dictionary_2.txt"))
        #checks for alternate casev
        self.assertEqual(["Animals"], getCombinedWordSuggestions("Animals", "test_dictionary_2.txt"))
        
unittest.main()
