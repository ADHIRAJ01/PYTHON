import requests  # HTTP package 

from bs4 import BeautifulSoup       # web scrapping 

import re # Regular Expression pattern making 

# from urllib.request import urlretrieve    # downloading mp4

import sys   # for argument parsing - using multiple url ass combined package


# EXCEPTION HANDLING 

if len(sys.argv)>1:
    url=sys.argv[1]
else:
    sys.exit("ERROR : PLEASSE ENTER TED TALK URL ")


#url = "..."

#url = "..."

r = requests.get(url)

print("DOWNLOAD ABOUT TO START ")

soup = BeautifulSoup(r.content , features = " lxml ")