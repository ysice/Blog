from __future__ import print_function

import json
result = {}

with open("../templates/misc/link/links.txt","rb") as link:
    link_tag = None
    for line in link:
        line = line.strip()
        if line == "":
            continue
        if ':' in line:
            link_tag = line[:-1]
        else:
            link_info = line.split(None,1)
            result.setdefault(link_tag,{})[link_info[0]]=link_info[1]

print(json.dumps(result,indent = 4).decode("unicode-escape"))

