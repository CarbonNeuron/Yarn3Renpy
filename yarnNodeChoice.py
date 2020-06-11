import re

class NodeBranch(object):
    def __init__(self, Title, DestinationNodeName):
        self.destination = DestinationNodeName
        self.title = Title

class NodeChoice(object):
    regex = r"\[\[Answer:(?P<Choice>[^|]+)\|(?P<Node>[^\]]+)\]\]"
    def __init__(self, node):
        self.node = node
        self.title = node.title
        self.tags = node.tags
        self.body = node.body
        self.branches = []

    def processBranches(self):
        print(f"Processing branch with name: {self.title}")
        matches = re.finditer(NodeChoice.regex, self.body, re.MULTILINE)
        for i in matches:
            self.branches.append(NodeBranch(i['Choice'],i['Node']))
        self.body = re.sub(NodeChoice.regex, '', self.body)

    def __repr__(self):
        self.body = self.body.strip('\n').rstrip()
        magic = f"label {self.title}:\n\t"
        if len(self.branches) == 0:
            magic+= f"\"{self.body}\"\n\treturn"
        else:
            magic+= f"menu:\n\t\t\"{self.body}\""
            for i in self.branches:
                magic += f"\n\t\t\"{i.title}\":\n\t\t\tjump {i.destination}"
        return magic.replace("\t", " "*4)



