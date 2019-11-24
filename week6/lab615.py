import requests, json
#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()

#print(data)
#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)



#creating excel file and writing into it
from xlwt import *
w = Workbook()
ws = w.add_sheet('githubusers')
row = 0
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"type")
row +=1

for follower in data: # different from car example becuse json name not defined for github followers
    ws.write(row,0,follower["login"])
    ws.write(row,1,follower["id"])
    ws.write(row,2,follower["node_id"])
    ws.write(row,3,follower["type"])
    row +=1
w.save('githubusers.xls')