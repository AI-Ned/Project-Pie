import json

class fileControl:
    
    def jsonFetch(target, filename):
        
        file = open(filename, "r")
        data = json.load(file)
        dataset = []

        for i in data[target]:
            dataset.append(i)
        
        file.close
       
        return dataset
    
    def jsonWrite(data, filename):

        if(data.find("'")):
            data = data.replace("'", '"')
         
        print(data[:300])
        file = open(filename, "w")
        file.write(data)
        file.close

 