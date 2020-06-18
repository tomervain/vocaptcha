class Sentence():
    """Sentence object used for TTS and QA-Generator modules"""
    def __init__(self, sType, sentence):
        self.type = sType
        self.attributes = dict()
        self.sentence_exp = sentence
        self.sentence_str = ' '.join(sentence)

        # parse data from sentence
        parser = parsers[self.type]
        parser(self.attributes, self.sentence_exp)
    
    def __str__(self):
        string = f'{self.type}: "{self.sentence_str}"\n'
        string += 'Attributes:\n'
        for att in self.attributes.items():
            string += f'{att[0]}: {att[1]}\n'
        return string
        


# Parser functions and callback dictionary

def s1_parser(attributes, sentence):
    attributes['entity'] = sentence[0]
    attributes['feel'] = sentence[1].split(' ')[0][:-1]
    attributes['verb'] = sentence[2]
    attributes['obj'] = sentence[3]

def s2_parser(attributes, sentence):
    entity = ' '.join(sentence[6:8]) if sentence[6] == 'my' else sentence[6]
    attributes['entity'] = entity
    loc = ' '.join(sentence[-2::]) if sentence[-2] == 'the' else sentence[-1]
    attributes['location'] = loc

def s3_parser(attributes, sentence):
    if sentence[0] == 'my':
        attributes['entity'] = ' '.join(sentence[:2])
        attributes['posses'] = sentence[2]
    else:
        attributes['entity'] = sentence[0]
        attributes['posses'] = sentence[1]

    attributes['adverb'] = sentence[-2]
    attributes['obj'] = sentence[-1]

def s4_parser(attributes, sentence):
    attributes['entity'] = sentence[0]
    attributes['animal'] = sentence[3]
    attributes['prep'] = sentence[4]
    attributes['location'] = sentence[-1]

def s5_parser(attributes, sentence):
    attributes['entity'] = sentence[0][:-2]
    attributes['topic'] = sentence[2]
    attributes['noun'] = sentence[-1]

parsers = {
    'S1': s1_parser,
    'S2': s2_parser,
    'S3': s3_parser,
    'S4': s4_parser,
    'S5': s5_parser
}
