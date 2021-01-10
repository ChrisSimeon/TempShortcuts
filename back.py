path = "/Users/chris/Library/Preferences/espanso/user/Temporary.yml"

with open(path, "r") as f:
    lines = f.readlines()
with open(path, "w") as f:
    a = len(lines) - 5 
    for line in lines[0:a]:
        f.write(line)