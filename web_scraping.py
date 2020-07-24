# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:27:00 2020

@author: Akash
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Website: https://en.tutiempo.net/climate

import os
import time
import requests # Did not use beautifulsoup but request enabled me to download in the form of html file
import sys


def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10): # For months before 10th Month - October hence '0{}-{}'
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            texts=requests.get(url) # Request/Retreive source URL
            text_utf=texts.text.encode('utf=8') # utf-8 to fix HTML tags
           
            
        # Step 1: Create folder for year     
        # Step 2: Open the folder
        # Step 3: write the text_utf - whatever I get from the website
        # Step 4: Flush everthing that is created in the file
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush() #Flush
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))