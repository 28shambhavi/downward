import networkx as nx
import numpy as np
import random 
import matplotlib.pyplot as plt
import pdb

def get_dependency_graph():
    pass

def main():
    # read lines from file
    with open('/home/biorobotics/downward/termes_plan1/sas_plan.1', 'r') as f:
        for line in f:
            line = f.readline()
            print(line)
            print("\n")

if __name__ == '__main__':
    main()