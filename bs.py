from ast import Return
from dataclasses import replace


gen1 = "En el principio creó Dios los cielos y la tierra. La"
gene=['in', 'the', 'beginning', 'created', 'God', 'the', 'Heavens', 'and', 'the', 'Earth.', 'the', 'earth', 'was', 'orderless', 'and', 'no', 'had', 'shape', 'The', 'darkness', 'covered', 'the', 'deep', 'abis', 'while', 'que', 'el', 'Spirit', 'of', 'God', 'se', 'movoved', 'over', 'the', 'waters']

def blen(word):
    dict={'En': 'in', 'el': 'el', 'principio': 'beginning', 'creó': 'created', 'Dios': 'God', 'los': 'the', 'cielos': 'Heavens', 'y': 'and', 'la': 'the', 'tierra.': 'Earth.', 'La': 'The', 'tierra': 'earth', 'estaba': 'was', 'desordenada': 'orderless', 'no': 'no', 'tenía': 'had', 'forma.': 'shape', 'oscuridad': 'darkness', 'cubría': 'covered', 'profundo': 'deep', 'abismo,': 'abis', 'mientras': 'while', 'que': 'que', 'Espíritu': 'Spirit', 'de': 'of', 'se': 'se', 'movía': 'movoved', 'sobre': 'over', 'las': 'the', 'aguas': 'waters'}
    for k,v in dict.items():
        print("1=g.replace(",k,",",v,")")

