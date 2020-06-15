from pyphonetics import *
import sys

sys.path.append('..')
from lib.sentence_generator import generate

# test sentence generator
sentences = generate()

for s in sentences:
    print(s, '\n')

# test phonetic comparison
# s1 = 'Dog'
# s2 = 'Dogs'
# soundex = RefinedSoundex()

# print(f'{s1}: {soundex.phonetics(s1)}')
# print(f'{s2}: {soundex.phonetics(s2)}')
# print(f'distance: {soundex.distance(s1,s2)}')

# similar = True if soundex.distance(s1,s2) < 3 else False
# print(f'similar: {similar}')
