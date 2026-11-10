import csv

regions = {}


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
            
            
    
    
except FileNotFoundError:
    print("Error: The original CSV file was not found. Please check the its path.")
    
except PermissionError:
    print("Error: Permission denied.")
    
except IOError:
    print("Error: an I/O error occured while reading or writing the file.")