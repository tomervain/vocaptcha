from random import sample, shuffle
from fuzzywuzzy import fuzz
import pyphonetics as pp
import sys

sys.path.append('..')
from lib.sentence_generator import generate
from lib.qa_generator import generate_qa

# test sentence generator
# sentences = generate()

# for s in sentences:
#     print(s, '\n')

# test full workflow:
# sentences = generate()
# qa_pairs = []
# for sentence in sentences:
#     print(sentence.sentence_str)
#     qa_pairs += generate_qa(sentence)

# shuffle(qa_pairs)
# pairs = sample(qa_pairs, k=3)

# print('\nQuestions:')
# for i, p in enumerate(pairs):
#     print(f'{i+1}. {p[0]}')

# print('\nAnswers:')
# for i, p in enumerate(pairs):
#     print(f'{i+1}. {p[1]}')


# test phonetic comparison
def phonetic_form(s, soundex):
    phon = []
    s_words = s.split(' ')
    for w in s_words:
        phon.append(soundex.phonetics(w))
    
    return ' '.join(phon)

def compare(s1, s2, soundex):
    ratio = soundex.distance(s1,s2)
    return (ratio, True) if ratio < 2 else (ratio, False)

s1 = 'Glue'
s2 = 'Wall'
soundex = pp.Soundex()

s1_p = phonetic_form(s1, soundex)
s2_p = phonetic_form(s2, soundex)
print(f'{s1}: {s1_p}')
print(f'{s2}: {s2_p}')

ratio, similar = compare(s1_p, s2_p, soundex)
print(f'distance: {ratio}')
print(f'similar: {similar}')
