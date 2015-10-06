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

print 'Press [l] for love song or [r] for rap-like rhymes'
typ = raw_input()

# here, the typ variable essentially defines what training data to use.
if typ == 'l':
        file_ = open('text/combined.txt')
else:
        file_ = open('text/1a.txt')

# generate poem based on files specified
while True:
        markov = markovlib.Markov(file_)
        text = markov.generate_markov_text()
        strlen = 0
        sentences = splitParagraphIntoSentences(text)
        for s in sentences:
                senlen = sylco.sylco(s)
                print(s.strip().capitalize())
                '''
                if(senlen <10):
                        print s.strip().capitalize()
                else:
                        print "          [" + s.strip().capitalize() + "]"
                '''
        print '\n'
        print 'Press [l] for love song or any key for rap songs'
        typ = raw_input()

        if typ == 'l':
                file_ = open('text/combined.txt')
        else:
                file_ = open('text/1a.txt')

        print '\n'
