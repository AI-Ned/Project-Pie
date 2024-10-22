import decimal
import json
from packages.fileController import fileReader


class PiToString:
    pi = 0
    places = 500
    letters = fileReader.jsonFetch("letters","LetterData.json")[0]
    piLetter = []
# A function I stole from the web to calculate pi
    def pi():

        ###
        # Notes
        #-----
        # Taken from https://docs.python.org/3/library/decimal.html#recipes
        ###


        decimal.getcontext().prec += 2  # extra digits for intermediate steps
        three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
        lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
        while s != lasts:
            lasts = s
            n, na = n + na, na + 8
            d, da = d + da, da + 32
            t = (t * n) / d
            s += t
        decimal.getcontext().prec -= 2
        return +s               # unary plus applies the new precision

 # The rule set the decides which letter should be assigned. We look at ever number in a pair, if the number pair is less than 26 we assign a number, otherwise we split the numbers
 # prefix each number with a 0 and treat that as a new pair.
    def numberPairing():
        pi2Str = str(PiToString.pi())
        pairs = 0
        valueA = 0
        valueB = 0
        value = []
        a = 0
        b = 1
        x = 0

        for i in pi2Str[2:]:
            value.append(i)
        while x <= len(value):
            if (b >= len(value)):
                valueA = '0'+value[a]
                PiToString.piLetter.append(PiToString.letters[valueA])
                break 
            elif (a >= len(value)):
                break
            else:
                pairs = value[a]+value[b]
                valueA = '0'+ pairs[0]
                valueB = '0'+ pairs[1]
                if (int(pairs) <= 26 and int(pairs[0])!=0):
                    PiToString.piLetter.append(PiToString.letters[pairs])
                elif (int(pairs) == 00 or int(pairs[0])==0 or int(pairs[1])==0):
                    pairs = ''
                else:
                    PiToString.piLetter.append(PiToString.letters[valueA])
                    PiToString.piLetter.append(PiToString.letters[valueB])
            
            x = x + 1
            a = a + 2
            b = b + 2

#Return the final result of the class.
    def encode():
        PiToString.numberPairing()
        output = ''
        for i in PiToString.piLetter:
            output = output+i

        #print(output)
        return output    


    decimal.getcontext().prec = places


