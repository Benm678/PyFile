import csv
import os
import stat

def delete_files_from_csv(csv_path):
    with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            filenames = row[4:]  # Assuming filenames are in columns 5 and onwards
            for filename in filenames:
                try:
                    # Ensure the file is not read-only
                    os.chmod(filename, stat.S_IWRITE)
                    os.remove(filename)
                    print(f"File deleted: {filename}")
                except FileNotFoundError:
                    print(f"File not found: {filename}")
                except Exception as e:
                    print(f"Error deleting {filename}: {e}")

if __name__ == "__main__":
    csv_path = input("Enter the path to the CSV file: ")
    delete_files_from_csv(csv_path)
