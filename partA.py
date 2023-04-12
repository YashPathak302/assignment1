import re
import sys
filename = sys.argv[1]

# Method/Function: List<Token> tokenize(TextFilePath)
# Write a method/function that reads in a text file and returns a list of the tokens in that file.
# For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization
# (so Apple, apple, aPpLe are the same token). You are allowed to use regular expressions if you wish to
# (and you can use some regexp engine, no need to write it from scratch), but you are not allowed to import a tokenizer
# (e.g. from NLTK), since you are being asked to write a tokenizer.


def tokenize(filepath) -> list:
    tokenList = []
    with open(filepath) as file:
        for line in file:
            lineList = re.split('[^a-zA-Z0-9]+', line.lower())[:-1]
            for word in lineList:
                tokenList.append(word.rstrip(".").rstrip(","))
    return tokenList

# Method/Function:        Map<Token,Count> computeWordFrequencies(List<Token>)
# Write another method/function that counts the number of occurrences of each token in the token list.
# Remember that you should write this assignment yourself from scratch, so you are not allowed to import
# a counter when the assignment asks you to write that method.


def computeWordFrequenceies(tokenList) -> dict:
    tokenDict = {}
    for token in tokenList:
        if token not in tokenDict:
            if token != "":
                tokenDict[token] = 1
        else:
            tokenDict[token] += 1
    return tokenDict

# Method/Function:         void print(Frequencies<Token, Count>)
# Finally, write a method/function that prints out the word frequency count onto the screen.
# The printout should be ordered by decreasing frequency (so, the highest frequency words first; if necessary, order the cases of ties alphabetically).


def printer(tokenDict) -> None:
    for token, tokenFrequency in tokenDict.items():
        print(token, "->", tokenFrequency)

# self function to write output to a file
# the writer function creates a new file, as the vs code terminal was not enough
# to handle all the numerous lines for extremely large inputs


def writer(tokenDict):
    file_object = open("output.txt", 'w')
    for token, tokenFrequency in tokenDict.items():
        keyValueString = f"{token} -> {tokenFrequency}" + '\n'
        file_object.write(keyValueString)
    file_object.close()


def main():
    # create a list of tokens
    lst = tokenize(filename)
    # create a hashmap/dictionary of words mapping to the frequency of the words
    dct = computeWordFrequenceies(lst)

    # create a file to check the output, works similar to the printer function in terms of representing output
    # writer(dct)

    # print the dictionary in one of the many forms of representation
    printer(dct)


if __name__ == "__main__":
    main()
