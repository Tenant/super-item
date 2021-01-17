import os

frame_cnt = 0


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
    t_max = 60 * 60 * 24
    t = (ss % t_max + 60 * 60 * 8) * 1000 + us // 1000
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

def split_pcap_file(fn):
    out_info = []
    with open(os.path.join(root, fn), 'rb') as f:
        pcap_header = read_pcap_header(f)
        if not pcap_header:
            return
        out_info.append(pcap_header)
        while True:
            p_data = f.read(16)
            if len(p_data) < 16:
                break
            else:
                s_seconds = read_uint32(p_data,0)
                u_seconds = read_uint32(p_data,4)
                m_seconds = convert_unix_to_local(s_seconds, u_seconds)
                data_len = read_uint16(p_data, 12)
                if m_seconds > tail:
                    break
                if data_len > 0:
                    if head <= m_seconds <= tail:
                        out_info.append(p_data)
                    p_data = f.read(data_len)
                    if head <= m_seconds <= tail:
                        out_info.append(p_data)
                print(s_seconds + u_seconds / 1000000, m_seconds, data_len)
    with open(os.path.join(outdir, fn), "wb") as f:
        for _info in out_info:
            f.write(_info)
    print("Create file: {}".format(os.path.join(outdir, fn)))

def split_csv_file(fn):
    out_info = []
    with open(os.path.join(root, fn), "r") as f:
        lines = f.readlines()
        out_info.append(lines[0].split("\n")[0].strip())
        for i in range(1, len(lines)):
            cur_time = int(lines[i].split(",")[0].strip())
            if head <= cur_time <= tail:
                out_info.append(lines[i].split("\n")[0].strip())
    with open(os.path.join(outdir, fn), "w") as f:
        f.write("\n".join(out_info))
    print("Create file: {}".format(os.path.join(outdir, fn)))



if __name__ == "__main__":
    root = "E:/KYXZ2020/G/data/data_20201010/data-RTK-5"
    head, tail = 54350101, 54410101
    outdir = os.path.join(root, "split-data_{}-{}".format(head, tail))
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(root):
        if f.split(".")[-1] == "pcap":
            split_pcap_file(f)
        if f.split(".")[-1] == "csv":
            split_csv_file(f)

# print("frame count: {}".format(frame_cnt))