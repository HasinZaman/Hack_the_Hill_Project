import random
import json

filename = './generated.json'


def parser(name):
    fcc_data = None
    with open(filename, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
    # print(type(fcc_data))
    # print(fcc_data)
    for i in fcc_data:
        if name == i["name"]:
            rand=random.randint(0,len(i["purchase"]))
            return i["purchase"][rand]["product_category"]

    return ""


print(parser("Lucile Roman"))
