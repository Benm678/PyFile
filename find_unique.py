import os
import csv

from collections import defaultdict


def find_unique_files(start_path):
    
    file_info_dict = defaultdict(list) #defaultdict here as will be appending unknown filenames later
    total_files = 0 #to report on total no of files checked
    
    for root, dirs, files in os.walk(start_path): #dirs is required by os.walk but not used here
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            file_info_dict[(name, file_size)].append(file_path)
            total_files += 1
            print("\rFiles checked", total_files, end="", flush=True)

    unique_files = [files for files in file_info_dict.values() if len(files) == 1]
    print("\nTotal unique files found:", len(unique_files))
    
    return unique_files


def write_to_csv(unique_files, output_csv=os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "UniqueFiles.csv")):
    
    with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write headers
        headers = ["filename", "size", "date modified", "type", "path"]
        csv_writer.writerow(headers)
        file_number = 0

        for files in unique_files:
            filename = os.path.basename(files[0]) #[0] to get the item from the list
            size = os.path.getsize(files[0])
            date_modified = os.path.getmtime(files[0])
            file_type = os.path.splitext(filename)[1] #included type to allow for sorts in excel
            row_data = [filename, size, date_modified, file_type, files[0]]
            csv_writer.writerow(row_data)
            file_number += 1
            print("\rWriting", file_number, end="", flush=True)


def generate_unique(start_path):
    start_path = os.path.normpath(start_path)
    unique_files = find_unique_files(start_path)

    if unique_files:
        write_to_csv(unique_files)
        print("\nUnique files information written to UniqueFiles.csv.                                                          ") 