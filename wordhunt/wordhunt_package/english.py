import json

def create_english_list(path: str) -> set[str]:
    with open(path, 'r') as f:
        lines = f.readlines()
    
    r = set()
    for line in lines:
        line = line.strip()
        if line.isalnum():
            r.add(line)

    return r

class Trie(dict):
    def insert(self, word):
        children = self
        for c in word:
            if c not in children:
                children[c] = Trie()
            children = children[c]
        children['*'] = None

def create_trie(wordlist):
    trie = Trie()
    for word in wordlist:
        trie.insert(word)

    with open('english.json', 'w') as f:
        json.dump(trie, f)

def restore_trie(path):
    with open(path, 'r') as f:
        trie = json.load(f)
    return trie