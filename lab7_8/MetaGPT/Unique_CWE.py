import os
import json
from collections import Counter


def get_cwe(path):
    cwe_cnt = Counter()
    all_files = [i for i in os.listdir(path) if i.endswith(".json")]
    for file in all_files:
        full_path = os.path.join(path, file)
        with open(full_path, 'r') as f:
            data = json.load(f)

            if 'results' in data and isinstance(data['results'], list):
                for r in data['results']:
                    if 'issue_cwe' in r and 'id' in r['issue_cwe']:
                        cwe_id = r['issue_cwe']['id']
                        cwe_cnt[cwe_id] += 1

    return dict(cwe_cnt)


if __name__ == "__main__":
    ans = get_cwe("/home/bobby/Downloads/software/lab7-8/MetaGPT/bandit_results3")

    for cwe_id, frequency in sorted(ans.items(), key=lambda x: x[1], reverse=True):
        print(f"CWE-{cwe_id}: {frequency} occurrences")