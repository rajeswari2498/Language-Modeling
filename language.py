"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    text=open(filename)
    list=[]
    read=text.read().splitlines()
    for sentence in read:
        if len(sentence)>0:
            list.append(sentence.split(" "))
            # print(list)
    return list

'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    length=0
    for sentence in corpus:
        for sentences in sentence:
            length=length+1
    return length


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    new_list=[]
    for sentence in corpus:
        for combined in sentence:
            if combined not in new_list:
                new_list.append(combined)
    # print(new_list)
    return new_list


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    dictionary={}
    for sentence in corpus:
        for word in sentence:
            if word not in dictionary:
                dictionary[word]=0
            dictionary[word]+=1
    # print(dictionary)
    return dictionary


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    list=[]
    for each in corpus:
        for word in each:
            if each[0] not in list:
                list.append(each[0])
    # print(list)
    return list


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    dictionary={}
    for sentence in corpus:
        for word in sentence:
            if sentence[0] not in dictionary:
                dictionary[sentence[0]]=0
        dictionary[sentence[0]]+=1
    # print(dictionary)
    return dictionary


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    new_dictionary={}
    for each in corpus:
        for i in range(len(each)-1):
            word1=each[i]
            word2=each[i+1]
            if word1 not in new_dictionary:
                new_dictionary[word1]={}
                if word2 not in new_dictionary[word1]:
                    new_dictionary[word1][word2]=1
                else:
                    new_dictionary[word1][word2]+=1
            else:
                if word2 not in new_dictionary[word1]:
                    new_dictionary[word1][word2]=1
                else:
                    new_dictionary[word1][word2]+=1 
    # print(new_dictionary) 
    return new_dictionary


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    list=[]
    n=len(unigrams)
    for value in unigrams:
            probability=1/n
            list.append(probability)
    # print(list)
    return list


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    empty_list=[]
    total=0
    for index in unigrams:
        total=unigramCounts[index]/totalCount
        empty_list.append(total)
    # print(empty_list)
    return empty_list


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    new_dictionary={}
    for prevWord in bigramCounts:
        key_list=[]
        probability_list=[]
        for keys in bigramCounts[prevWord]:
                key_list.append(keys)
                probability_list.append(bigramCounts[prevWord][keys]/unigramCounts[prevWord])
                dictionary={}
                dictionary["words"]=key_list
                dictionary["probs"]=probability_list
                new_dictionary[prevWord]=dictionary
    # print(new_dictionary)
    return new_dictionary

'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    dictionary={}
    empty_dictionary={}
    for i in range(len(words)):
        if words[i] not in dictionary and words[i] not in ignoreList:
            dictionary[words[i]]=probs[i]
    sorted_order=sorted(dictionary,key=dictionary.get,reverse=True)
    for i in sorted_order:
        if len(empty_dictionary)<count:
            empty_dictionary[i]=dictionary[i]
    # print(empty_dictionary)
    return empty_dictionary


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    return


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    return


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    return


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    return


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    return


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testLoadBook()
    test.testGetCorpusLength()
    test.testBuildVocabulary()
    test.testCountUnigrams()
    test.testGetStartWords()
    test.testCountStartWords()
    test.testCountBigrams()
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    test.runWeek1()

    test.testBuildUniformProbs()
    test.testBuildUnigramProbs()
    test.testBuildBigramProbs()
    test.testGetTopWords()
#     ## Uncomment these for Week 2 ##
# """
#     print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
#     test.week2Tests()
#     print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
#     test.runWeek2()
# """

#     ## Uncomment these for Week 3 ##
# """
#     print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
#     test.runWeek3()
# """