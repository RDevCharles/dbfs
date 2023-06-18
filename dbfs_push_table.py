from dotenv import load_dotenv
import os
import dbfs_parser
import pysftp

load_dotenv()

#sending over the file to the server
cnopts = pysftp.CnOpts()

cnopts.hostkeys = None
cnopts.log = True


def push_table():
    args, parser = dbfs_parser.prog_parser()

    sql_file = args.push
    if sql_file:

        try:

            local_file_path = f'./config/{sql_file}.txt'
            remote_file_path = f"/home/dev/Desktop/projects/{sql_file}.txt"
            print("hello")
            #host is the ip address of ec2 instance
            #username is the user name of ec2 instance
            #private_key is the path to the private key(pem file)
            svr = pysftp.Connection(host=os.getenv("EC2HOST"), username=os.getenv(
                "EC2USERNAME"), private_key=os.getenv("EC2PATH2PEM"), cnopts=cnopts)

            print(svr.listdir("/home/ubuntu/"))
            print("world")
            #svr.put(local_file_path,  remote_file_path)
            #svr.close()

        except Exception as e:
            print('An error occurred:', str(e))

#todo:
#needs conditional to check that the file is an sql file
