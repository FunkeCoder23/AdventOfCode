from html.parser import HTMLParser
import requests
from replit import db


class AoCParser(HTMLParser):

    store = False
    instr = []
    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.store = True

    def handle_endtag(self, tag):
        if tag == "article":
            self.store = False

    def handle_data(self, data):
        if self.store:
            self.instr.append(data)
            if len(self.instr) == 1:
                self.instr.append("\n")

    def get_data(self):
        return self.instr


parser = AoCParser()

url = "https://adventofcode.com/2015/day/1"
cookies = dict(session=db['sessionID'])
print(cookies)
# data = requests.get(url, cookies=cookies)
with open("test.html", 'r') as f:
    # f.write(data.text)
    parser.feed(f.read())
print("".join(parser.get_data()))
