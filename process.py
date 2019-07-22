from collections import namedtuple
import os
import re

path = './process_directory/'

def main():
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    for f in files:
        # Processing Each file data put it in array
        company_data = []
        with open(f, "r") as f:
            # Reading a company text file line by line
            contents = f.readlines()
            header = contents[0].strip() # Extracting Headers of the file
            header = re.sub(r'\s+', ', ', header) # Cleaning the data
            
            # Creating a lightweight object type for company info
            # where class properties like Date, CompanyName, Volume, Open, High etc. would be available
            Company = namedtuple('Company', header) 
            for item in contents[1:]:
                item = re.sub(r'\s+', ' ', item.strip()).split()
                # Storing each company object details to array
                c = Company(*item)
                company_data.append(c)
            # Here, We get the each company info in Object oriented fashion.
            # Now user either can store into DB or call 3rd party API
            # for this example I am printing the data
            print(company_data)

if __name__ == "__main__":
    main()

