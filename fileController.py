import json

class fileReader:
    
    def jsonFetch(target, filename):
        
        file = open(filename)
        data = json.load(file)
        dataset = []

        for i in data[target]:
            dataset.append(i)
       
        return dataset