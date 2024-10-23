from packages.fileController import JsonFileControl
from packages.fileController import TextFileControl
import os.path

class getWordsbyCharLen:

    dictionaryfull = JsonFileControl.jsonFetch("all", "json\FullWordList.json")
    wordlist = list(dictionaryfull[0].values())
    dict2 = dictionaryfull + []
    
    xletterwords = []
    
    def wordgetter(wordlength):
     
        if(os.path.isfile("json/"+str(wordlength)+"_letter_word_list")==False):
            for i in getWordsbyCharLen.wordlist:
                for x in i:
                    if(len(x) == wordlength):
                        getWordsbyCharLen.xletterwords.append(x)

            getWordsbyCharLen.xletterwords.sort()
            getWordsbyCharLen.jsonFormatter(getWordsbyCharLen.xletterwords, str(wordlength)+"_letter_word_list")
        else:
            pass
    



    def jsonFormatter(words, filename):
        reference = []
        final = "{"
        letters = JsonFileControl.jsonFetch("letters", "json/LetterData.json")[0]

        for i in letters:
            #create the json object (letter of the alphabet) then assign each word based on the first letter
           
            final+= "'"+str(letters[i])+"':"
            for x in words:
                
                if(x[0] == letters[i]):
                    reference.append(x)
                else:
                    continue

            #finally close the array.
            final+= str(reference)+","
            reference.clear()
        
        final= final[:-1] + "}"
        JsonFileControl.jsonWrite(final, "json/"+ filename +".json")



class DictUpdater:

    def wordadder():
        letters = JsonFileControl.jsonFetch("letters", "json/LetterData.json")[0]
        txtdata = TextFileControl.txtLinetoArray("json\Word Lists\english.txt")
        txtdata.sort()

        for i in letters:
            for x in txtdata:
                if(x[0] == letters[i]):
                    x = str(x).replace("'", "`")
                    getWordsbyCharLen.dict2.append(x)

        getWordsbyCharLen.dict2.sort()
        getWordsbyCharLen.dict2 = list(dict.fromkeys(getWordsbyCharLen.dict2))
        getWordsbyCharLen.jsonFormatter(getWordsbyCharLen.dict2)



#build files from dictionary.json
#getWordsbyCharLen.wordgetter(5)


#DictUpdater.wordadder()