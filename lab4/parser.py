def parser(input):
    while('</' in input):
        tr = False
        start = 0
        end = 0
        for i in range(len(input)):
            if tr and input[i]=='>':
                end = i
                tr = False
            if tr:
                continue
            if (i<len(input)-1):
                if (input[i]+input[i+1])=='</':
                    tr = True
                    start=i
                    
        input = input[0:start]+input[end+1:len(input)]
    input = input.replace('<','').replace('>',": ")
    return input



with open('./input.xml', 'r') as f:
    s = ''.join(f.readlines())

res = parser(s)

with open('output.yml', 'w') as f:
    f.write(res)