import ipaddress
import socket

# port = [21, 23, 80, 443, 8080]
# portnum = 8080
# address = '10.0.0.125'
portnum = 80
address = 'google.com'
# for ip in ipaddress.IPv4Network('192.168.1.0/24'):
#     print(ip)

def getservice(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return None

def scanport(addr, port):
    socket.setdefaulttimeout(1)
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = socket_obj.connect_ex((addr, port))
    socket_obj.close()

    if result == 0:
        machine_hostname = socket.gethostbyaddr(addr)[0]
        # service = socket.getservbyport(port)
        service = getservice(port)
        print(f'{addr} {port} {machine_hostname} {service}')
        # return port
    else:
        return None

scanport(address, portnum)


# def bannergrabbing(addr, port):
#     '''Connect to process and return application banner'''
#     print("Getting service information for port: ", port)
#     socket.setdefaulttimeout(2)
#     bannergrabber = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     bannergrabber.connect((addr, port))
#     # try:
#     # bannergrabber.connect((addr, port))
#     # bannergrabber.send('WhoAreYou\r\n')
#     bannergrabber.send(b"GET / HTTP/1.1\r\n\r\n")
#     # message = "GET / HTTP/1.1\r\n\r\n"
#     # bannergrabber.sendall(message)
#     banner = bannergrabber.recv(1024)
#     print(banner, "\n")
#     bannergrabber.close()
#     # except:
#     #     print("Cannot connect to port ", port)

# bannergrabbing(address, portnum)