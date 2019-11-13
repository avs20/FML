import os 
import sys 
import pandas as pd


# get a list of stocks 
demo_folder_for_stock_list = r"C:\Users\as250199\nifty50\oneminutedata\2017\APR\NIFTY50_APR2017\NIFTY50_APR2017"

company  = []

for files in os.listdir(demo_folder_for_stock_list):
    if files.endswith(".txt"):
        stock_name = files[:-4]
        company.append(stock_name)

# now for each of the company , go in all folders
# search for the file with that name and if present add it to its'
# dataframe, then save a CSV file. 

# start_folder = r"C:\Users\as250199\nifty50\oneminutedata\2017"

# columns =  ["STOCK","DATE","TIME", "OPEN","HIGH", "LOW","CLOSE", "VOLUME" ]

# now do a recursive search of folders and 
root_folder = r"C:\Users\as250199\nifty50\oneminutedata\2018"

count = 0 
part = 0 

full_dataset = pd.DataFrame([], columns = columns)

for root, dirs, files in os.walk(root_folder):
    # print(files)
    count += 1
    
    if not root[49:].startswith("NIFTY50")  :
        continue

    # print(dirs)
    print(root[49:])
    


    for _file in files:
        if _file.endswith(".txt"):
            # add it to dataframe 
            full_path = os.path.join(root_folder, root, _file)
            print(full_path)
            df = pd.read_csv(full_path, names=columns, header = None)
            count += len(df)
            if (len(full_dataset) == 0):
                full_dataset = df
            else:
                full_dataset = pd.concat([full_dataset, df])
            # print(full_dataset.head())
            

    if count > 100000:
        # save the iteration
        part += 1
        
        full_dataset.to_csv("full_dataset_2017_part_{}.csv".format(str(part)), index=False)
        full_dataset = pd.DataFrame([], columns = columns)
        count = 0 


# after everything save the CSV file


# now merge all the part datasets 

allfiles = []
full_dataset = pd.DataFrame()
for files in os.listdir("."):

    # print(files)
    
    if files.find("part") > 0:
        print(files)

        df = pd.read_csv(os.path.join(os.getcwd(), files))

        if(len(full_dataset) == 0):
            full_dataset = df
        else:
            full_dataset = pd.concat([full_dataset,df])

        



full_dataset.to_csv("all_dataset_2017.csv", index=False)