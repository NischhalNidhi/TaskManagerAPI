import requests
endpoint = "https://icanhazdadjoke.com/"

header = {"Accept":"text/plain"}
print(requests.get(endpoint,headers=header).text)

