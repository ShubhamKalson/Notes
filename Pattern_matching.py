import os
import re
import csv

data=[
    ["Reports","Views used"]
]
file_path='H:\\Documents\\Analysis\\Excel\\analysis.csv'
with open(file_path,mode='w',newline='') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerows(data)

DIR = "H:\\Documents\\Analysis\\reports"#path
entries = [entry for entry in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, entry))]

def read_text_file(f):
    with open(f,'r') as file:
        file_contents = file.read()
        file_name=os.path.basename(file.name)
        set1=set()
        set1.clear()
        query_searching=r'<CommandText>(.*?)</CommandText>'
        SQL_query=re.findall(query_searching,file_contents,re.DOTALL)
        final=""
        for query in SQL_query:
            final=query
        
        pattern=r'SRC\.(\w+)\.(\w+)\.(\w+)'
        matches=re.findall(pattern,final)
        
        for match in matches:
            database_name=match[0]
            table_name=match[1]
            view_used="SRC."+database_name+"."+table_name
            set1.add(view_used)
        
        pattern=r'SRC\.(\w+)\.(\w+)'
        matches=re.findall(pattern,final)
        for match in matches:
            database_name=match[0]
            table_name=match[1]
            view_used="SRC."+database_name+"."+table_name
            set1.add(view_used)

        with open(file_path,mode='a',newline='') as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow(" ")
            writer.writerow([file_name])
            
            for data in set1:    
                writer.writerow([data]) 

for file_name in os.listdir(DIR):
    if os.path.isfile(os.path.join(DIR,file_name)):
        read_text_file(os.path.join(DIR,file_name))

 
    
