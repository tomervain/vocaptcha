import pyphonetics as pp
from fuzzywuzzy import fuzz
import spacy

nlp = spacy.load('en_core_web_sm')
soundex = pp.Metaphone()

def phonetic_dist(s1, s2):
    p1 = soundex.phonetics(s1)
    p2 = soundex.phonetics(s2)
    return soundex.distance(p1, p2, metric='levenshtein')

def textual_dist(s1, s2):
    score = fuzz.ratio(s1, s2)
    return score

def preprocess(s):
    doc = nlp(s)
    words = [t.text for t in doc if not t.is_stop]
    return doc

def main():
    s1 = input('enter s1: ')
    # s2 = input('enter s2: ')
    s1 = preprocess(s1)
    # s2 = preprocess(s2)
    for t in s1:
        print(t.text, t.lemma_, t.pos_, t.tag_)

    # print('phonetic dist:', phonetic_dist(s1, s2))
    # print('textual dist:', textual_dist(s1, s2))
    
if __name__ == "__main__":
    main()
