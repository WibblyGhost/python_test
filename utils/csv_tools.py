import csv
import os


def csv_reader(file_path: str) -> list:
    """
    Reads a CSV file....
    """
    table = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file_instance:
            writer = csv.reader(file_instance)
            for row in writer:
                table.append(row)
    return table
