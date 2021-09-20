import nltk
import re
training = []

with open('WSJ_02-21.pos-chunk') as f:
    for line in f:
        sen = nltk.word_tokenize(line)
        if line in ['\n', '\r\n']:
            #print('')
            training.append("")
            prev_pos = ""
        else:
            word = sen[0]
            pos = sen[1]
            bio = sen[2]
            final = word + "\t" + "pos=" + pos + '\t' + "prev_pos=" + prev_pos + "\t" + bio
            training.append(final)
            prev_pos = pos
f = open("training.feature", "a")
for i in training:
    f.write(i + "\n")
f.close()

testing = []
with open('WSJ_23.pos') as f:
    for line in f:
        sen = nltk.word_tokenize(line)
        if line in ['\n', '\r\n']:
            #print('')
            testing.append("")
            prev_pos = ""
        else:
            word = sen[0]
            pos = sen[1]
            final = word + "\t" + "pos=" + pos + '\t' + "prev_pos=" + prev_pos
            testing.append(final)
            prev_pos = pos

f = open("test.feature", "a")
for i in testing:
    f.write(i + "\n")
f.close()