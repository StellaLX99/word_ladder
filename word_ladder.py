#!/bin/python3
from collections import deque
from copy import copy,deepcopy
filename= dictionary_file='words5.dict'
with open (filename) as dic:
    wholewords= dic.read().split("\n")
    wholewords=set(wholewords)
#print('words=',words) 
def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
# stack=[]creates a list/stack that is empty
# you want to check word by word,make sure there's only one difference between the words, and the difference is only one. the letter will exit the words if being replaced, aka being popped off and will establish to a new stack
# and it is from left to right, the rightest one is the top of the stack, first in last out, last in , first out   
    s=[]
    s.append(start_word) #adding the first word together
    q =deque() 
    q.append(s)#recursion,build upon, first in, first out
    if start_word== end_word:
        return s
    if len(q)==0: #if the queue is empty
        return False 
    while len(q)!=0:
        topstack=q.popleft() #queue is first in first out, from left to right
        for word in set(wholewords):
            if _adjacent(topstack[-1],word): #run to see if only 1 difference, and next to each other
                newwords=deepcopy(topstack) #we want to store it and go on
                newwords.append(word) #add the rest of it in
                if end_word==word: #here we finish basically
                    for i in range(1, len(newwords)-2): # we start looping from the second word to the last second word
                        if _adjacent(newwords[i-1],newwords[i+1]):
                                newwords.pop(i) #get rid of the other words that is not at first and end 
                    return newwords
                q.appendleft(newwords)
                wholewords.remove(word)
    return None 

    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''

    if len(ladder) == 0: # it has to have multiple words to start with 
        return False
    else:
        for i in range(len(ladder)-1):#given this range
            if _adjacent (ladder[i],ladder[i+1])is False:# using the helper function to see if only one difference exists between the words that are next to each other
                return False
        return True 

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
            
#because there's only one different character between this two words, the difference should be 1? 
#so go through the whole index and see if the differnce is one, if it is then add it on?
    df=0 #start with initial difference, which is 0, since we have not run it yet
    if len(word1)!=len(word2):# the two words has to have the same length to start with
        return False
    else: 
        for i in range(len(word1)):#given a range and let it run one by one
            if word1[i]!=word2[i]:# if the letter in the words is not the same, then it means that there is a difference 
                df=df+1 #keep adding one
        if df ==1:#needs to only have 1 differrence
            return True
         else:
            return False 
