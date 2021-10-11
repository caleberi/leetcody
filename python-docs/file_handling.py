import sys
from random  import randint
import pickle

_file_object = None

def count_file_lines(path):
    file =  open("input.txt","r")
    count = 0
    # while file.readline()!='':
    #     count+=1
    #OR
    for line in file:
        count+=1
    file.close();
    return count
    
def set_stdout(path,mode):
    global _file_object
    _file_object = open(path,mode)
    sys.stdout = _file_object

def reset_stdout():
    sys.stdout = sys.__stdout__

def reset_stdin():
    sys.stdout = sys.__stdin__
    
def reset_stderr():
    sys.stderr = sys.__stderr__
    
def set_stdin(path,mode):
    global _file_object
    _file_object = open(path,mode)
    sys.stdin = _file_object

def set_stderr(path,mode):
    global _file_object
    _file_object = open(path,mode)
    sys.stderr = _file_object


"""
mio module , (contains functions  capture_output ,restore_output 
    print_file , and clear_file )
"""




def  capture_output(file="capture_file.txt"):
    """redirect the standard output to capture_output.txt """
    global _file_object
    print("output will be sent to file : {0} ".format(file))
    print("restore to normal by calling  mio.restore_output()")
    set_stdout(file,"w")

def restore_output():
    """
    restore the standard output back to the default stdout
    """
    global _file_object
    reset_stdout()
    _file_object.close()
    print("standard output has been back to stdout (normal)")

def print_file(file="capture_file.txt"):
    """
    print the given file  to the stdout
    """
    set_stdout(file,"r")
    print(_file_object.read)
    _file_object.close()

def clear_file(file="capture_file.txt"):
    """
    clears the content of the file
    """
    global _file_object 
    _file_object = open(file,"w")
    _file_object.close()

mem_cache ={}

def sole(m,n,t,fn):
    if (m,n,t) in mem_cache:
        return mem_cache[(m,n,t)]
    else:
        # time-consuming operation
        result = fn(randint(1,1000))
        mem_cache[(m,n,t)] = result
        return result

_mem_disk_file = "mem_cache"
file = open(_mem_disk_file,"r")
mem_cache = pickle.load(file)
file.close()


def save_mem_to_disk():
    """
    save the mem_cache to disk
    """
    global mem_cache,_mem_disk_file
    file=open(_mem_disk_file,"w")
    pickle.dump(mem_cache,file)
    file.close()


def show_mem_cache():
    global mem_cache,_mem_disk_file
    print(_mem_disk_file)

    