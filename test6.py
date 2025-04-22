import csv

def convert_log_to_csv(log_file_path, csv_file_path, delimiter=' '):
    """
    Converts a GPS log file to a CSV file.

    Args:
        log_file_path (str): Path to the input GPS log file.
        csv_file_path (str): Path to the output CSV file.
        delimiter (str, optional): Delimiter used in the log file. Defaults to space.
    """
    try:
        with open(log_file_path, 'r') as infile, open(csv_file_path, 'w', newline='') as outfile:
            reader = csv.reader(infile, delimiter=delimiter)
            writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)
        print(f"Successfully converted '{log_file_path}' to '{csv_file_path}'")
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
log_file = 'gps_log2.txt'
csv_file = 'gps_data2.csv'
convert_log_to_csv(log_file, csv_file)