class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
    
    def vowels(self):
        count = 0 
        for s in self.string:
            if s.lower() in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        if count == 0:
            return '0'
        elif count == 1:
            return '1'
        elif count == 2:
            return '2'
        elif count == 3:
            return '3'
        elif count == 4:
            return '4'
        else:
            return "many"
    
    def bothEnds(self):
        if len(self.string) < 2:
            return ""
        return self.string[0:2] + self.string[-2:]
    
    def fixStart(self):
        if len(self.string) == 0:
            return self.string
        else:
            firstcharacter = self.string[0]
            return firstcharacter + self.string[1:].replace(firstcharacter, "*")
    
    def asciiSum(self):
        return sum(ord(s) for s in self.string)
    
    def cipher(self):
        result = ""
        for letter in self.string:
            if letter.isalpha():
                if letter.islower():
                    result += chr((ord(letter) - 97 + 3) % 26 + 97)
                else:
                    result += chr((ord(letter) - 65 + 3) % 26 + 65)
            else:
                result += letter
        return result
    

        
    
