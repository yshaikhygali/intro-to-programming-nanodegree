from random import shuffle

qas = [
    ('How many beats are there per measure in 2/4 time?', '2'),
    ('In what family of instruments is the piano?', 'percussion'),
    ('How many strings does a violin have?', '4')
]

shuffle(qas)
numRight = 0

for question, rightAnswer in qas:
    answer = input(question + ' ')
    if answer == rightAnswer:
        print('Right!')
        numRight += 1
    else:
        print('No, the answer is ' + rightAnswer)

print('You got {} right and {} wrong'.format(numRight, len(qas) - numRight))
