import requests
import hashlib
import hmac
import base64
import random
import time

secretKey = ''
secretID = ''
with open('keys.txt', encoding='utf-8') as keys:
    secretID = keys.readline().strip()
    secretKey = keys.readline().strip()


class Translator:
    def __init__(self, key, id):
        self.secretKey = key
        self.payload = {
            "Action": "TextTranslate",
            "Nonce": '1',
            "ProjectId": '0',
            "Region": "ap-guangzhou",
            "SecretId": id,
            "SignatureMethod": "HmacSHA256",
            "Source": "en",
            "SourceText": "hello",
            "Target": "zh",
            "Timestamp": '1',
            "Version": '2018-03-21'
        }

    def conta(self, data):
        dataList = []
        for key, value in data.items():
            str = key + '=' + value
            dataList.append(str)
        dataList.sort()
        dataStr = '&'.join(dataList)
        return dataStr

    def genSig(self):
        self.payload['Nonce'] = str(random.randint(1, 2147483647))
        self.payload['Timestamp'] = str(int(time.time()))
        message = 'GETtmt.tencentcloudapi.com/?' + self.conta(self.payload)
        M = message.encode(encoding="utf-8")
        S = self.secretKey.encode(encoding="utf-8")

        signature = base64.b64encode(hmac.new(S, M, digestmod=hashlib.sha256).digest())
        self.payload['Signature'] = signature.decode()

    def start(self, text):
        self.__init__(self.secretKey,self.payload["SecretId"])
        self.payload['SourceText'] = text
        self.genSig()
        res = requests.get('https://tmt.tencentcloudapi.com/', self.payload)
        print(res.json()['Response'])
        return res.json()['Response']['TargetText']


time_start = time.time()

T = Translator(secretKey, secretID)

with open('preprocessed.txt', encoding='utf-8') as inFile:
    with open('tobechecked.md', 'w', encoding='utf-8') as outFile:
        for line in inFile:
            paraEnd = ''
            if line.strip().endswith('^p'):
                paraEnd = '^p'
                line = line.replace('^p', '')
            transed = T.start(line.strip())
            sentence = line + '>' + transed + paraEnd + '\n\n'
            outFile.write(sentence)

time_end = time.time()
print('用时：', time_end - time_start, 's')
