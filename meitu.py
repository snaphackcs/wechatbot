from json import load
from os.path import exists, join
from requests import get
from pprint import pprint
from os import mkdir, getcwd
from json import dump


# 爬虫函数
def erciyuan():
    print("enter")

    path_list = []
    # 新建文件夹
    if not exists(r".\temp"):
        mkdir("temp")
    # 新建原始json

    # headers用于伪装成浏览器爬取图片
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 '
                      'Safari/537.36 '
    }
    # 打开json文件

    # api网址
    api_url = 'http://api.ooomn.com/api/ag?type=img'
    # 发送参数并请求色图信息
    response = get(api_url, headers=headers)
    # 将色图信息转为字典
    img_content = get(api_url, headers=headers).content

    with open(f"./temp/2.jpg", mode="wb") as f:
        f.write(img_content)

    path_list.append(join(getcwd(), f"temp\\2.jpg").replace("\\", "/"))
    print(path_list)
    return path_list


