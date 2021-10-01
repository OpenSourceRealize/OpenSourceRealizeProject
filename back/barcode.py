import pyzbar.pyzbar as pyzbar


def barcode(img, decodedstr):
    decoded = pyzbar.decode(img)
    if decodedstr == "":
        if decoded != []:
            if len(decoded[0].data.decode('utf-8')) == 14:
                decodedstr = decoded[0].data.decode('utf-8')
                print(decodedstr)
    return decodedstr
