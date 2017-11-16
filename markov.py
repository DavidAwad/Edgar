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


def selection_text():
    # read appropriate training data based on specified file
    print('\nPress [l] for love songs \n[b] for' +
          ' blues \n[r] for rap-like rhymes\n[t] for trump speeches')
    c = raw_input()

    # here, the c variable essentially defines what training data to use.
    if c == 'l':
            file_ = open('text/combined.txt')
    elif c == 'b':
            file_ = open('text/blues_combined')
    elif c == 't':
            file_ = open('text/speeches.txt')
    else:
            file_ = open('text/1a.txt')
    return file_.read().split()


def generate_poem(data):
    # generates a weighted markov graph based on frequency of words
    # succeeding each other in training data
    markov = markovlib.Markov(data)
    text = markov.generate_markov_text()
    strlen = 0
    sentences = splitParagraphIntoSentences(text)
    out_poem = ''
    for s in sentences:
            # TODO senlen = sylco.sylco(s)
            out_poem += s.strip().capitalize()
            out_poem += '\n'
    return out_poem


while True:
    print(generate_poem(selection_text()))
