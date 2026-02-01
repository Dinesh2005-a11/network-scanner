import socket
def scan_port(ip,port):
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.settimeout(1)
  result=s.connect_ex((ip,port))
  s.close()
  if result==0:
    return True
  else:
    return False
def network_scan():
  target_ip=input("Enter target IP address:")
  common_ports=[21,22,23,80,443,8080]
  print(f"\n Starting scan on {target_ip}")
  print("-"*30)
  for port in common_ports:
    status=scan_port(target_ip,port)
    if status:
      print(f"Port{port}:OPEN")
    else:
      print(f"Port{port}:CLOSED")
  print("-"*30)
  print("Scan completed successfully")
network_scan()
      
  
