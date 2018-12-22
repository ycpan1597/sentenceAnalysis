#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 09:37:02 2018

@author: preston
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import re

titles = ['Dr', 'Prof', 'Mr', 'Mrs', 'Ms', 'Sr', 'Jr', 'Rev', 'St']
t = '('
for item in titles:
    t += item + ')('
t = t[:-1]
    
class wordAnalysis:
    
    def __init__(self, fileName, location = 'sampleFiles/'):
        self.fileName = fileName
        self.raw = self.readFile(fileName, location)
        self.wordsInSen, self.sen, self.avg, self.std = self.findwordsInSen(self.raw)
        
        plt.figure()
        plt.hist(self.wordsInSen, bins = np.arange(0, 35, 1))
        plt.title(fileName + ' (total = ' + str(len(self.sen)) + ' sentences)')
        plt.axvline(x = self.avg, label = 'Avg = ' + str(self.avg) + ', Std = ' + str(self.std), color = 'k')
        plt.axvline(x = self.avg + self.std, color = 'k', ls = '--')
        plt.axvline(x = self.avg - self.std, color = 'k', ls = '--')
#        plt.axvline(x = 20, label = 'too many words!', color = 'r', ls = '--')
#        plt.axvline(x = 4, label = 'too few words!', color = 'r', ls = '--')
        plt.legend()
        
    def readFile(self, fileName, location):
        with open(location + fileName, 'r') as f:
            x = f.readlines()
        return x
    
    def findwordsInSen(self, content, threshLow = 3):
        wordsInSen = [] #number of words in each sentence
        sen = []
        for oneP in content:
            oneP = oneP.replace('\t', '')
            oneP = oneP.rstrip()
#            I might want to use re.findall instead of split to retain the end-of-sentence punctuation
#            allS = re.split(r'(?:(?<!Dr)(?<!Prof)(?<!Sr)(?<!Jr)(?<!Mr)(?<!Mrs)(?<!Ms))[?.!]\"?\s(?=\w)', oneP)
            allS = re.split(r'(?:(?<!Dr)(?<!Prof)(?<!Sr)(?<!Jr)(?<!Mr)(?<!Mrs)(?<!Ms)[?.!]\"?)\s\"*(?=\w)', oneP)
#            allS = re.findall('.*?[?.!]', oneP) #most intuitive but too simple
            for oneS in allS:
#                curLength = len(oneS.split(' '))
                curLength = len(re.split(r'\s+', oneS))
                wordsInSen.append(curLength)
                sen.append(oneS)
            for index, item in enumerate(sen):
                if item == '':
                    del sen[index]
                    del wordsInSen[index]
        return wordsInSen, sen, round(sum(wordsInSen)/len(sen), 2), round(np.std(wordsInSen), 2)
    
    """
    current issue: 
        1) Sentence fragments (without a period at the end) should be ignored
        2) Date - Nov. 13 is cut into two separate phrases
        3 - 1) Quotation mark: ". . . sentence finishes." new sentence --> Currently treated as one
        3 - 2) Quotation mark: sentence finishes. "New sentence. . . " --> currently treated as one too
    """
    
    
    def printSentencesUnder(self, thresh = 3): 
        for index, item in enumerate(self.wordsInSen):
            if item <= thresh:
                print(self.sen[index])
plt.close('all')
#reads all files in a directory and returns a dictionary of wordAnalysis objects
def readAll(location = 'sampleFiles'):
    fileDic = {}
    for oneFileName in os.listdir(location):
#        print(oneFileName)
        fileDic[oneFileName] = wordAnalysis(oneFileName)
    return fileDic

#dic = readAll()
pp2 = wordAnalysis('pp(2).txt')
sample105 = wordAnalysis('sample105.txt')
sample104 = wordAnalysis('sample104.txt')
test = wordAnalysis('testfile.txt')
print(test.sen)




        