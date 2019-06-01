import math
import random
import sys
words = []
scores = []
correct_word = list(input('word or phrase: '))
while True:
  try:
    mutation_rate = float(input('Mutation Rate: '))
    break
  except:
    print('Please return a number')
while True:
  try:
    start_pop = int(input('What would you like the population to be?: '))
    break
  except:
    print('Please return a whole number.')
for i in range(start_pop):
  word = []
  for i in range(len(correct_word)):
    word.append(chr(random.randint(32, 126)))
  words.append(word)
keeps = []
gen = 0
while True:
  gen += 1
  if words[-1] == correct_word:
    print('words: {}'.format(''.join(words[-1])))
    sys.exit()
  scores = []
  for i in range(len(words)):
    ls = []
    ls.append(0)
    ls.append(i)
    scores.append(ls)
  for i in range(len(words)):
    for x in range(len(correct_word)):
      if words[i][x] == correct_word[x]:
        scores[i][0] = scores[i][0] + 1
  scores.sort(reverse = True)
  words_to_keep = len(words) / 2
  words_to_keep = math.floor(words_to_keep)
  if words_to_keep % 2 != 0:
    words_to_keep -= 1
  keeps = []
  for i in range(words_to_keep):
    keeps.append(words[scores[i][1]])
  closest_word = ''.join(words[scores[0][1]])
  print('closest word: {}, gen: {}'.format(closest_word, gen))
  words = []
  for i in range(2):
    for i in range(len(keeps)):
      word = []
      for b in range(len(correct_word)):
        if random.randint(0, 1000000000) / 10000000 <= mutation_rate:
          mutation = random.randint(-1, 1)
        else:
          mutation = 0
        try:
          if random.randint(0, 1) == 1:
            word.append(chr(ord(keeps[i][b]) + mutation))
          else:
            word.append(chr(ord(keeps[-i][b]) + mutation))
        except:
          del word
          break
      try:
        words.append(word)
      except:
        l = 0
  for i in range(len(words)):
    if words[i] == correct_word:
      print('closest word: {}, gen: {}'.format(''.join(correct_word), gen))
      print('Found! That took {} generations with a {}% mutation rate!'.format(gen, mutation_rate))
      sys.exit()

