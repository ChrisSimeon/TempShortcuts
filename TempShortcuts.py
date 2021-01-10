# -*- coding: utf-8 -*-
import os.path
import sys

def tempshort():
    path = "/Users/chris/Library/Preferences/espanso/user/Temporary.yml"

    query = sys.argv[1]
    query = query.split("+")
    if len(query) == 2 or 3:
        if not os.path.isfile(path):
            with open("/Users/chris/Library/Preferences/espanso/user/Temporary.yml", "a") as f:
                f.write('name: Temporary' + "\n")
                f.write('parent: default'+ "\n\n")
                f.write('matches:'+ "\n")



        with open("/Users/chris/Library/Preferences/espanso/user/Temporary.yml", "a") as f:
            f.write('  - trigger: "{a}"'.format(a = query[0]) + "\n")
            f.write('    replace: "{b}"'.format(b = query[1]) + "\n")
            if len(query) ==3:
                f.write('    word: true'+ "\n")
            f.write("\n\n")

        print("Shortcut hinzugefügt")

    else:
        print("nicht genügend Argumente")

if __name__ == "__main__":
    tempshort()


