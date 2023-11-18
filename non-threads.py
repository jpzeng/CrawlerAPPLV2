import requests
import re
import time

#抓取若干页面
def crawler(arg):
    for g in arg:
       print(g)
       try:
         r=requests.get(g)
       except:
         print("skip")
         continue #忽略异常网页，继续抓取下一个
             
def main():
    starttime = time.time()
    res=requests.get("https://www.fudan.edu.cn/")
    urls=re.findall(' href="http://[a-z0-9.\\/\?]+"',res.text)
    urls=[url[7:-1] for url in urls]
    print(len(urls))
    crawler(urls)
    endtime = time.time()
    print("完成所有抓取任务，总耗时：{}".format(endtime - starttime))

main()
