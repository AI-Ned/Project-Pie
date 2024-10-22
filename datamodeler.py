from packages.fileController import fileControl

class getWordsbyCharLen:

    dictionaryfull = fileControl.jsonFetch("all", "json/dictionary.json")[0]
    words = list(dictionaryfull.keys())
    xletterwords = []
    
    def wordgetter(wordlength):
        for i in getWordsbyCharLen.words:
            if(len(i) == wordlength):
                getWordsbyCharLen.xletterwords.append(i)
            else:
                continue
        
        getWordsbyCharLen.xletterwords.sort()
        getWordsbyCharLen.jsonFormatter(getWordsbyCharLen.xletterwords)
    



    def jsonFormatter(words):
        reference = []
        final = "{"
        letters = fileControl.jsonFetch("letters", "json/LetterData.json")[0]

        for i in letters:
            #create the json object (letter of the alphabet) then assign each word based on the first letter
           # reference.append('''"''' + letters[i] + '''":[''')
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

        fileControl.jsonWrite(final, "json/FiveLetterWords.json")

getWordsbyCharLen.wordgetter(5)