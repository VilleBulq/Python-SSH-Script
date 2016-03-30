import socket

def test_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
       
        s.connect((host, port))

        s.close()

    except:

        return False

    return True

def portrange_to_list(portrange):
    ports = []
    numbers = portrange.split("-")
    first = int(numbers[0])
    second = int(numbers[1])
    return range(first, second+1)
   

    

   


ports = portrange_to_list("79-80")

for port in ports:
    if test_port("195.148.26.130", port) == False:
        print "Portti", port, "Kiinni"
       
    else:
        print "Portti", port, "Auki"

    
        
