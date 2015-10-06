from string import punctuation
import markovlib
import sylco
import re

def num_of_words(words):
        r = re.compile(r'[{}]'.format(punctuation))
        new_words_cont = r.sub(' ',words)
        wordlen = len(new_words_cont.split())
        return wordlen

def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''
    # to split by multile characters

    sentenceEnders = re.compile('[.!?,]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList


while True:
        print 'Press [l] for love song or [r] for rap-like songs'
        typ = raw_input()
        if typ == 'l' or typ=='r':
                break

if typ == 'l':
        file_ = open('text/combined.txt')
else:
        file_ = open('scraped_data/1a.txt')


while True:
        markov = markovlib.Markov(file_)
        text = markov.generate_markov_text()
        strlen = 0
        sentences = splitParagraphIntoSentences(text)
        for s in sentences:
                senlen = sylco.sylco(s)
                #num_words = num_of_words(s)
                print s.strip().capitalize()
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
                file_ = open('scraped_data/1a.txt')

        print '\n'
