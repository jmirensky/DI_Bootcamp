import sys
from tabulate import tabulate

def extract_file_contents(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def display_files(file1_contents, file2_contents):
    table = {
        "file1": file1_contents,
        "file2": file2_contents
    }
    print(tabulate(table))

def main(file1, file2):
    file1 = extract_file_contents(file1)
    file2 = extract_file_contents(file2)

    display_files(file1, file2)

    dates = sorted(set(file1).union(file2))
    print("\nFecha mediana:")
    print(dates[len(dates) // 2])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usá: python main.py datefile1.txt datefile2.txt")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])