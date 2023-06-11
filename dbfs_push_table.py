import dbfs_parser
import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
def push_table():
    args, parser = dbfs_parser.prog_parser()

    sql_file = args.push
    if sql_file:

        print(sql_file)

        local_file_path = f'/config/{sql_file}.txt'
        remote_file_path = ''

        svr = pysftp.Connection('', username='', password='')
        svr.put(local_file_path, remote_file_path)
        svr.close()
