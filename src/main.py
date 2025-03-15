import os
from leafnode import LeafNode
from textnode import *
from functions import *


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

   
    
    generate_pages_recursive()

main()
