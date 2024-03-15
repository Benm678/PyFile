import csv
import os
import shutil

def get_folder_structure(filepath):

    return os.path.normpath(filepath).split(os.sep) 

def copy_files_from_csv(csv_path, destination_path):

    copied_count = 0
    error_count = 0
    error_list = []

    with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            filenames = [filename for filename in row[4:] if filename]  #Take all csv columns 5+ sp don't need to move kept files to column 5

            for filename in filenames:
                try:
                    folder_structure = get_folder_structure(filename)
                    relative_path = os.path.join(*folder_structure[1:])  # Exclude the root folder
                    destination_file = os.path.join(destination_path, relative_path)
                    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                    shutil.copy2(filename, destination_file)
                    print("File copied:", filename, "to", destination_file)
                    copied_count += 1
                except (FileNotFoundError, OSError) as e:
                    error_count += 1
                    error_list.append(filename)
                    print("Error copying", filename, ":", e)

    # Report statistics
    print("\nCopy Summary:")
    print("Files copied:", copied_count)
    print("Errors encountered:", error_count)

    # Write error list to a CSV file so have a record
    if error_list:
        error_report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "error_report.csv")
        with open(error_report_path, 'a', newline='', encoding='utf-8') as error_report:
            csv_writer = csv.writer(error_report)
            csv_writer.writerow(["Error Files"])
            csv_writer.writerows([[error] for error in error_list])
        print("\nError file paths written to", error_report_path)