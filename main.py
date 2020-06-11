import json
import re
from YarnReader import nodes_from_dict
from yarnNodeChoice import NodeChoice
f= open("output.txt","w+")
nodesWithBranches = []
formattedNodes = []
with open('yarnExample.json') as json_file:
    result = nodes_from_dict(json.load(json_file))

for node in result:
    newNode = NodeChoice(node)
    newNode.processBranches()
    nodesWithBranches.append(newNode)

for i in nodesWithBranches:
    f.write(str(i)+"\n")

