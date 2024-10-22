from api import DictApi
from piConverter import PiToString as p2s
from packages.fileController import fileControl
import json

pistring = p2s.encode()
values = []

#load in the illegal character combinations.
illegalSets = fileControl.jsonFetch("non_existent_combinations","json/LetterData.json")

#itterate through all of the 5 word values in the converted pi number, discard any letter combinations that have characters combinations that don't exist in the english language
#any successful letter combinations are then added to the value array. 
def findwords():
   
    position = 0
    #potential words
    potword = ''

    while(position < len(pistring)-4):
        
        if(len(potword)< 5):
            for i in pistring[position:position+5]:
                potword += i
        
        #elif(len(potword) >= 5):

        if(illegalcharacterCombos(potword)== True):
            #if(DictApi.wordtest(potword) == True):
            values.append(potword)
            potword = ""
            position += 1
            #else:
             #   potword = ""
             #   position += 1
              #  continue
        else:
            potword = ""
            position += 1
            continue
                    #print(potword + " has no illegal characters")
            
            
    print(values)

def illegalcharacterCombos(characters):

    for i in illegalSets:

        if(characters.find(i)!=-1):
            return False

   
    for x in characters[0:3]:
        
        if(characters.find(x+x+x)!=-1):
            return False

        
    return True


findwords()