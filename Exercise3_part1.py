# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 01:02:59 2020

@author: Guo Bujia
"""
import requests
from bs4 import BeautifulSoup 
from collections import Counter
import re
import json
"""This function scrapes all the words from given website
and returns a list of all the words from the website"""
def w_scraper(url, stopwords):
    wordlist = []
    c_wordlist = []
    #Fetching the sites sources code
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser") 
    for each_text in soup.findAll("div"): 
        content = each_text.text
        #convert text to lowercase and splitting the sentences
        words = content.lower().split()
        
        for each_word in words:
            #checking most common words in english and skipping them
            if each_word not in stopwords:
                wordlist.append(each_word)
    #Remocing unwanted symbols from the words
    for word in wordlist:
        #repaling non ASCII and numbers with ""
        word = re.sub("\W|\d+", "", word)
        if len(word) > 0:
            c_wordlist.append(word)
        
    return c_wordlist

#Creating dictiornay from the word list
def dictionary(wlist):
    c= Counter()
    for word in wlist:
        c[word] +=1
    return c

def main():

    f1 = open("stopwords.txt", "r")
    stopwords = f1.read()
    #Creating dict for the word counter
    wlist = []
    with open("sites.txt", "r") as file:
        for line in file:
             url = line.strip()
             words = w_scraper(url, stopwords)
             wlist = wlist + words
          
    data = dictionary(wlist)
    with open('gambling_words.json', 'w') as fout:
        json.dump(data, fout)   
        
if __name__ == "__main__":
   main()
