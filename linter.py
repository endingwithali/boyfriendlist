import os

with open(os.path.join(os.getcwd(), 'README.md'), 'r') as fd:
    md_content = fd.read()

content = md_content.split('\n')

for idx, _cont in enumerate(content):
    if _cont == '<ol>':
        content.insert(idx+1, '  <li><a href="https://github.com/VersaceSauce">VersaceSauce</a></li>')
        break

with open(os.path.join(os.getcwd(), 'README.md'), 'w') as fd:
    fd.write('\n'.join(content))