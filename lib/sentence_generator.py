import json
from random import choice, choices

from lib.grammar import grammar
from lib.Sentence import Sentence

# open terminals data for sentence generator
with open('../lib/data.json', 'rb') as f:
    data = json.load(f)

terminals = data['terminal']


def extract(t):
    """Extract terminal keys from brackets"""
    ob = t.find('<')
    cb = t.find('>')
    return t[ob+1:cb]


def start_parse(s):
    """Starter function for Recursive Descent Parser"""
    exp = []
    for i in grammar[s]:
        expand(i, exp)

    return (s, exp)


def expand(pick, exp):
    """Recursive Descent variable expend function"""
    if isinstance(pick, list):
        for i in pick:
            expand(i, exp)
    elif pick in grammar:
        pick = choice(grammar[pick])
        expand(pick, exp)
    else:
        exp.append(pick)


def fill_terminals(sentence):
    """Replaces terminal variables with random data"""
    k = sentence[0]
    s = sentence[1]

    exp = []
    for w in s:
        if w[0] == '<':
            key = terminals[extract(w)]
            exp.append(choice(key))
        else:
            exp.append(w)

    if k == 'S3' and exp[-2][0] in 'aeiou':
        det_idx = exp.index('a')
        exp[det_idx] = 'an'
    
    if k == 'S4' and exp[3][0] in 'AEIOU':
        det_idx = exp.index('a')
        exp[det_idx] = 'an'

    return (k, exp)


def generate(k=3):
    """Generates list of k Sentences (3 by default)"""
    start = choices(grammar['S'], k=k)
    sentences = []
    for s in start:
        sentences.append(start_parse(s))

    # fill all data and return list of complete sentences
    sentences = [fill_terminals(s) for s in sentences]

    # generate and return list of Sentences objects:
    return [Sentence(s[0], s[1]) for s in sentences]
