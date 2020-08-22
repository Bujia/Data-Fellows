# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:07:12 2020

@author: Guo Bujia
"""

import sys
from urllib.parse import urlparse
import requests
import bs4

def main():
   x = sys.argv[1]
   #Parsing URL to six components
   site = urlparse(x)
   tld = site[1].split(".")[-1]
   hostname = site[1]
   domain = hostname.split(".")[1:]
   domain = ".".join(domain)
   path = site[2]
   
   print("TLD: " + tld)
   print("DOMAIN: " + domain)
   print("HOSTNAME: " + hostname)
   print("PATH: " + path)
   print("LINKS: ")
   
   hostlist = []
   sdomainlist = []
   domainlist = []
   
   res = requests.get(x)
   soup = bs4.BeautifulSoup(res.text, "lxml")
   #Find all a-tags which contais href string value
   for link in soup.find_all("a", href = True):
       #exculing non-link from the html
       if link["href"][0] == "#":
           pass
       #link is only path, need to attach the hostname to the link
       elif link["href"][0] == "/":
           urlink = "https://"+ hostname + link["href"]
           #sorting the links 
           if hostname in urlink:
               hostlist.append(urlink)
           elif domain in urlink:
               sdomainlist.append(urlink)
           else:
               domainlist.append(urlink)
       else:
           #sorting the links 
           if hostname in link["href"]:
               hostlist.append(link["href"])
           elif domain in link["href"]:
               sdomainlist.append(link["href"])
           else:
               domainlist.append(link["href"])
           

   print("Same hostname: ")
   for y in range(len(hostlist)):
       print(hostlist[y])
    
   print("Same domain: ")
   for z in range(len(sdomainlist)):
       print(sdomainlist[z])
   print("Other domain: ")
   for a in range(len(domainlist)):
       print(domainlist[a])
        
if __name__ == "__main__":
   main()
