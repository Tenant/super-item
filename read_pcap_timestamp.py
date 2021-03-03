import sys

def read_uint16(data, idx):
  return data[idx+1]*256 + data[idx+0]

def read_uint32(data, idx):
  return data[idx+3]*256*256*256 + data[idx+2]*256*256 + data[idx+1]*256 + data[idx+0]

def read_uint64(data, idx):
  return read_uint32(data, idx+4)*256*256*256*256 + read_uint32(data, idx)

def read_sint32(data, idx):
  val = data[idx+3]*256*256*256 + data[idx+2]*256*256 + data[idx+1]*256 + data[idx+0] 
  return val-2**32 if val > 2**31-1 else val

def convert_unix_to_local(ss, us):
    ss = ss + 8 * 3600
    t_max = 60 * 60 * 24 
    t = (ss % t_max) * 1000 + us // 1000
    return t

def read_pcap_header(f):
    p_data = f.read(24)
    if len(p_data) < 24:
        return False
    if p_data[0:4] == b'\xd4\xc3\xb2\xa1':
        version_major = read_uint16(p_data, 4)
        version_minor = read_uint16(p_data, 6)
        thiszone = read_sint32(p_data, 8)
        timestamp = read_uint32(p_data, 12)
        print("version: {}.{}".format(version_major, version_minor))
        print("timezone: {}".format(thiszone))
        print("timestamp: {}".format(timestamp))
        return p_data
    else:
        print("This is not a pcap file") 
        return None

def read_pcap_file(fn):
    out_info = []
    with open(fn, 'rb') as f:
        pcap_header = read_pcap_header(f)
        if not pcap_header:
            return
        while True:
            p_data = f.read(16)
            if len(p_data) < 16:
                break
            else:
                s_seconds = read_uint32(p_data,0)
                u_seconds = read_uint32(p_data,4)
                m_seconds = convert_unix_to_local(s_seconds, u_seconds)
                data_len = read_uint16(p_data, 12)
                if data_len > 0:
                    p_data = f.read(data_len)
                out_info.append(m_seconds)
                # print(s_seconds + u_seconds / 1000000, m_seconds, data_len)
    with open("timestamp.csv", "w") as f:
        for t in out_info:
            f.write(str(t) + "\n")

if __name__ == '__main__':
    read_pcap_file(sys.argv[1])