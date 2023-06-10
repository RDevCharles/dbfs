import dbfs_parser
import pysftp




def push_table():
    args, parser = dbfs_parser.prog_parser()
    
    sql_file = args.push
    if sql_file:
        
        print(sql_file)
       
        local_file_path = f'/path/to/{sql_file}'
        remote_file_path = f'/path/on/server/{sql_file}'

        with pysftp.Connection('server_address', username='your_username', password='your_password') as sftp:
            sftp.put(local_file_path, remote_file_path)
            sftp.close()
