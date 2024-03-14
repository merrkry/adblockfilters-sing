import json
import requests

url = "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt"
response = requests.get(url)
source = response.text.split("\n")

with open("template.json", "r") as file:
    rules = json.load(file)

for line in source:
    line = line.strip()
    if not line.startswith('!'):
        if line.startswith('||'):
            domain = line[2:-1]
            rules['rules'][0]['rules'][0]['domain'].append(domain)
            rules['rules'][0]['rules'][0]['domain_suffix'].append("." + domain)
        elif line.startswith('@@||'):
            domain = line[4:-1]
            rules['rules'][0]['rules'][1]['domain'].append(domain)
            rules['rules'][0]['rules'][1]['domain_suffix'].append("." + domain)

with open('adblockfilters-sing.json', 'w') as file:
    json.dump(rules, file, indent=2)