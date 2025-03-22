import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="To Do List")
    parser.add_argument("a", "add")
    parser.add_argument("v", "view")
    parser.add_argument("d", "delete")
    parser.add_argument("q", "quit")
    return parser

#QUESTIONS: 1) what is this supposed to look like? examples? 2) how to import argparse?
#MY EXPECTATION FOR WHAT IT WILL LOOK LIKE...

# Welcome to your to-do list app!
# Type 'a' to add item to your list. Type 'd' to delete item from your list. Type 'v' to view your list. Type 'q' to exit.

# laundry (linens):
# laundry (clothes):
# dishes:
# tidy up:
# sweep:
# mop: