from sys import stdin
from itertools import combinations

import string

table = dict(zip(string.ascii_lowercase, list(range(26))))

bit_table = '0'*26

bit_table[table['a']] = '1'


