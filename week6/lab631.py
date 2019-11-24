import requests
from github import Github
#token generated for my github 
g = Github("f829462466b96bcd0796b2f576e5796e58b62b57")

for repo in g.get_user().get_repos():
    print (repo.name)


repo = g.get_repo("healyshane/SH")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + "Kelly \n"
print (newContents)


gitHubResponse=repo.update_file(fileInfo.path,"updated through Github API",newContents,fileInfo.sha)
print (gitHubResponse)
