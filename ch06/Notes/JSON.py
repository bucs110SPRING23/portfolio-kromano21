#Programs cannot directly talk to one another for security reasons. If program1 writes out file, how does program2 know how to read the file?
#In other words, in order to read data from a file, you have to know the string format of the data (conventions)

#String formats allow programs to understand data between them 
#Use standardized string formats to transfer data between programs. 
#Often, the formmatted string is saved to a file, and the other programs reads the file. 
#Some string format examples:
#csv - comma seperated values for creating a spreadsheet
#html - tree structured text to layout the content of a web page
#JSON - standard data object exchange format 

#JSON (JavaScript Object Notation)
#relatively easy for humans to read and write
#Easy for most programming languages to parse and generate
#You can store one dictionary or list in a JSON formatted string 

{
    name: "ABC"
}

#You can store any valid object in that list or dictionary
{
  person: {
    name: "The Tick",
    superpower: "Nigh Invulnerable",
    aquaintences: [
      "Arthur",
      "American Maid",
      "Die Fledermaus"
    ]
  }
}

#2 symbols
#[] - Lists
#{} - Dictionaires 

#Valid Data Types:
#int, float
#str,
#bool
#None

#You can take any JSON formatted str and convert is to  list or dictionary or vice versa
data = """
  {
  "num": 1
        "letter":"a"
  }
"""
json2python = json.loads(data)
print(json2python, type(json2python))

dictionary2json =json.dumps(json2Python)
print(dictionary2json, type(dictionary2json))

#JSON in a File 
#If your string is stored in a file, you must open the file for reading 
fptr = open(“mydata.json”)
json2python = json.loads(fptr.read())
#You can skip reading the file 
fptr = open(“mydata.json”)
json2python = json.load(fptr) #(no s)
#Like for writing JSON to a file:
fptr = open(“mydata.json”, 'w')
nums = [1,2,3]
list2json = json.dump(nums, fptr)

#How to use JSON 
#1. Convert objects to strings, and write them out to a file:
#save the program state
#2. Send file to another program 
#Transfer data between programs 
#3. Send data over a network to another computer
#How the modern web works 
