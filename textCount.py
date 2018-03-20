class Word:
    def __init__(self, word, repeats):
        self.word = word
        self.repeats = repeats

    
    def __repr__(self):
        return (self.word)



import string
import os

# make path specifiable, don't hardcode it !!!!!!!
#path = '/Users/jessicakarpovich/Desktop/text.txt'

script_dir = os.path.dirname(__file__)
rel_path = "text.txt"
path = os.path.join(script_dir, rel_path)

wordArray = []

text_file = open(path, 'r')

temp = str.maketrans('', '', string.punctuation)

"read in the text file"
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
        match = False

        
        for i, w in enumerate(wordArray, start=0):
            if word == w.word:
                match = True
                w.repeats += 1
                break
        if match == False:
            wordArray.append(Word(word, 1))

"""sort the words based on number of appearances"""
for num in range(len(wordArray)-1, 0, -1):
    for i in range(num):
        if wordArray[i+1].repeats > wordArray[i].repeats:
            temp = wordArray[i]
            wordArray[i] = wordArray[i+1]
            wordArray[i+1] = temp

print(wordArray)
text_file.close()
