import os
import sys

def get_all_files(path, avoid_list):
    file_list = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in avoid_list]
        for file in files:
            if file not in avoid_list:
                file_list.append(os.path.join(root, file))
    return file_list

def read_avoid_list():
    avoid_list_file = "avoid.txt"
    try:
        with open(avoid_list_file, "r") as file:
            avoid_list = file.read().splitlines()
    except FileNotFoundError:
        avoid_list = [
            "node_modules",
            "package-lock.json",
            "package.json",
            ".DS_Store",
            ".env",
            ".git",
            ".gitattributes",
            ".gitignore",
            "LICENSE"
        ]
    return avoid_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_directory>")
        sys.exit(1)

    path = sys.argv[1]  # Get the path from command-line arguments
    output_file = os.path.basename(os.path.abspath(path)) + '_combined_code.txt' # Change this to your desired output file name
    separator = '#################### FILE: {file_path} \n'

    avoid_list = read_avoid_list()
    all_files = get_all_files(path, avoid_list)
    with open(output_file, 'w') as output:
        for file_path in all_files:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                output.write(separator.format(file_path=file_path))
                output.write(content)
                output.write('\n\n')
            except Exception as e:
                print(f'Error processing file {file_path}: {e}')

if __name__ == '__main__':
    main()
