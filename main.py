
import json
import csv
import requests


# Your access token and Instagram Business Account ID
access_token = "EAAUrCZCcwyJgBAB64jIhtL7rsiBZBf4vZCwBS45oc6XHvOY7WwejnjdzZAM0uxW9OcZCRQRZC8MaS3ZBUZAd01wtWXX5SOuCNPNZByGqt2uJDsVmtHA525TIdTS0ZC0rwn7lm2Irj4BxXAtBWxWSY9E8CwwjdjgUrjmVv72rxNOA8iZCrBSsDKgR0aZBuL6mIRtA5PGFsZC8HPWAGWFx3HgsQdtG501oL1z2ltGEZD"
business_account_id = "17841449740080543"

# The Instagram user you want to retrieve data for
instagram_username = "beerbiceps"

"""
profile_url = f"https://graph.facebook.com/v16.0/{business_account_id}?fields=business_discovery.username(puma)%7Bfollowers_count%2Cmedia_count%2Cmedia%7Bcomments_count%2Clike_count%7D%7D&access_token={access_token}"
posts_response = requests.get(profile_url)
print(posts_response)
data = posts_response.json()
print(data)
"""
#response1 = requests.get("www.google.com")
#print(response1)

endpoint_url = f"https://graph.facebook.com/v16.0/{business_account_id}?fields=id%2Cbusiness_discovery.username({instagram_username})%7Bid%2Cfollowers_count%2Cmedia_count%2Cname%2Cusername%2Cmedia%7Bid%2Ccaption%2Cmedia_type%2Cmedia_url%2Cpermalink%2Ctimestamp%2Cusername%7D%7D&access_token={access_token}"
response = requests.get(endpoint_url)

print(response)
# Convert response to JSON
data = response.json()

print(data)



business_discovery = data['business_discovery']
print("Business Discovery Data:")
print("Name:", business_discovery['name'])
print("Username:", business_discovery['username'])
print("Followers Count:", business_discovery['followers_count'])
print("Media Count:", business_discovery['media_count'])

with open(f'CSVfiles/users.csv','w',newline='') as ucsv:
    uwriter = csv.writer(ucsv)

    uwriter.writerow(["id","Username","Name","followersCNT","MediaCNT"])
    list1 = [f"'{data['business_discovery']['id']}'", f"'{data['business_discovery']['username']}'",
             f"'{data['business_discovery']['name']}'", data['business_discovery']['followers_count'],
             data['business_discovery']['media_count']]

    uwriter.writerow(list1)

with open(f'CSVfiles/posts.csv','w',newline='') as pcsv:
    pwriter = csv.writer(pcsv)

    pwriter.writerow(["id", "Username", "media_type", "permalink", "timestamp"])

    for i in data['business_discovery']['media']['data']:
        list1 = [f"'{data['business_discovery']['id']}'", f"'{data['business_discovery']['username']}'",
                 f"'{i['id']}'", f"'{i['username']}'",
                 f"'{i['media_type']}'", f"'{i['permalink']}'", f"'{i['permalink']}'",
                 f"'{i['timestamp']}'"]
        pwriter.writerow(list1)

"""
with open('media.csv','w',newline='') as fcsv:
    cwriter = csv.writer(fcsv)
    cwriter.writerow(["id","likeCNT","commentCNT"])

    for i in data1['business_discovery']['media']['data']:
        cwriter.writerow([f"'{i['id']}'", i['like_count'], i['comments_count']])
"""

"""
# Print media data
media_data = business_discovery['media']['data']
print("\nMedia Data:")

for media in media_data:
    print("ID:", media['id'])
    print("Username:", media['username'])
    print("Caption:", media['caption'])
    print("Media Type:", media['media_type'])
    print("Media URL:", media['media_url'])
    print("Permalink:", media['permalink'])
    print("Timestamp:", media['timestamp'])


print(1)

import csv

with open("./abc.json") as file:
    data1 = {
        "business_discovery": {
            "name" : "puma1",
            "username" : "puma200",
            "followers_count": 12845726,
            "media_count": 3461,
            "media": {
                "data": [
                    {
                        "comments_count": 118,
                        "like_count": 15141,
                        "id": "17911931744652659"
                    },
                    {
                        "comments_count": 516,
                        "like_count": 15917,
                        "id": "17980175987094126"
                    },
                    {
                        "comments_count": 89,
                        "like_count": 3973,
                        "id": "17959910879416903"
                    }
                ],
                "paging": {
                    "cursors": {
                        "after": "QVFIUjV0dWhhalBqZAkQxSm14TGJ4ZAnVmWm56aDNWRmJJY2FUUTNKMVMzNWlsMGpfWHdZAQVprQy10bGN2ZAFA1LTI2cHV4c2Vjdk03bDZAzb24xSnVrUV8tcFRR"
                    }
                }
            },
            "id": "17841401011180158"
        },
    "id": "17841449740080543"
    }
    print(data1)

with open('media.csv','w',newline='') as fcsv:
    cwriter = csv.writer(fcsv)
    cwriter.writerow(["id","likeCNT","commentCNT"])

    for i in data1['business_discovery']['media']['data']:
        cwriter.writerow([f"'{i['id']}'", i['like_count'], i['comments_count']])

"""
