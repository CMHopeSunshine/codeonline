import re
import requests

codeType = {
    'py': ['python', 'py'],
    'cpp': ['cpp', 'cpp'],
    'java': ['java', 'java'],
    'php': ['php', 'php'],
    'js': ['javascript', 'js'],
    'c': ['c', 'c'],
    'c#': ['csharp', 'cs'],
    'go': ['go', 'go'],
    'asm': ['assembly', 'asm']
}


async def run(strcode):
    try:
        a = re.findall(r'(py|php|java|cpp|js|c#|c|go|asm)', strcode[0])
    except:
        return "输入有误\n目前仅支持c/cpp/c#/py/php/go/java/js"
    if strcode[1][0:2] == "-i":
        strcode=strcode[1].split(' ',2)
        lang, code = a[0], strcode[2]
        dataJson = {
            "files": [
                {
                    "name": f"main.{codeType[lang][1]}",
                    "content": code
                }
            ],
            "stdin": strcode[1],
            "command": ""
        }
    else:
        lang, code = a[0], strcode[1]
        dataJson = {
            "files": [
                {
                    "name": f"main.{codeType[lang][1]}",
                    "content": code
                }
            ],
            "stdin": "",
            "command": ""
        }
    headers = {
        "Authorization": "Token 0123456-789a-bcde-f012-3456789abcde",
        "content-type": "application/"
    }

    res = requests.post(url=f'https://glot.io/run/{codeType[lang][0]}?version=latest', headers=headers, json=dataJson)
    if res.status_code == 200:
        if res.json()['stdout'] != "":
            if len(repr(res.json()['stdout'])) < 500:
                return res.json()['stdout']
            else:
                return "输出结果过长，仅显示前500：" + res.json()['stdout'][0:500]
        else:
            return res.json()['stderr'].strip()

