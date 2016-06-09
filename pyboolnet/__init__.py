from os import listdir
from os.path import isfile, join
import numpy as np
import csv

class Pyboolnet(object):
    def __init__(self, data_path):
        self.names = [n for n in listdir(data_path) if isfile(join(data_path, n))]

        print("len: ",len(self.names))

        self.nodes = [Node(data_path,n) for n in self.names]        
            
class Node(object):
    def __init__(self, data_path, name):
        self.name = name
        print(name)
        f_path =data_path+"/"+name
        self.neighbours = np.genfromtxt(f_path,skip_header=0, delimiter=' ',dtype='|S16')[0][:-1]
        
        self.rules = np.genfromtxt(f_path,delimiter=' ',dtype=int)[1:] 
        print(self.rules.shape)
        self.rules_array = np.zeros(pow(2, len(self.neighbours)),dtype=bool)
        print(self.rules_array.shape)
        for i, r in enumerate(self.rules):
            output = r[-1]
            self.rules_array[i] = output
        
        print("name  :", name)
        print("neighbours   :", self.neighbours)
        print("rules \n", self.rules)
        print("rule array\n",self.rules_array)
        
