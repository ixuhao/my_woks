# -*- coding: utf-8 -*-
# http://www.blog.pythonlibrary.org/2014/01/27/python-201-an-intro-to-generators/

def process_file_differently(path):
    """
    Process the file line by line using the file's returned iterator
    """
    try:
        with open(path) as file_handler:
            while True:
                #print next(file_handler)
                print file_handler.next()
    except (IOError, OSError):
        print ("Error opening / processing file")
    except StopIteration:
        pass

if __name__ == '__main__':
    path = r"c:\Users\xuhao\Downloads\TB_data_dictionary_2014-02-21.csv"
    process_file_differently(path)
