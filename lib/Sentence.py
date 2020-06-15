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
    entity = sentence[7] if sentence[6] == 'my' else sentence[6]
    attributes['entity'] = entity
    attributes['location'] = sentence[-1]


def s3_parser(attributes, sentence):
    e_idx = 1 if sentence[0] == 'my' else 0
    attributes['entity'] = sentence[e_idx]
    attributes['posses'] = sentence[e_idx + 1]
    attributes['adverb'] = sentence[-2]
    attributes['obj'] = sentence[-1]

parsers = {
    'S1': s1_parser,
    'S2': s2_parser,
    'S3': s3_parser
}
