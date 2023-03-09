"""
    Input: two paths (path1, path2). Path1 has an input file named file.csv.
    Objective:  To write a function
    Transform(path1, path2) that does the following
    Read the CSV file from path1
    Remove all duplicate rows keeping only the first row based on column1
    Sort the whole file datewise descending order on column2
    Copy the existing data of the maximum date from column2 and change the date to today's date and append it to the file
    Change the date format of the entire file to dd-mm-yyyy
    Write the file to path2
"""

## Notes

# we could use a list instead of a set to keep track of the rows we've already seen. However, using a set can make the duplicate checking process more efficient for large datasets.

# The reason for this is that sets have a constant time complexity for adding and checking membership, whereas lists have a linear time complexity. Therefore, as the number of rows in the CSV file increases, using a set to check for duplicates will become faster than using a list.


import csv
from datetime import datetime as dt

def transform(path1,path2):
    
    with open(path1, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        rows = [row for row in reader]
    
    unique_rows = []
    # visited_rows = [] # O(n) -> checking, adding
    visited_rows = set()  # O(1) -> checking, adding
    for row in rows:
        if row[0] not in visited_rows:
            unique_rows.append(row)
            visited_rows.add(row[0])
            
    # Sort the whole file datewise descending order on column2
    sorted_rows = sorted(unique_rows, key=lambda row: dt.strptime(
        row[1], '%d-%b-%y'), reverse=True)
    
    # Copy the existing data of the maximum date from column2 and change the date to today's date and append it to the file
    today_date = dt.today().strftime('%d-%b-%y')
    new_row = [sorted_rows[0][0], today_date , sorted_rows[0][2]]
    sorted_rows.append(new_row)
    
    # Change the date format of the entire file to dd-mm-yyyy
    for row in sorted_rows:
        row[1] = dt.strptime(row[1], '%d-%b-%y').strftime('%d-%m-%Y')
    
    with open(path2, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','Date','value'])
        writer.writerows(sorted_rows)
  
path1 = './file.csv'  
path2 = './output.csv'      
transform(path1,path2)