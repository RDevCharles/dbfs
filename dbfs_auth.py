import dbfs_parser
import os

def dbfs_auth():
    folder_path = os.path.expanduser("~/.dbfs")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print('Folder created successfully.')
  

    file_name = 'dbfs.config'
    file_path = os.path.join(folder_path, file_name)

    args, parser = dbfs_parser.prog_parser()

    try:
        with open(file_path, 'w') as file:
            file.write('Hello, world!')
            print('File created successfully.')
    except Exception as e:
        print('An error occurred:', str(e))


    
    #auth place holder
    #needs to be replaced with actual authentication
    if args.set == "username":

        print("username set to: " + args.set)

    elif args.set == "password":
        print("password changed")

