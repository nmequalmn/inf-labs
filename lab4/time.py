import timeit

for i in ['parser.py', 'parser_with_re.py', 'parser_with_libs.py']:
    with open('./'+i, 'r') as f:
        code = ''.join(f.readlines())
    elapsed_time = timeit.timeit(code, number=100)/100
    print(i + ': ' + str(elapsed_time*10))