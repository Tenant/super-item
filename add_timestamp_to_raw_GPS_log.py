import sys

def process(infile, outfile):
    first_stamp = 0
    first_gps_stamp = 0
    lines = open(infile, "r").readlines()
    with open(outfile, "w") as logfile:
        for data_in in lines:
            if '$GPFPD' not in data_in: 
                continue
            sec = float(data_in.split(',')[2])
            if first_stamp == 0:
                first_stamp = (28386844 + 1476662400000) / 1000 # unit: second
                first_gps_stamp = sec
            t = first_stamp + (sec - first_gps_stamp)
            logfile.write(('%.6f,' % t) + data_in)

process("a-XW-20161017075306.log", "gpslog2016-10-18.log")
