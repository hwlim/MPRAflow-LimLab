#!/usr/bin/env python3

'''
Written by:
    Christopher Ahn
    Hee Woong Lim
Description:
    Print contents of coords_to_barcodes pickle_file to STDIO in the format:
    <CRS name>::<barcode
'''

import pickle
import sys


def print_dict_value_len(pickle_file):
    ## Attempt to load the pickle file
    try:
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)
    except (pickle.UnpicklingError, EOFError, AttributeError, ValueError) as e:
        print(f"Error: input file is not a pickle file.")
        return

        ## loop through all keys
    for key, value in data.items():
        for bcd in value:
            print( key + "::" + bcd )

## main
if __name__ == "__main__":
    ## check command line format
    if len(sys.argv) != 2:
        print("Usage: python mpra.print_coords_to_barcodes.py <pickle_file>")
    else:
        pickle_file = sys.argv[1]
        '''
        pickle_file="Example_coords_to_barcodes.pickle"
        '''


        print_dict_value_len(pickle_file)
