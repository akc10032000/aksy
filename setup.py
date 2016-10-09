from distutils.core import setup

config = {'name':           'Asky',
        'version':          'v1.0',
        'description':      'Ask questions and check correctness.',
        'long_description': ('Asky asks questions and checks if the answers '
            'given by the user are correct. Asky must be given two separate '
            'files, one the question file and the other, the answers file. '
            'Answers are in the form of RegEx; if the RegEx matches the user '
            'given answer, the answer is considered correct, otherwise wrong.'
            ),
        'author':           'Abhishek Kumar',
        'author_email':     'akc10032000@gmail.com',
        'scripts':          ['bin/asky'],
        'license':          'GNU GPL version 3 or newer',
}

setup(**config)
