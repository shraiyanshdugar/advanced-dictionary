import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        YN=input("did you mean %s ? enter y for yes and n for no: " % get_close_matches(w,data.keys())[0])
        if YN == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif YN =="n":
            return " word does not exist"
        else:
            return "sorry we didnt got you"
    else:
        return "word not exist"
word=input("enter the word: ")

output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
