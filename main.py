import argparse
import datetime
import json
import random
import datetime
from time import sleep

import requests

import form

url = "https://docs.google.com/forms/d/e/1FAIpQLSd6uMTGvlrlbA5LwRcvci88tmYqMLRp5-F_nYW1JUiwgNJfPg/formResponse"

# {
#     # Student Name (required)
#     #   Option: any text
#     "entry.2005620554": "",
#     # Student ID (required)
#     #   Option: any text
#     "entry.1456717958": "",
#     # DMD Group (required)
#     #   Options: ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6', 'Group 7', 'Group 8']
#     "entry.585399452": "",
#     # Date Student is Available (required)
#     #   Option: YYYY-MM-DD
#     "entry.1864927337": "",
#     # AM/PM/Both (required)
#     #   Options: ['AM', 'PM', 'Both']
#     "entry.1846801040": "",
#     # Student Phone # (required)
#     #   Option: any text
#     "entry.1166974658": "",
#     # Email Address (required)
#     #   Options: email address
#     "emailAddress": ""
# }

value1 = {
    # Name (required)
    #   Option: any text
    "entry.2005620554": "Alex",
    # Email (required)
    #   Option: any text
    "entry.1045781291": "tempemail@gmail.com",
    # Address (required)
    #   Option: any text
    "entry.1065046570": "Texas",
    # Phone number
    #   Option: any text
    "entry.1166974658": "941555215",
    # Comments
    #   Option: any text
    "entry.839337160": "This will be submitted first"
}

def submit(data):
    try:
        print(url)
        requests.post(url, data = data)
        print("Submitted successfully!")
    except:
        print("Error!")

def main(value):
    try:
        submit(value)
        print("Done!!!")
    except Exception as e:
        print("Error!", e)

if __name__ == '__main__':
    #submit time is in military time
    #HOUR:minute:Millisecond it takes a millisecond to submit to put the submit time one millisecond before
    submitTime="21:31:30.50"
    string_i_want=""
    while(string_i_want != submitTime):
        now=datetime.datetime.now()
        string_i_want=('%02d:%02d:%02d.%d'%(now.hour,now.minute,now.second,now.microsecond))[:-4]
        print(string_i_want)
    main(value1)
