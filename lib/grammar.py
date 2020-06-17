grammar = {
    'S': ['S1', 'S2', 'S3', 'S4'],
    'S1': ['<name>', 'FEEL'],
    'S2': ['i', 'went', 'on', 'a', 'trip', 'with', 'PERSON', 'to', 'LOCATION'],
    'S3': ['PERSON', 'POSSES', 'a', 'NN_ADV'],
    'S4': ['<name>', 'saw', 'a', 'ANIMAL_LOCATION'],
    'FEEL': [
        ['likes to', 'VB_POS'],
        ['loves to', 'VB_POS'],
        ['hates to', 'VB_NEG'],
    ],
    'VB_POS': [
        ['play', 'VB_NN_PLAY'],
        ['eat', 'VB_NN_EAT'],
        ['drink', 'VB_NN_DRINK'],
        ['cook', 'VB_NN_COOK'],
        ['write', 'VB_NN_WRITE'],
        ['read', 'VB_NN_READ'],
        ['tell', 'VB_NN_TELL'],
        ['collect', 'VB_NN_COLLECT'],
        ['watch', 'VB_NN_WATCH'],
        ['bake', 'VB_NN_BAKE'],
        ['study', 'VB_NN_STUDY']
    ],
    'VB_NEG': [
        ['study', 'VB_NN_STUDY'],
        ['eat', 'VB_NN_EAT'],
        ['drink', 'VB_NN_DRINK'],
        ['clean', 'VB_NN_CLEAN'],
    ],
    'VB_NN_PLAY': [
        ['the <instrument_musical>'],
        ['<game_video>'],
        ['<game_sport>'],
        ['<game_board>'],
        ['<game_card>']
    ],
    'VB_NN_EAT': [
        ['<food_cooking>'],
        ['<food_groups>'],
        ['<food_baking>'],
    ],
    'VB_NN_DRINK': [
        ['<drink_soft>'],
        ['<drink_alcohol>'],
    ],
    'VB_NN_COOK': [['<food_cooking>']],
    'VB_NN_WRITE': [['<content_written>']],
    'VB_NN_READ': [['<content_readed>']],
    'VB_NN_TELL': [['<content_spoken>']],
    'VB_NN_COLLECT': [['<collectable>']],
    'VB_NN_WATCH': [
        ['televison'],
        ['<game_sport> games'],
        ['plays'],
        ['movies']
    ],
    'VB_NN_BAKE': [['<food_baking>']],
    'VB_NN_STUDY': [['<study>']],
    'VB_NN_CLEAN': [
        ['the furnitures'],
        ['the floor'],
        ['the bathroom'],
        ['the kitchen']
    ],
    'PERSON': [['<name>'], ['my', 'RELATIVE']],
    'RELATIVE': [
        'father',
        'mother',
        'sister',
        'brother',
        'grandfather',
        'grandmother',
        'uncle',
        'aunt',
        'cousin',
        'best friend',
        'friend',
        'husband',
        'wife'
    ],
    'LOCATION': [['<location_named>'], ['the', '<location_touring>']],
    'POSSES': ['has', 'owns', 'got'],
    'NN_ADV': [
        ['NN_ADV_PET', '<animal_pet>'],
        ['NN_ADV_STRUCTURE', '<structure>'],
        ['NN_ADV_VEHICLE', '<vehicle>'],
        ['NN_ADV_IHOUSEHOLD', '<item_household>'],
        ['NN_ADV_IFABRIC', '<item_fabric>'],
        ['NN_ADV_IJEWELRY', '<item_jewelry>'],
    ],
    'NN_ADV_PET': [
        'cute',
        'big',
        'tiny',
        'small',
        'young',
        'old',
        'smart',
        'dumb',
        'silly',
        'shy',
        'playful'
    ],
    'NN_ADV_STRUCTURE': [
        'new',
        'small',
        'big',
        'beautiful',
        'ugly'
    ],
    'NN_ADV_VEHICLE': [
        'fast',
        'old',
        'new',
        'beautiful',
        '<color>',
        'expensive',
        'cheap'
    ],
    'NN_ADV_IHOUSEHOLD': [
        'new',
        'old',
        'expensive',
        'cheap',
        'big',
        'small'
    ],
    'NN_ADV_IFABRIC': [
        '<color>',
        'decorated',
        'plain',
        'new',
        'old'
    ],
    'NN_ADV_IJEWELRY': [
        'luxurious',
        'simple',
        'expensive',
        'cheap',
        'shiny',
        'golden',
        'silver'
    ],
    'ANIMAL_LOCATION': [
        ['<animal_wild>', 'at', 'the', 'WILD_ANIMAL_LOC'],
        ['<animal_water>', 'in', 'the', 'WATER_ANIMAL_LOC'],
        ['<animal_jungle>', 'in', 'the', 'jungle'],
        ['<animal_forest>', 'in', 'the', 'forest'],
        ['<animal_safari>', 'at', 'the', 'safari'],
        ['<animal_farm>', 'at', 'the', 'farm']
    ],
    'WILD_ANIMAL_LOC': [
        'zoo',
	    'natural reserve',
	    'wildlife refuge',
	    'wildlife sanctuary'
    ],
    'WATER_ANIMAL_LOC': [
        'aquarium',
	    'oceanarium',
	    'ocean'
    ]
}
