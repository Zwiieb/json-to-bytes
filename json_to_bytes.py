import json

if __name__ == '__main__':
    with open('data.json') as mon_fichier:
        data = json.load(mon_fichier)
    result = open('result.txt', 'w')
    txtBytes = open('txtBytes.txt', 'w')
    for i in data:
        a =str(data[i].to_bytes(8, byteorder='big',signed=True))
        txtBytes.write(a+"\n")

        a = a.replace("\\x","")
        a = a.replace("'", "")
        a = a[1:]
        result.write(a+"\n")
