# F-Secure
F-Securen coding exercise

Exercise 1
General
-------

This is a basic Python coding exercise. In order to properly solve this,
you would need some understanding on how URLs are built and how links work.

Given a URL, you need to generate the following:

1.) The Top Level Domain (TLD) of this URL.

2.) The domain of this URL.

3.) The hostname of this URL.

4.) The path of this URL.

5.) All the links (both statically clickable & statically unclickable but dynamically generated) found on the page this URL points to, arranged in the following:

    a.) Links that belong to the same hostname.
    
    b.) Links that belong to the same domain, but different hostname.
    
    c.) Links that belong to a different domain.


Exercise 3
This is an exercise to test your ideas for content classification.
In order to properly solve this, you would need to be able to parse an HTML file.

This exercise has 2 parts:
Part 1 - Generating the dictionary of keywords.
Part 2 - Using the dictionary of keywords to classify a website.

Part 1
1. Hunt for as much websites as you can that you can classify as a Gambling site. These have to be websites in the English language, and you can look for as many websites as possible. List the URLs of the websites in a text file.
Eg:
	text file contains:
		http://site1.gambling
		http://sportsbetting.tld
		http://bettingtips.blog/a.html


2. Using the text file you generated above, create a Python script that will visit those websites, parse out the keywords and generate a dictionary of Gambling-related terms. This dictionary can be any file format (text, json, csv, etc.) that you will be using in Part 2. You can use any method that you deem necessary to generate the appropriate keywords.
	- INPUT: yourscript1.py <the text file with the gambling URLs>
	- OUTPUT: dictionary file

Part 2
Using the dictionary from Part 1, create a Python script that will expect a URL input, and then generate a classification if it's a Gambling site or not.
	- INPUT: yourscript2.py <Any URL>
	- OUTPUT1: Gambling site
	- OUTPUT2: Non-Gambling site
