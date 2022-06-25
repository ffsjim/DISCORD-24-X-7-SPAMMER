from webserver import keep_alive
import requests

channelID = 956008679231082536
headers = {
    "authorization":
    ""MjY4MzkwNjMyOTkxNDkwMDQ5.GyUnQ3.2V4cfCZBpgiWqrToKzFt5GnQCcpuB0zPiBC2d8""
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
