#!/usr/bin/env python
# coding: utf-8

# In[55]:


import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy
from more_itertools import split_after
import itertools
from itertools import groupby

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

filepath = './Introduce.mp3'
y, sr = librosa.load(filepath)
plt.figure()
plt.subplot(3, 1, 1)
librosa.display.waveplot(y, sr=sr)
plt.title('Monophonic')
print(y)
print(numpy.where(y == 0)[0])
print(numpy.where(y != 0)[0])
split_at = 0
newList = [list(g) for k, g in groupby(y, lambda x: x != split_at) if k]
morse = []
for i in range(len(newList)):
    morse.append(len(newList[i]))

morse_mean = numpy.mean(morse)

for i in range(len(morse)):
    if morse[i]>morse_mean:
        morse[i] = "-"
    else:
        morse[i] = "."
print(morse)


newList_2 = [list(g) for k, g in groupby(y, lambda x: x == 0) if k]
morse_empty = []
for i in range(len(newList_2)):
    morse_empty.append(len(newList_2[i]))

morse_empty_mean = numpy.mean(morse_empty)

for i in range(len(morse_empty)):
    if morse_empty[i]>morse_empty_mean:
        morse_empty[i] = "="
    else:
        morse_empty[i] = ","
print(morse_empty)

idx = []
for i in range(len(morse_empty)):
    if morse_empty[i] == "=":
        idx.append(i)
print(idx)

increment = len(idx)

while increment>0:
    idx[increment-1]+=increment
    increment-=1

for i in range(len(idx)):
    morse.insert(idx[i]," ")
    
print(morse)
message = "".join(morse)


def decrypt(message): 
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0  
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
    return decipher 
result = decrypt(message) 

print(result)


# In[ ]:




