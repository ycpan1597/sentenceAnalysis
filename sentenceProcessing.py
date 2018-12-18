#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 09:37:02 2018

@author: preston
"""
import matplotlib.pyplot as plt
import numpy as np


class wordAnalysis:
    def __init__(self, fileName):
        self.content = self.readFile(fileName)
        self.wordsInSent, self.sentences, self.avg, self.std = self.findWordsInSent(self.content)
        
        plt.figure()
        plt.hist(self.wordsInSent, bins = np.arange(0, 35, 1))
        plt.title('Words in each sentence, (total = ' + str(len(self.sentences)) + ' sentences)')
        plt.axvline(x = self.avg, label = 'Avg = ' + str(self.avg) + ', Std = ' + str(self.std), color = 'k')
        plt.axvline(x = self.avg + self.std, color = 'k', ls = '--')
        plt.axvline(x = self.avg - self.std, color = 'k', ls = '--')
        plt.axvline(x = 20, label = 'too many words!', color = 'r', ls = '--')
        plt.axvline(x = 4, label = 'too few words!', color = 'r', ls = '--')
        plt.legend()
        
    def readFile(self, fileName):
        with open(fileName, 'r') as f:
            x = f.readlines()
        return x
    
    def findWordsInSent(self, content, threshLow = 3):
        wordsInSent = [] #number of words in each sentence
        sentences = []
        for oneP in content:
            allS = oneP.split('. ')
            for oneS in allS:
                curLength = len(oneS.split(' '))
                wordsInSent.append(curLength)
                sentences.append(oneS)
        for index, item in enumerate(wordsInSent):
            if item <= threshLow:
                wordsInSent.remove(item)
                del sentences[index]
        return wordsInSent, sentences, round(sum(wordsInSent)/len(sentences), 2), round(np.std(wordsInSent), 2)

plt.close('all')
writing1 = wordAnalysis('Personal Statement - BME.txt')
writing2 = wordAnalysis('Personal Statement - BME(2).txt')



        