
braille_codes={
            frozenset(['d']):'a',
            frozenset(['d','w']):'b',
            frozenset(['d','k']):'c',
            frozenset(['d','k','o']):'d',
            frozenset(['d','o']):'e',
            frozenset(['d','w','k']):'f',
            frozenset(['d','w','k','o']):'g',
            frozenset(['d','w','o']):'h',
            frozenset(['w','k']):'i',
            frozenset(['w','k','o']):'j',
            frozenset(['d','q']):'k',
            frozenset(['d','w','q']):'l',
            frozenset(['d','q','k']):'m',
            frozenset(['d','q','k','o']):'n',
            frozenset(['d','q','o']):'o',
            frozenset(['d','w','q','k']):'p',
            frozenset(['d','w','q','k','o']):'q',
            frozenset(['d','w','q','o']):'r',
            frozenset(['w','q','k']):'s',
            frozenset(['w','q','k','o']):'t',
            frozenset(['d','q','p']):'u',
            frozenset(['d','w','q','p']):'v',
            frozenset(['w','k','p','o']):'w',
            frozenset(['d','q','k','p']):'x',
            frozenset(['d','q','k','o','p']):'y',
            frozenset(['d','q','o','p']):'z'
        }


dot_values={
                'a':[1, 0, 0, 0, 0, 0],  #d
                'b':[1, 1, 0, 0, 0, 0],  #d,w
                'c':[1, 0, 0, 1, 0, 0],  #d,k
                'd':[1, 0, 0, 1, 1, 0],  #d,k,o
                'e':[1, 0, 0, 0, 1, 0],  #d,o
                'f':[1, 1, 0, 1, 0, 0],  #d,w,k
                'g':[1, 1, 0, 1, 1, 0],  #d,w,k,o
                'h':[1, 1, 0, 0, 1, 0],  #d,w,o
                'i':[0, 1, 0, 1, 0, 0],  #w,k
                'j':[0, 1, 0, 1, 1, 0],  #w,k,o
                'k':[1, 0, 1, 0, 0, 0],  #d,q
                'l':[1, 1, 1, 0, 0, 0],  #d,w,q
                'm':[1, 0, 1, 1, 0, 0],  #d,q,k
                'n':[1, 0, 1, 1, 1, 0],  #d,q,k,o
                'o':[1, 0, 1, 0, 1, 0],  #d,q,o
                'p':[1, 1, 1, 1, 0, 0],  #d,w,q,k
                'q':[1, 1, 1, 1, 1, 0],  #d,w,q,k,o
                'r':[1, 1, 1, 0, 1, 0],  #d,w,q,o
                's':[0, 1, 1, 1, 0, 0],  #w,q,k
                't':[0, 1, 1, 1, 1, 0],  #w,q,k,o
                'u':[1, 0, 1, 0, 0, 1],  #d,q,p
                'v':[1, 1, 1, 0, 0, 1],  #d,w,q,p
                'w':[0, 1, 0, 1, 1, 1],  #w,k,o,p
                'x':[1, 0, 1, 1, 0, 1],  #d,q,k,p
                'y':[1, 0, 1, 1, 1, 1],  #d,q,k,o,p
                'z':[1, 0, 1, 0, 1, 1],  #d,q,o,p
                '?':[0, 0, 0, 0, 0, 0]   #Invalid input
            }