import dbfs_parser
import pysftp
import os

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
def push_table():
    args, parser = dbfs_parser.prog_parser()

    sql_file = args.push
    if sql_file:

        try:


            local_file_path = f'./config/{sql_file}.txt'
            remote_file_path = f"/home/dev/Desktop/projects/{sql_file}.txt"
            svr = pysftp.Connection('', username='', password='')
            #print(svr.listdir("/home/dev/Desktop/projects"))
            svr.put(local_file_path,  remote_file_path)
            svr.close()

        except Exception as e:
            print('An error occurred:', str(e))
        
