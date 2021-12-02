import os
import sys
import requests
import argparse
from shutil import copyfile
from datetime import datetime

parser=argparse.ArgumentParser()
parser.add_argument("-d","--day",help="Manually get <day>'s challenge")
args=parser.parse_args()

print(args.day)
# Get day's challenge
if args.day is None:
    date=datetime.now()
    day=date.strftime("%d")
else:
    day=args.day

# To get Session ID, open Chrome/Brave to AOC, press F12, click on Application tab 
# On the left hand side, select Storage->Cookies->adventofcode.com and click the session cookie 
# The cookie value should appear below. Store it in a file called sessionID in the same folder as this script
path=sys.path[0]
with open(f"{path}/sessionID",'r') as sid:
    sessionID = sid.readline()
# Set up URL 
url = f'https://adventofcode.com/2021/day/{int(day)}/input'

cookies = dict(session=sessionID)
data = requests.get(url, cookies=cookies)

# Make challenge directory
day_path=f"{path}/{day}"
os.makedirs(day_path,exist_ok=True)

# Get input
with open(f"{day_path}/input",'w') as input:
    input.write(data.text)

# Create file for test input (on challenge page)
with open(f"{day_path}/test_input",'w') as testinput:
    pass

copyfile("template.py",f"{day_path}/1.py")
copyfile("template.py",f"{day_path}/2.py")

