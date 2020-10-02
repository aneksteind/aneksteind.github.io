

# hoffer.py
# Python 3.8.3

import random
import sys

random.seed(int(sys.argv[1]))

numbers = [random.random() for _ in range(3)]

# my copy of the book ranges from page 3 to page 207
pages = [n * 204 + 3.0 for n in numbers]

print(pages)