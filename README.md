Combine Structure Code
======================

This Python script allows you to combine multiple source code files into a single file, and then split them back into their original files. It can be useful for simplifying the deployment process for your code. I use it to send my entire application code to ChatGPT.

Requirements
------------

*   Python 3

Usage
-----

### Combining Files

To combine multiple files into a single file, run the following command:

    python combined_code.py <path_to_directory>
    

This will create a new file in the same directory as the `combined_code.py` script with the name `<directory_name>_combined_code.txt`, where `<directory_name>` is the name of the directory containing the code files.

The script will search for all files in the specified directory (and its subdirectories), except for those listed in the `avoid.txt` file. The avoid list is a list of file names and directories that should be excluded from the search.

### Splitting Files

To split the combined file back into its original files, run the following command:

    python structure_code.py
    

This will take the `payment-template_combined_code.txt` file (or the file specified in the `input_file` variable) and split it back into its original files. The script will create any necessary directories and write the contents of each file to its original file path.

Configuration
-------------

### Avoid List

To configure the avoid list of files and directories, edit the `avoid.txt` file. By default, the avoid list contains the following files and directories:

*   node\_modules
*   package-lock.json
*   package.json
*   .DS\_Store
*   .env
*   .git
*   .gitattributes
*   .gitignore
*   LICENSE

### Output File Name

To change the name of the output file when combining files, edit the `output_file` variable in the `combined_code.py` script.
