import csv

regions = {}


# CIS 117 Python Lab 3
# Python script that reads country names and regions from a CSV file and writes them to separate CSV files by region.
# Author: Sean Coffin and Leonard Ferreira
# Leonard Ferreira wrote the reading and the exception handling parts of the script. Sean Coffin wrote the documentation and the writing portion of the script.

try: 

    with open ("country_full.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv. DictReader(file)
        
        
        for row in reader:
            country = row["name"]
            region = row["region"]
            
            if region == "":
                continue
            
            if region not in regions:
                regions[region] = []
                
            regions [region].append(country)

        for region, countries in regions.items():
            filename = f"{region}.csv"
            with open(filename, "w", encoding="utf-8", newline="") as wf:
                writer = csv.writer(wf)
                writer.writerow(["country", "region"])
                for country in countries:
                    writer.writerow([country, region])

        print("CSV files have been created successfully.")
            
    
    
except FileNotFoundError:
    print("Error: The original CSV file was not found. Please check the its path.")
    
except PermissionError:
    print("Error: Permission denied.")
    
except IOError:
    print("Error: an I/O error occured while reading or writing the file.")