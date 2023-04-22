import os

def create_directory(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    input_file = 'payment-template_combined_code.txt'  # Replace with your input file name
    separator = '#################### FILE: '
    
    with open(input_file, 'r') as input_file:
        content = input_file.read()
    
    file_blocks = content.split(separator)
    file_blocks = file_blocks[1:]  # Remove the first empty block

    for block in file_blocks:
        lines = block.split('\n')
        file_path = lines.pop(0).strip()  # Get the file path from the first line and remove it from the lines
        file_content = '\n'.join(lines[:-2])  # Rejoin the lines, excluding the last two empty lines

        create_directory(file_path)
        try:
            with open(file_path, 'w') as f:
                f.write(file_content)
        except Exception as e:
            print(f'Error processing file {file_path}: {e}')

if __name__ == '__main__':
    main()
