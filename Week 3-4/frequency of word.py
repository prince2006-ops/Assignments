# checking the frequency of the word in a sentence
def word_frequency(sentence):
    words=sentence.split() # making sentence to list
    frequency={}
    for word in words: #iterating the list  words
        if word in frequency:
            frequency[word] += 1 # checking the word in list
        else:
            frequency[word] = 1
    return frequency
sentence_input=input("Enter the sentence")
print(word_frequency(sentence_input))
