import os

home_dir= "D:\\folder\\home"            # directory of the files needed to be checked
unique_dir= "D:\\folder\\unique"        # directory of the unique files
duplicate_dir= "D:\\folder\\duplicate"  # directory of the duplicate files

i=0
table=[]

for file_target in os.listdir(home_dir):
    h_name=file_target
    h_file_path = os.path.join(home_dir, h_name)
    u_file_path = os.path.join(unique_dir, h_name)
    d_file_path = os.path.join(duplicate_dir, h_name)
    h_size= os.stat(h_file_path).st_size

    if h_size in table:
        os.replace(h_file_path,d_file_path)     # move to duplicate folder

    try:
        os.replace(h_file_path,u_file_path)     # move to unique folder
        table.append(h_size)
    except FileNotFoundError:
        i += 1
        print(str(i) + " Duplicate(s) found!")