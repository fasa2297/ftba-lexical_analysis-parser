print("Tugas Besar Teori Bahasa Automata | IF-43-01")
print("Lexical Analyzer & Parser")
print("Anindika Riska Intan Fauzy (1301194254)\nBagus Seno Pamungkas (1301190337)\nFauzi Arya Surya Abadi (1301194101)\n")

import string

def LA(sentence):
    # initialization
    print("\n====== Lexical Analyzer ====== \n")
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
                'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                'q11','q12','q13','q14','q15','q16','q17','q18','q19',
                'q20','q21','q22','q23','q24','q25','q26',
                ]
    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    # Deskripsi CFG untuk Bahasa Inggris
    # S = {SB, VB, OB} 
    # SB → we | she 
    # VB →  eats | loves | likes
    # OB →  her | them | cat | it | bread

    # first state
    transition_table[("q0", " ")] = "q0"

    # Finish state
    transition_table[("q25", "#")] = "accept"
    transition_table[("q25", " ")] = "q26"

    transition_table[("q26", "#")] = "accept"
    transition_table[("q26", " ")] = "q26"

    #____for string "we"
    transition_table[("q26", "w")] = "q2"
    transition_table[("q0", "w")] = "q2"
    transition_table[("q2", "e")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "she"
    transition_table[("q26", "s")] = "q1"
    transition_table[("q0", "s")] = "q1"
    transition_table[("q1", "h")] = "q2"
    transition_table[("q2", "e")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "eats"
    transition_table[("q26", "e")] = "q3"
    transition_table[("q0", "e")] = "q3"
    transition_table[("q3", "a")] = "q4"
    transition_table[("q4", "t")] = "q5"
    transition_table[("q5", "s")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "loves"
    transition_table[("q26", "l")] = "q6"
    transition_table[("q0", "l")] = "q6"
    transition_table[("q6", "o")] = "q7"
    transition_table[("q7", "v")] = "q8"
    transition_table[("q8", "e")] = "q9"
    transition_table[("q9", "s")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "likes"
    transition_table[("q26", "l")] = "q6"
    transition_table[("q0", "l")] = "q6"
    transition_table[("q6", "i")] = "q10"
    transition_table[("q10", "k")] = "q11"
    transition_table[("q11", "e")] = "q12"
    transition_table[("q12", "s")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "cat"
    transition_table[("q26", "c")] = "q13"
    transition_table[("q0", "c")] = "q13"
    transition_table[("q13", "a")] = "q14"
    transition_table[("q14", "t")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "her"
    transition_table[("q26", "h")] = "q15"
    transition_table[("q0", "h")] = "q15"
    transition_table[("q15", "e")] = "q16"
    transition_table[("q16", "r")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "them"
    transition_table[("q26", "t")] = "q17"
    transition_table[("q0", "t")] = "q17"
    transition_table[("q17", "h")] = "q18"
    transition_table[("q18", "e")] = "q19"
    transition_table[("q19", "m")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "it"
    transition_table[("q26", "i")] = "q20"
    transition_table[("q0", "i")] = "q20"
    transition_table[("q20", "t")] = "q25"
    transition_table[("q25", " ")] = "q26"

    #____for string "bread"
    transition_table[("q26", "b")] = "q21"
    transition_table[("q0", "b")] = "q21"
    transition_table[("q21", "r")] = "q22"
    transition_table[("q22", "e")] = "q23"
    transition_table[("q23", "a")] = "q24"
    transition_table[("q24", "d")] = "q25"
    transition_table[("q25", " ")] = "q26"


    #lexical analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state!='accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q25':
            print('current token: ' , current_token,', valid')
            current_token = ''
        if state== 'error':
            print('eror')
            break;
        idx_char = idx_char + 1
    #conclusion
    if state=='accept':
        print('semua token di input: ', sentence, ', valid') 
    
    return LA

def Parser(sentence):
    print("\n====== Parser ====== \n")
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
        print('Input string ','"', sentence,'"', ' diterima, sesuai Grammar')
    else:
        print('Error, input string:','"', sentence,'"', ', tidak diterima, tidak sesuai Grammar')

    return Parser


print("Terminal: we - she | eats - loves - likes | her - them - cat - it - bread \n")
sentence = input("Input in here:  ") 
input_string = sentence.lower()+'#'
LA(sentence)
Parser(sentence)

