# Objective
# Merge a set of sorted files of different length into a single sorted file. 
# We need to find an optimal solution, where the resultant file will be generated in minimum time.
# Approach
# If the number of sorted files are given, there are many ways to merge them into a single sorted file.
# This merge can be performed pair wise.To merge a m-record file and a n-record file requires possibly m+n record moves,
# the optimal choice being, merge the two smallest files together at each step (greedy approach).
from os import stat,path,getcwd
import os

from sys import getfilesystemencoding
from collections import deque

def resolve_os_encoding(path):
    return os.fsdecode(path) if getfilesystemencoding() != "utf-8" else path

def get_file_info(filename):
    file_path = path.join(getcwd(),filename)
    file_stat = stat(file_path)
    word_count = 0
    file_size = file_stat.st_size
    file = open(file_path)
    for line in file.readlines():
        word_count+=len(line.split())
    file.close()
    return (word_count,file_size,file_path)


def get_file_stats(file_list):
    stats = []
    for file in file_list:
        stats.append(get_file_info(file))
    return stats



def merge_files(file_list,dest_file):
    file_stats = get_file_stats(file_list)
    file_stats = sorted(file_stats,key=lambda s: s[1],reverse=True)
    queue =  deque(file_stats)
    while len(queue) > 1:
        largest = queue.popleft()
        smallest = queue.pop()
        with open(largest[2],"a")  as fs:
            small_file = open(smallest[2])
            fs.write("\n")
            fs.writelines(small_file.readlines())
            small_file.close()
        os.unlink(smallest[2])
        queue.appendleft(get_file_info(largest[2]))
    

if __name__ == "__main__":
    merge_files([
        "merge_files/a.txt",
        "merge_files/b.txt",
        "merge_files/c.txt"]
    ,"merge_files/result.txt"
)





    


