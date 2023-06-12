import dbfs_parser
import pysftp

#sending over the file to the server
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
def push_table():
    args, parser = dbfs_parser.prog_parser()
    print (args.list)
  
    if args.push:

        try:
            svr = pysftp.Connection('', username='', password='')
            #print(svr.listdir("/home/dev/Desktop/projects"))
         
            svr.close()

        except Exception as e:
            print('An error occurred:', str(e))
        
#todo:
#needs conditional to check that the file is an sql file