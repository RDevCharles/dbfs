import dbfs_parser
import os


#set the varification code or "link code" for the database
#need to set to another data structure not just a txt file
#the hash will come from a server

args, parser = dbfs_parser.prog_parser()
def dbfs_auth():
    file_name = 'config/dbfs_config.py'

    folder_path = os.path.expanduser("~/.dbfs")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print('You must add your passcode to the dbfs.config file with set command.')
        try:
            with open(file_name, 'w') as file:
                    file.write(f"link_code={args.link}")
                    print('File created successfully.')
        except Exception as e:
                print('An error occurred:', str(e))

    else:
         if args.link:
            try:
                with open(file_name, 'w') as file:
                    file.write(f"link_code='{args.link}'")
                    print('File created successfully.')
            except Exception as e:
                print('An error occurred:', str(e))

