from lib.Sentence import Sentence
from lib.sentence_generator import terminals
from random import choice

def generate_qa(sentence: Sentence):
    parser = qa_parsers[sentence.type]
    return parser(sentence.attributes)

def qa_parser_s1(attributes):
    entity = attributes['entity']
    feel = attributes['feel']
    verb = attributes['verb']
    obj = attributes['obj']
    qa_pairs = []
    qa_pairs.append((f'What does {entity} {feel} to {verb}?', obj))
    qa_pairs.append((f'Who {feel}s to {verb} {obj}?', entity))
    return qa_pairs

def qa_parser_s2(attributes):
    entity = attributes['entity']
    location = attributes['location']
    qa_pairs = []
    qa_pairs.append((f'Who went with me on a trip to {location}?', entity))
    qa_pairs.append((f'Where did i go on a trip with {entity}?', location))
    return qa_pairs

def qa_parser_s3(attributes):
    ps = { 'got': 'got', 'has': 'have', 'owns': 'own' }
    entity = attributes['entity']
    posses = attributes['posses']
    adverb = attributes['adverb']
    obj = attributes['obj']
    det = 'an' if adverb in 'aeiou' else 'a'
    qa_pairs = []
    qa_pairs.append((f'What does {entity} {ps[posses]} that is {adverb}?', obj))
    qa_pairs.append((f'Who {posses} {det} {adverb} {obj}?', entity))
    qa_pairs.append((f'What is known about {entity}\'s {obj}?', adverb))
    return qa_pairs

qa_parsers = {
    'S1': qa_parser_s1,
    'S2': qa_parser_s2,
    'S3': qa_parser_s3
}
