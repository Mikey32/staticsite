import sys
from leafnode import LeafNode
from textnode import *
from functions import *


def main(arg):
    if arg:
        print(arg)
        basepath = arg
    else:
        basepath = "/"
    
    
    
    generate_pages_recursive(basepath)

if len(sys.argv) > 1:
    main(sys.argv[1])
else: 
    main(None)
