import json
import struct

import bitstring as bitstring
import byte as byte

if __name__ == '__main__':
    with open('result.txt') as mon_fichier:
        data = mon_fichier.readlines()
    result = open('result.json', 'w')
    #result.write("{ \"x\":"+str(int(data[0].replace('\n', ""),16))+", \"y\":"+str(int(data[1].replace('\n', ""),16))+", \"z\":"+str(int(data[2].replace('\n', ""),16))+", \"m\":"+str(int(data[3].replace('\n', ""),16))+"}")
    #result.write("{ \"x\":"+str(int.from_bytes(data[0].replace('\n', ""),"big",signed=True))+", \"y\":"+str(int.from_bytes(data[1].replace('\n', ""),"big",signed=True))+", \"z\":"+str(int.from_bytes(data[2].replace('\n', ""),"big",signed=True))+", \"m\":"+str(int.from_bytes(data[3].replace('\n', ""),"big",signed=True))+"}")(
    #bit = bitstring.Bits(uint=byte, length=8)
    #print(struct.unpack("<L", bytes(data[0],'utf - 8'))[0])
    #print(int.from_bytes(bytes(data[1]),"big",signed=True))

    str_1 = str(int.from_bytes(bytes.fromhex(data[0]), "big",signed=True))
    str_2 = str(int.from_bytes(bytes.fromhex(data[1]), "big",signed=True))
    str_3 = str(int.from_bytes(bytes.fromhex(data[2]), "big",signed=True))
    str_4 = str(int.from_bytes(bytes.fromhex(data[3]), "big",signed=True))
    result.write("{ \"x\":"+str_1+", \"y\":"+str_2+", \"z\":"+str_3+", \"m\":"+str_4+"}")


