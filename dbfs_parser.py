import argparse

def prog_parser():
    parser = argparse.ArgumentParser(
                   description="A relational database solution for students",)
    
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-l', '--login', action='store_true', help='Login to the database')
    parser.add_argument('-p', '--push', help='Push a file to the database')
    parser.add_argument('-s', '--set', help='Change username or password')
    
    args = parser.parse_args()
    
    return (args, parser)


    