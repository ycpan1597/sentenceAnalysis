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

class wordAnalysis:
    def __init__(self, fileName, location = 'sample files/'):
        self.fileName = fileName
        self.content = self.readFile(fileName, location)
        self.wordsInSent, self.longSentences, self.avg, self.std = self.findWordsInSent(self.content)
        
        plt.figure()
        plt.hist(self.wordsInSent, bins = np.arange(0, 35, 1))
        plt.title(fileName + ' (total = ' + str(len(self.longSentences)) + ' sentences)')
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
    
    def findWordsInSent(self, content, threshLow = 3):
        wordsInSent = [] #number of words in each sentence
        longSentences = []
        for oneP in content:
            allS = re.split(r'\n', oneP)
#            allS = oneP.split('. ')
            for oneS in allS:
                curLength = len(oneS.split(' '))
                wordsInSent.append(curLength)
                longSentences.append(oneS)
        for index, item in enumerate(wordsInSent):
            if item <= threshLow:
                wordsInSent.remove(item)
                del longSentences[index]
        return wordsInSent, longSentences, round(sum(wordsInSent)/len(longSentences), 2), round(np.std(wordsInSent), 2)

plt.close('all')
#reads all files in a directory and returns a dictionary of wordAnalysis objects
def readAll(location = 'sample files'):
    fileDic = {}
    for oneFileName in os.listdir(location):
        fileDic[oneFileName] = wordAnalysis(oneFileName)
    return fileDic

dic = readAll()
        
    




        