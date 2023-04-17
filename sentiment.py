import re
sadwords = []
with open('emotions.txt','r') as file :
    for line in file :
        m = re.search("'(.*?)': 'sad'", line)
        if m:
            sadwords.append(m.group(1))
print(sadwords)
