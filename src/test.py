from random import sample, shuffle
import pyphonetics as pp
import sys

sys.path.append('..')
from lib.sentence_generator import generate
from lib.qa_generator import generate_qa

# test sentence generator
# sentences = generate()

# for s in sentences:
#     print(s, '\n')

# test phonetic comparison
# s1 = 'Hannah'
# s2 = 'Ana'
# soundex = pp.RefinedSoundex()

# print(f'{s1}: {soundex.phonetics(s1)}')
# print(f'{s2}: {soundex.phonetics(s2)}')
# print(f'distance: {soundex.distance(s1,s2)}')

# similar = True if soundex.distance(s1,s2) < 2 else False
# print(f'similar: {similar}')

# test full workflow:
sentences = generate()
qa_pairs = []
for sentence in sentences:
    print(sentence.sentence_str)
    qa_pairs += generate_qa(sentence)

shuffle(qa_pairs)
pairs = sample(qa_pairs, k=3)

print('\nQuestions:')
for i, p in enumerate(pairs):
    print(f'{i+1}. {p[0]}')

print('\nAnswers:')
for i, p in enumerate(pairs):
    print(f'{i+1}. {p[1]}')

