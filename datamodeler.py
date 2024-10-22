from packages.fileController import fileReader

class wordGetterbyCharLen:

    dictionaryfull = fileReader.jsonFetch("all", "json/dictionary.json")[0]
    words = list(dictionaryfull.keys())
    xletterwords = []
    
    def wordgetter(wordlength):
        for i in wordGetterbyCharLen.words:
            if(len(i) == wordlength):
                wordGetterbyCharLen.xletterwords.append(i)
            else:
                continue
        
        wordGetterbyCharLen.xletterwords.sort()
        return wordGetterbyCharLen.xletterwords
    

        #print(wordGetterbyCharLen.xletterwords)

wordGetterbyCharLen.wordgetter(5)