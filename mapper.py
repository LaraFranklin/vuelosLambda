#!/usr/bin/env python

# Use the sys module
import sys

# 'file' in this case is STDIN
def read_input(file):
    # Split each line into words
    for line in file:
        yield line.split(',')

def main(separator='\t'):
    # Read the data using read_input
    data = read_input(sys.stdin)
    #data = read_input(open('xaa.csv','r'))
    # Process each word returned from read_input
    datos = []
    
    for words in data:
        #datos.append(words)
        #print(datos)
        # Process each line
        if (words[15]!="DepDelay" and words[15] != "NA" and int(words[15])>0):
            key = words[3]+","+words[4]+","+words[10]+","+words[16]+","+words[17]
            valor = int(words[15])
            print '%s%s%d' % (key, separator, valor)
if __name__ == "__main__":
    main()