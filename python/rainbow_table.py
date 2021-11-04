from hashlib import sha1

class RainbowTable():
    def __init__(self,input_file_name,out_file_name):
        self.input =  open(input_file_name,"r")
        self.output = open(out_file_name,"w")
        
    def parse_data(self):
        for line in self.input.readlines():
            line.split(" ")