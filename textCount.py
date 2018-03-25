class Word:
    def __init__(self, word, repeats):
        self.word = word
        self.repeats = repeats

    
    def __repr__(self):
        return (self.word)


"""sort the words based on number of appearances"""
def bubbleSort(array):
    length = len(array)

    for i in range(length):
        for j in range(0, length-i-1): 
            if array[j].repeats > array[j+1].repeats:
                array[j], array[j+1] = array[j+1], array[j]

def calcPercent(array, count):
    percent = 0
    
    for word in array:
        percent = (word.repeats/count) * 100
        print(word.word + ":\t " + str(word.repeats) + " -\t " + str(percent))

#imports               
import string
import os

# make path specifiable, don't hardcode it!
# get path to the scripts
script_dir = os.path.dirname(__file__)
# save user entered file name
rel_path = input("Enter the name of the file: ")
# join the paths
path = os.path.join(script_dir, rel_path)
#open the file
text_file = open(path, 'r')

#Variables
wordArray = []
temp = str.maketrans('', '', string.punctuation)
wordCount = 0

"read in the text file"
print("Reading the file and counting matches...")
for line in text_file:
    # ignore empty lines
    if line == "\n":
        continue
    
    # remove punctuation
    line = line.translate(temp)

    # change to lowercase
    line = line.lower()

    # split the line into words
    lineArray = line.split()

    # for each word, check if there is a match
    for word in lineArray:
        word = word.translate(temp)
        match = False
        
        # Add to total word count
        wordCount += 1
        
        for i, w in enumerate(wordArray, start=0):
            if word == w.word:
                match = True
                w.repeats += 1
                break
        if match == False:
            wordArray.append(Word(word, 1))
            
text_file.close()

print("Sorting...")
print("Total word count: " + str(wordCount))

#Sort the array
bubbleSort(wordArray)
calcPercent(wordArray, wordCount)
