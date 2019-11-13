import sys 
import os 
import zipfile




nifty_50_namaes = os.listdir()

# months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

# zip_file_names = []
# for month in months:
#     for date in range(1,32):
#         zip_file_names.append(str(date)+month)
# print(zip_file_names)





def unzip_all(folder_path):
    print(folder_path)
    os.chdir(folder_path)
    print(os.getcwd())

    count = 0
    for folder in os.listdir(folder_path):

        # make sure the folder is not itself a zip file 
        if not folder.endswith("zip"):        
            sub_folder = os.path.join(folder_path, folder)
        else:
            # continue for the moment 
            continue

        os.chdir(sub_folder)
        count += 1
        for zipfiles in os.listdir(sub_folder):
            print(zipfiles)
            if zipfiles.endswith(".zip"):
                full_path = os.path.join(sub_folder, zipfiles)
                print(full_path)


                # now unzip the zip file 
                with zipfile.ZipFile(full_path, 'r') as zip_ref:
                    zip_ref.extractall(zipfiles[:-4])
        # change the directory 
        # os.chdir(folder)
        # get back to parent folder 
        os.chdir("..")


def unzip_nifty50(folder_path):

    for files in os.listdir(folder_path):

        
        if not files.endswith(".zip"):
            # it's a month folder 
            
            sub_folder = os.path.join(folder_path, files)
            os.chdir(sub_folder)

            for sub_files in os.listdir("."):
                if not sub_files.startswith("NIFTY50"):
                    continue
                print(sub_files)


                # this is a nifty file for the month 
                full_path = os.path.join(sub_folder,sub_files)
                print(full_path)

                 # now unzip the zip file 
                with zipfile.ZipFile(full_path, 'r') as zip_ref:
                    zip_ref.extractall(full_path[:-4])

                break



# unzip_all(r"C:\Users\as250199\nifty50\oneminutedata\2018")
unzip_nifty50(r"C:\Users\as250199\nifty50\oneminutedata\2018")