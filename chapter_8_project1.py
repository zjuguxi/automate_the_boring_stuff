#! python3
# -*- coding:utf-8 -*-

import random

capitals = {'q1': 'a1', 'q2': 'a2', 'q3': 'a3', 'q4': 'a4'}

for quizNum in range(4):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizFile.write(('  '* 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

for questionNum in range(4):

    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

    for i in range(4):
        quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))

    quizFile.write('\n')

    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()
