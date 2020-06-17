import sys
from random import sample, shuffle

sys.path.append('..')

from lib.qa_generator import generate_qa
from lib.sentence_generator import generate


def main():
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

if __name__ == "__main__":
    main()
