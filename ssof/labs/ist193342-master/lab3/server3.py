#!/usr/bin/env python
import hashlib
import os
import shutil
import pickle


# ===================================================
class Note(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return "Note '%s': %s" % (self.name, self.content)

def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

CLASSY_MODE = 'CLASSY'
FREE_MODE = 'FREE'
def check_mode(mode):
    try:
        with open(directory + '/mode', 'r') as f:
            return f.read() == mode
    except:
        return False

def set_mode(mode):
    with open(directory + '/mode', 'w') as f:
        f.write(mode)

def reset(mode):
    shutil.rmtree(directory)
    os.makedirs(directory)
    set_mode(mode)
# ===================================================


# Print banner
notes_storage = " _______   ________   ______________________  _________         ____________________________   __________    _____     ________ ___________\n \      \  \_____  \  \__    ___/\_   _____/ /   _____/        /   _____/\__    ___/\_____  \  \______   \  /  _  \   /  _____/ \_   _____/\n /   |   \  /   |   \   |    |    |    __)_  \_____  \         \_____  \   |    |    /   |   \  |       _/ /  /_\  \ /   \  ___  |    __)_ \n/    |    \/    |    \  |    |    |        \ /        \        /        \  |    |   /    |    \ |    |   \/    |    \\    \_\  \ |        \\\n\____|__  /\_______  /  |____|   /_______  //_______  / ______/_______  /  |____|   \_______  / |____|_  /\____|__  / \______  //_______  /\n        \/         \/                    \/         \/ /_____/        \/                    \/         \/         \/         \/         \/ "

print ("1. Ever lost your class notes??")
print ("2. Ever wanted to store notes but had no place to and then forgot everything and failed the exam???")
print ("3. Are you tired of having to carry your notebooks????")
print ("")
print ("If you answered YES, this is the service for you!!")
print (notes_storage)
print ("\n")


# Read username and setup directory
username = input('Username: ')
directory = "/tmp/notes/%s" % sha256(username)
if not os.path.exists(directory):
    os.makedirs(directory)

# Read user choices
type_choice = ""
while type_choice not in ('0', '1'):
    print("Which note type do you want:")
    print("0: Classy note")
    print("1: Free Note")
    type_choice = input('>>> ')

def read_or_write_option():
    action_choice = ""
    while action_choice not in ('0', '1'):
        print("0: Read note")
        print("1: Write Note")
        action_choice = input('>>> ')

    note_name = input('note_name: ')
    note_path = "%s/%s" % (directory, sha256(note_name))
    if action_choice == '0':
        if not os.path.isfile(note_path):
            print("[ERROR] Can't read a file that does not exist")
            exit(-1)
        else:
            with open(note_path, 'rb') as f:
                note_content = f.read()
    elif action_choice == '1':
        note_content = ""
        line = input("note_content: ")
        while line:
            note_content += line + '\n'
            line = input()

    return action_choice, note_path, note_name, note_content


# Main functionality
if type_choice == '0': # Classy note
    if not check_mode(CLASSY_MODE):
        reset(CLASSY_MODE)

    action_choice, note_path, note_name, note_content = read_or_write_option()
    if action_choice == '0': # read
        note = pickle.loads(note_content)
        print(note)
    elif action_choice == '1': # write
        note = Note(note_name, note_content)
        with open(note_path, 'wb') as f:
            pickle.dump(note, f)
    else:
        print("YT0!?")

elif type_choice == '1': # Free note
    if not check_mode(FREE_MODE):
        reset(FREE_MODE)

    action_choice, note_path, _, note_content = read_or_write_option()
    if action_choice == '0': # read
        print(note_content)
    elif action_choice == '1': # write
        with open(note_path, 'wb') as f:
            f.write(note_content.encode('utf8','surrogateescape'))
    else:
        print("HuM!?")
else:
    print("WHaT!?")