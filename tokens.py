import requests
import time

url = 'https://api.divar.ir/v8/web-search/1/residential-sell'

json = {"json_schema": {"category": {"value": "residential-sell"},"cities": ["1"]},
    "last-post-date": 1672815366483199} #Start Url: 1672848945805837
headers ={
    "content-type": "application/json"
}

res = requests.post(url, json=json, headers=headers)
data = res.json()
last_post_date = data['last_post_date']


list_of_tokens = []

count = 0
token_count=0
while (token_count<10000):

    count += 1
    print(count)

    json = {"json_schema": {"category": {"value": "residential-sell"},"cities": ["1"]},
    "last-post-date": last_post_date}

    try:
        res = requests.post(url, json=json, headers=headers)
        if res.ok==True:
            data = res.json()
        else:
            print("wait 30 seconds")
            time.sleep(30)
            res = requests.post(url, json=json, headers=headers)
            data=res.json()
    
        last_post_date = data['last_post_date']

        for widget in data['web_widgets']['post_list']:
            token = widget['data']['token']
            token_count+=1
            list_of_tokens.append(token)

    except:
        txt_file = open('tokens_First_5000.txt','a',encoding='utf8')
        txt_file.write("Next last_post_date: "+str(last_post_date)+"\n")
        txt_file.write(','.join(list_of_tokens))
        txt_file.close()
        raise Exception(last_post_date)  

txt_file = open('tokens_10000.txt','a',encoding='utf8')
txt_file.write("Next last_post_date: "+str(last_post_date)+"\n")
txt_file.write(','.join(list_of_tokens))
txt_file.close()      