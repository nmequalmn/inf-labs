import re

def parser(input):
    input = re.sub(r'<(\w+)>', r'\g<1>: ', input)
    input = re.sub(r'</\w+>', r'', input)
    return input

with open('./input.xml', 'r') as f:
    s = ''.join(f.readlines())

res = parser(s)

with open('output_with_re.yml', 'w') as f:
    f.write(res)