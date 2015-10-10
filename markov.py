from string import punctuation
import markovlib
import sylco
import re


def splitParagraphIntoSentences(paragraph):
    '''
    break a paragraph into sentences
    and return a list
    '''
    sentenceEnders = re.compile('[.!?,]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList


def in_pointer():
    print('\nPress [l] for love songs \n[b] for' +
          ' blues \n[r] for rap-like rhymes\n')
    c = raw_input()

    # here, the c variable essentially defines what training data to use.
    if c == 'l':
            file_ = open('text/combined.txt')
    elif c == 'b':
            file_ = open('text/blues_combined')
    else:
            file_ = open('text/1a.txt')

    return file_.read().split()

# reads file into memory instead of passing it around internal to the object
file_ = in_pointer()

# generate poem based on files specified
while True:
        # generates a weighted markov graph based on frequency of words
        # succeeding each other in training data
        file_ = in_pointer()
        markov = markovlib.Markov(file_)
        text = markov.generate_markov_text()
        strlen = 0
        sentences = splitParagraphIntoSentences(text)
        for s in sentences:
                print(s)
                # senlen = sylco.sylco(s)
                # print(s.strip().capitalize())
                '''
                if(senlen <10):
                        print s.strip().capitalize()
                else:
                        print "          [" + s.strip().capitalize() + "]"
                '''
