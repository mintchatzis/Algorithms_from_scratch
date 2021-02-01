import re

my_str = "We are taking the hobbits to Isengard"
regex = r'[a-z]'

matches = re.findall(regex,my_str)

for match in matches:
    print(match)