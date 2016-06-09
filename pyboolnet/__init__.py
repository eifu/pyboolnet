from os import listdir
from os.path import isfile, join
import numpy as np
import csv

class Pyboolnet(object):
    def __init__(self, data_path):
        self.names = [n for n in listdir(data_path) if isfile(join(data_path, n))]



        self.nodes = [Node(data_path,n) for n in self.names]        
            
class Node(object):
    def __init__(self, data_path, name):
        self.name = name
        f_path =data_path+"/"+name
        self.neighbors = np.genfromtxt(f_path,
                                        skip_header=0,
                                        delimiter=' ',
                                        dtype='|S16')[0][:-1]
        
        _rules = np.genfromtxt(f_path,delimiter=' ',dtype=int)[1:] 
       
        self.rules = np.zeros(pow(2, len(self.neighbors)),dtype=bool)
       
        for i, r in enumerate(_rules):
            self.rules[i] = r[-1]
     
        
