import json
from difflib import get_close_matches
data=json.load(open("E:data.json"))
def first(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=raw_input('Did you mean %s? Enter Y for yes and N for no: '%get_close_matches(w,data.keys())[0])
        if yn=='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='N':
            return "Word doesn't exist"
        else:
            return "Wrong choice"
    else:
        return "Word doesn't exist"
word=raw_input('Enter word: ')
print (first(word))
