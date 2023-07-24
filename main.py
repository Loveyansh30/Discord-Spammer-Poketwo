from webserver import keep_alive
import requests

channelID = 1132936016395784202
headers = {
    "authorization":
    "OTU1NzcxNDY0NTYzNDUzOTgy.Gy2lIT.xYLSv0X3iQkNnyGqwOlUiE7iRhpCNPz0NLxIAo"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{1132936016395784202}/messages",
            headers=headers,
            json={"content": line})
