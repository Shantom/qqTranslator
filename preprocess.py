import re

with open('source.txt', encoding='utf-8') as file:
    data = file.read()
    paras = data.split('\n')

    paraList = []
    print(len(paras))
    for data in paras:
        if data.strip():
            data = re.split(r"([.。!！?？；;:：])", data)
            if len(data) > 1:
                data = ["".join(i) for i in zip(data[0::2], data[1::2])]
            data[-1] += '^p'
            paraList.append(data)

    with open('preprocessed.txt', 'w', encoding='utf-8') as tar:
        for data in paraList:
            for line in data:
                line = line.strip()
                tar.write(line + '\n')
