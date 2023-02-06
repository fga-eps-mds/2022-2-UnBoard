import json
def altera_curso() -> str:
    file = open('./data.json')
    data = json.load(file)
    print(data)
    return data['curso']

def altera_ano() -> int:
    file = open('./data.json')
    data = json.load(file)
    print(data)
    return data['ano']
