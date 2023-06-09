import dbfs_parser
import os


def push_table():
    args, parser = dbfs_parser.prog_parser()
    
    connect_str = args.push
    if connect_str:
        #here we need to make a connection to the database
        print(connect_str)
       
