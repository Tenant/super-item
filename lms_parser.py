import struct

def check_urg(fn):
    # timestampe: long, uint32
    # data: uint16 * bim numbers
    with open(fn, "rb") as f:
        p_data = f.read(4)
        if len(p_data) < 4:
            print("Cannot open file")
            return
        ang_range = struct.unpack('<f', p_data)[0] # ang range: float, 4 byte, = 180 degreee
        p_data = f.read(4)
        ang_resol = struct.unpack('<f', p_data)[0] # ang resolution: float, 4 byte, = 0.125 degree
        p_data = f.read(4)
        unit = struct.unpack('<f', p_data)[0] # unit: float, 4 byte, = 100
        print("angle range: {}, angle resolution: {}, unit: {}".format(ang_range, ang_resol, unit))
        bim_numbers = int(ang_range // ang_resol) + 1
        print("bim number: {}".format(bim_numbers))
        while True:
            p_data = f.read(4)
            if len(p_data) < 4:
                break
            timestamp = struct.unpack('<l', p_data)[0]
            p_data = f.read(bim_numbers * 2)
            print(timestamp)

check_urg(r".\URG.lms")
