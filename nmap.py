from netaddr import IPNetwork
# from tqdm import tqdm,trange
import sys
import socket 

progress = None
count = 0
# def showProgressBar():
#     global progress,count
#     progress.update(count)
#     count =0



if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("e.g. python3 nmap.py 192.168.0.0/24 1 65535 (port range)")
        sys.exit()
    ipRange = IPNetwork(sys.argv[1])
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    # progress = tqdm(total=len(ipRange)*(end-start))
    for ip in ipRange:
        print(f"scan {ip} ...")
        socket.setdefaulttimeout(0.00001)

        
        for port in range(start,end):
            count +=1
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            rs = s.connect_ex((str(ip),port))
            if rs ==0:
                print(f"    Port {port} is open")
        # showProgressBar()

    

