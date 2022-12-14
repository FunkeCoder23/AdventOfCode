import os
from shutil import copyfile
from datetime import datetime, timezone
import pytz
import requests
import sys
import subprocess

today = datetime.now(pytz.timezone('US/Eastern'))
# day = 8
# year = 2015
year = today.year
day = today.day
path = sys.path[0]

filepath = f"{path}/{year}/{day}"
if (not os.path.exists(f"{filepath}/1.py")):
    # import os

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = dict(session=os.environ['sessionID'])
    data = requests.get(url, cookies=cookies)

    # Make challenge directory
    os.makedirs(filepath, exist_ok=True)

    # Get input
    with open(f"{filepath}/input", 'w') as input:
        input.write(data.text)

    # Create file for test input (on challenge page)
    with open(f"{filepath}/test_input", 'w') as testinput:
        pass

    copyfile("template.py", f"{filepath}/1.py")
    copyfile("template.py", f"{filepath}/2.py")
else:
    print("Part 1")
    subprocess.run(["python3", f"{filepath}/1.py"], cwd=filepath)
    print("Part 2")
    subprocess.run(["python3", f"{filepath}/2.py"], cwd=filepath)
