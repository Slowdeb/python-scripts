import socket

target = input("Enter an IP address to scan: ")
port_range = input("Enter the port range to scan (ex 0-200): ")

lowport = int(port_range.split('-')[0])
highport= int(port_range.split('-')[1])

print('Scanning host ', target, 'from port ', lowport, 'to port ', highport)

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if (status == 0):
        print('*** Port', port, '- OPEN ***')
    else:
        print('Port', port, 'CLOSED')
    s.close()
