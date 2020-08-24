# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:12:58 2020

@author: Guo Bujia
"""
import requests
from bs4 import BeautifulSoup 
from collections import Counter
import re
import sys
import json
import heapq
import difflib
"""This function scrapes all the words from given website
and returns a list of all the words from the website"""
def w_scaper(url, stopwords):
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
    #Loading the most common gamling words
    with open("gambling_words.json", "r") as json_file:
        data = json.load(json_file)
        
    url = sys.argv[1]
    wlist = w_scaper(url, stopwords)
    dlist = dictionary(wlist)    
    #getting the top common words from urls
    data1 = heapq.nlargest(100, data, key = data.get)
    data2 = heapq.nlargest(10, dlist, key = dlist.get)
    print(data2)
    similarity=difflib.SequenceMatcher(None,data2,data1).ratio()
    print(similarity)
    if similarity > 0.05:
        print("Gambling site")
    else:
        print("Non-Gambling site")


if __name__ == "__main__":
   main()