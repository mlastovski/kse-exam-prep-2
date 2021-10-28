import argparse
import re

# add console arguments to program
parser = argparse.ArgumentParser(description='Process some data.')
parser.add_argument('path', metavar='PATH', type=str, help='Path to the file')
args = parser.parse_args()

path = str(args.path)

file_to_process = open(path, 'r')
lines = file_to_process.readlines()

words = []
for e in lines:
    word = e.split(' ')
    for i in word:
        result = re.sub('[\W_]+', '', i)
        result = result.lower()
        words.append(result)
    
words_new = [item for item in words if item != '']

length_of_chars = [len(item) for item in words_new]

sum_of_chars = 0
for count in length_of_chars:
    sum_of_chars += count
print("Character count is: " + str(sum_of_chars))


length_of_words = len(words_new)
print("There are " + str(length_of_words) + " words in " + path)

count_words = {}

max = 0
max_word = ''
for item in words_new:
    check = count_words.get(item)
    if(check):
        check += 1
        count_words[item] = check
        if(check > max): 
            max = check
            max_word = item
    else:
        count_words[item] = 1


for e in count_words:
    if count_words.get(e) == int(max):
        print("Most used word is ||| " +  str(e) + " ||| " + "(" + str(max) + ' times)')
