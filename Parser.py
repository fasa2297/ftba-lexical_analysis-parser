
# input
print("Terminal: SB(we-she) VB(eats-loves-likes) OB(her-them-cat-it-bread \n")
sentence = input("input in here: ") 
tokens = sentence.lower().split()
tokens.append('EOS')

# symbols definition
non_terminals = ['S','SB','VB','OB']
terminals = ['we','she','eats','loves','likes',
            'her','them','cat','it','bread',
            ]

parse_table = {}

parse_table[('S','we')] = ['SB','VB','OB']
parse_table[('S','she')] = ['SB','VB','OB']
parse_table[('S','eats')] = ['error']
parse_table[('S','loves')] = ['error']
parse_table[('S','likes')] = ['error']
parse_table[('S','her')] = ['SB','VB','OB']
parse_table[('S','them')] = ['SB','VB','OB']
parse_table[('S','cat')] = ['SB','VB','OB']
parse_table[('S','it')] = ['SB','VB','OB']
parse_table[('S','bread')] = ['SB','VB','OB']
parse_table[('S','EOS')] = ['error']

parse_table[('SB','we')] = ['we']
parse_table[('SB','she')] = ['she']
parse_table[('SB','eats')] = ['error']
parse_table[('SB','loves')] = ['error']
parse_table[('SB','likes')] = ['error']
parse_table[('SB','her')] = ['error']
parse_table[('SB','them')] = ['error']
parse_table[('SB','cat')] = ['error']
parse_table[('SB','it')] = ['error']
parse_table[('SB','bread')] = ['error']
parse_table[('SB','EOS')] = ['error']

parse_table[('VB','we')] = ['error']
parse_table[('VB','she')] = ['error']
parse_table[('VB','eats')] = ['eats']
parse_table[('VB','loves')] = ['loves']
parse_table[('VB','likes')] = ['likes']
parse_table[('VB','her')] = ['error']
parse_table[('VB','them')] = ['error']
parse_table[('VB','cat')] = ['error']
parse_table[('VB','it')] = ['error']
parse_table[('VB','bread')] = ['error']
parse_table[('VB','EOS')] = ['error']

parse_table[('OB','we')] = ['error']
parse_table[('OB','she')] = ['error']
parse_table[('OB','eats')] = ['error']
parse_table[('OB','loves')] = ['error']
parse_table[('OB','likes')] = ['error']
parse_table[('OB','her')] = ['her']
parse_table[('OB','them')] = ['them']
parse_table[('OB','cat')] = ['cat']
parse_table[('OB','it')] = ['it']
parse_table[('OB','bread')] = ['bread']
parse_table[('OB','EOS')] = ['error']

#stack initialization
stack = []
stack.append('#')
stack.append('S')

#input reading initialization
idx_token = 0
symbol = tokens[idx_token]

#parse table process
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == "EOS":
                stack.pop()
                print('isi stack:', stack)
        else:
            print('error')
            break;
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbol_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbol_to_be_pushed)-1,-1,-1):
                stack.append(symbol_to_be_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('isi stack: ', stack)
    print()

#conlusion
print()
if symbol == 'EOS' and len(stack)== 0:
    print('input string ', sentence, ' diterima, sesuai Grammar')
else:
    print('Error, input string:', sentence, ', tidak diterima, tidak sesuai Grammar')