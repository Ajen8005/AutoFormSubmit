import argparse
import datetime
import json
import random
import datetime

import requests

import form

url = "https://docs.google.com/forms/d/e/1FAIpQLSfUXMXl16jyhRIQU-2i1m3gM7I255YTfVh4VQDG785vts681Q/formResponse"

# example
def fill_form():
    value = {
    # Untitled Question
    #   Options: ['Option 1']
    "entry.477139486": ['Option 1']
    }
    print(value, flush = True)
    return value

def submit(data):
    try:
        print(url)
        requests.post(url, data = data)
        print("Submitted successfully!")
    except:
        print("Error!")

def main():
    try:
        submit(fill_form())
        print("Done!!!")
    except Exception as e:
        print("Error!", e)

if __name__ == '__main__':
    #submit time is in military time
    #HOUR:Second:Millisecond it takes a millisecond to submit to put the submit time one millisecond before
    submitTime="20:58:59"
    string_i_want=""
    while(string_i_want != submitTime):
        now=datetime.datetime.now()
        string_i_want=('%02d:%02d:%02d.%d'%(now.hour,now.minute,now.second,now.microsecond))[:-4]
        print(string_i_want)
    main()
