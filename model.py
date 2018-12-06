import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
COUNTER_FILE = "count.json"
entries = []

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

    return entries

def get_entries():
    global entries
    global counter
    return entries

def count():
    global entries
    counter={}
    try:
        with open(COUNTER_FILE, encoding = 'utf-8') as g:
            counter = json.load(g)
    except:
        counter['count'] = 0

    return str(counter['count'])

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, counter, COUNTER_FILE
    now = datetime.now()
    counter={}
    #time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": count()}
    entries.insert(0, entry) ## add to front of list
    try:
        g = open(COUNTER_FILE)
        counter = json.loads(g.read())
        g.close()
    except:
        counter['count'] = 0

    counter['count']+= 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

    try:
        f = open(COUNTER_FILE, "w")
        dump_counter = json.dumps(counter)
        f.write(dump_counter)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(counter):
    global entries
    entry1 = []
    try:
        with open(GUESTBOOK_ENTRIES_FILE, encoding = 'utf-8') as g:
            jsonReader = json.load(g)
            for i in jsonReader:
                if str(counter)!=i['id']:
                    entry1.append(i)
                else:
                    pass
    except:
        entry1 = []
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entry1)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
