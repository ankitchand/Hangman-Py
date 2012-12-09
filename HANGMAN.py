"""
		    GNU GENERAL PUBLIC LICENSE
		       Version 2, June 1991

*******************************************************************************************************************
*   Originally Created by Ankit Chand                                                                             *
*   This is a small game HANGMAN which is only in TEXT MODE for now. Graphic version is coming soon please wait.  *
*   Any changes and issues/bugs are welcome <constructively>.                                                     *
*   Copyright (C) 2012  <Ankit Chand>                                                                             *
*******************************************************************************************************************

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

"""


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    iterate=0
    for i in xrange(0,len(lettersGuessed)):
        for j in xrange(0,len(secretWord)):
            if lettersGuessed[i] == secretWord[j]:
                iterate+=1
    if iterate==len(secretWord):
        return True
    else:
        return False

#print isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's','a','l'])
#print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.   
    '''
    
    guess=secretWord
    li=[]
    i=0
    while i<len(secretWord):
        for letter in lettersGuessed:
            if secretWord[i]== letter:
                li=li+[i]
        i=i+1

    for item in xrange(0,len(guess)):
        if item in li:
            guess=guess
        else:
            guess=guess.replace(guess[item],'_')    
    return guess

#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getGuessedWord('apple' , ['e', 'i', 'k', 'p', 'r', 's'])
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
  
    lo=string.ascii_lowercase
    for item in lettersGuessed:
        lo=lo.replace(item,'')
    return lo

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getAvailableLetters(lettersGuessed)    
    
def isLetter(secretWord,letter):
    if letter in secretWord:
        return True
    else:
        return False
    
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    length=len(secretWord)
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(length)+" letters long."
    flag=True
    mistake=8
    letters=[]
    result=False
    while (mistake!=0):
        #print "GUEsED?: "+str(isWordGuessed(secretWord,letters))
        print "------------"
        print "You have "+ str(mistake)+ " guesses left."
        print "Available letters: "+str(getAvailableLetters(letters))
        char=raw_input("Please guess a letter: ")
        char=char.lower()
        if char in letters:
            letters=letters
            print "Oops! You've already guessed that letter "+str(getGuessedWord(secretWord,letters))
        else:
            letters=letters+[char]
            result=isLetter(secretWord,char)
            
            if result==True:
                print "Good guess: "+str(getGuessedWord(secretWord,letters))
                if (isWordGuessed(secretWord,letters)==True):
                        break
            else:
                print "Oops! That letter is not in my word "+str(getGuessedWord(secretWord,letters))
                mistake-=1
    print "------------"            
    if mistake==0:
        print "Sorry, you ran out of guesses. The word was "+str(secretWord)
    elif isWordGuessed(secretWord, letters)==True:
        print "Congratulations, you won!"


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
