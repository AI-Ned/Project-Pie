import json

class JsonFileControl:
    
    def jsonFetch(target, filename):
        
        file = open(filename, "r", encoding="utf8")
        data = json.load(file)
        dataset = []

        for i in data[target]:
            dataset.append(i)
        
        file.close
       
        return dataset
    
    def jsonWrite(data, filename):

        if(data.find("'")):
            data = data.replace("'", '"')
         

        file = open(filename, "w", encoding="utf8")
        file.write(data)
        file.close

class TextFileControl:

    def txtFetch(filename):

        file = open(filename,  "r", encoding="utf8")
        data = file.read()
        file.close
        return data
    
    def txtLinetoArray(filename):

        file = open(filename,  "r", encoding="utf8")
        lines = file.readlines()
        data = []
        for line in lines:
            line = line.replace("\n", "").replace("\r", "")           
            data.append(line)


        file.close
        return data



 