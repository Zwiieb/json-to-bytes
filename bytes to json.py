if __name__ == '__main__':
    
    # input file
    with open('result.txt') as mon_fichier:
        data = mon_fichier.readlines()
        
    # output file
    result = open('result.json', 'w')
    
    # return var
    str_1 = str(int.from_bytes(bytes.fromhex(data[0]), "big",signed=True))
    str_2 = str(int.from_bytes(bytes.fromhex(data[1]), "big",signed=True))
    str_3 = str(int.from_bytes(bytes.fromhex(data[2]), "big",signed=True))
    str_4 = str(int.from_bytes(bytes.fromhex(data[3]), "big",signed=True))
    
    result.write("{ \"x\":"+str_1+", \"y\":"+str_2+", \"z\":"+str_3+", \"m\":"+str_4+"}")


