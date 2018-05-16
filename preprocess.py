import re

with open('source.txt') as file:
    data = file.read()
    paras = data.split('\n')

    paraList = []
    print(len(paras))
    for data in paras:
        if data:
            data = re.split(r"([.。!！?？；;:：])", data)
            data = ["".join(i) for i in zip(data[0::2], data[1::2])]
            data[-1] += '^p'
            paraList.append(data)

    with open('preprocessed.txt', 'w') as tar:
        for data in paraList:
            for line in data:
                line = line.strip()
                tar.write(line + '\n')
