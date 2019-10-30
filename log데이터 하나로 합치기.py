import pandas as pd
import numpy as np
import os


directory = 'Data/log/'
outfile_name = 'merged_MeterHour.log'

out_file = open(outfile_name, 'w')
files = os.listdir(directory)


for filename in files:
    if ".log" not in filename:
        continue
    file = open(directory + filename)
    for line in file:
        out_file.write(line)
    out_file.write('\n\n')
    file.close()
out_file.close()