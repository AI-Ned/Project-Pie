from archivedCode.api import DictApi
from piConverter import PiToString as p2s
from packages.fileController import JsonFileControl
from datamodeler import getWordsbyCharLen
#import json
import time

pistring = p2s.encode()
values = []
wordlengthreq = "5" #input("Enter the character length as a whole number: ")
wordlength = int(wordlengthreq)

#load in the illegal character combinations.
illegalSets = JsonFileControl.jsonFetch("non_existent_combinations","json/LetterData.json")

#itterate through all of the 5 word values in the converted pi number, discard any letter combinations that have characters combinations that don't exist in the english language
#any successful letter combinations are then added to the value array. 
def findwords():
   
    position = 0
    #potential words
    potword = ''
  

    while(position < len(pistring)-4):
        
        if(len(potword)< wordlength):
            for i in pistring[position:position+wordlength]:
                potword += i
        


        if(illegalcharacterCombos(potword)== True):

            list = JsonFileControl.jsonFetch(potword[0],"json/"+wordlengthreq+"_letter_word_list.json")
            searchlist = set(list)
            if(potword in searchlist):
                values.append(potword)
            potword = ""
            position += 1

        else:
            potword = ""
            position += 1
            continue
                    
            
    getWordsbyCharLen.jsonFormatter(values, wordlengthreq+" Results")        
    #print(values)

def illegalcharacterCombos(characters):

    #baddieset = [i for i in illegalSets if characters.find(i) > -1]
    #baddiecharacter = [x for x in characters[0:3] if characters.find(x+x+x) > -1]
    
    #if(len(baddiecharacter) > 0 or len(baddieset) > 0):
    #    baddiecharacter.clear()
    #    baddieset.clear()
    #    return False
    #else:
    #    return True
    
    for i in illegalSets:

        if(characters.find(i)!=-1):
            return False

   
    for x in characters[0:3]:
        
        if(characters.find(x+x+x)!=-1):
            return False
       
    return True


start_time = time.time()
if int(wordlengthreq):
    getWordsbyCharLen.wordgetter(wordlength)
    findwords()
else:
    print("That was not an integer")

print("--- %s seconds ---" % (time.time() - start_time))