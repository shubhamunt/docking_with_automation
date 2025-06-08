'''This script is prepared by Kartikay Prasad, and it is a part of the course teaches by Kartikay.

***************************************
Script Usage:
            pyhton3 python_file_name.py input_file_having_list_of_drug_name.txt input_file_format output_file_format

***************************************
This is how input_file_having_list_of_drug_name.txt must  look like:
1.sdf
2.sdf
3.sdf

***************************************
Sample command for above file to covert sdf files into pdbqt
            pyhton3 python_file_name.py input_file_having_list_of_drug_name.txt sdf pdbqt
This command will convert all the sdf files into pdbqt format
'''

import os
import sys
if __name__ == "__main__":
    try:
        c_dir = os.getcwd()
        input_file = sys.argv[1]
        input_file_format = sys.argv[2]
        output_file_format = sys.argv[3]
        f = open(input_file)
        for lines in f:
            line_data = lines.strip()
            line_data_splitting = line_data.split(".")
            drug_name = line_data_splitting[0]
            out_file_name = drug_name + "." +output_file_format
            os.system(f"obabel -i{input_file_format} {line_data}  -o{output_file_format} -O{out_file_name} --gen3d -d")
            os.chdir(c_dir)

    except Exception as e:
        print(f"Check your input file format, or check if the tool is installed properly. Also check whether the  OS and SYS libraries of python is installed\n")
