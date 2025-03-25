import os
import json
from collections import Counter

def generator(path):
    cnt = Counter()
    alls = [i for i in os.listdir(path) if i.endswith(".json")]
    for f in alls:
        f_path = os.path.join(path, f)
        with open(f_path, 'r') as f:
            data = json.load(f)

            if 'results' in data and isinstance(data['results'], list):
                for r in data['results']:
                    if 'issue_cwe' in r and 'id' in r['issue_cwe']:
                        id = r['issue_cwe']['id']
                        cnt[id] += 1


ans = generator("/home/bobby/Downloads/software/lab7-8/django/bandit_results")
for id, freq in sorted(ans.items(), key=lambda x: x[1]):
    print(f"CWE-{id}: {freq} frequency")