from pyboy import PyBoy
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse

socket_token = "xapp-iam-not-telling-you"
bot_token = "xoxb-why-are-you-looking-at-this"

sock = SocketModeClient(app_token=socket_token)
client = WebClient(token=bot_token)

channel_id = "C086M5DM8F7"

pyboy = PyBoy("Pokemon Red.gb")
pyboy.set_emulation_speed(0)
def send_mon(c_id,filename):
    try:
        response = client.files_upload(channels=c_id,file=filename)
        file_url = response["file"]["permalink"]
        client.chat_postMessage(channel=channel_id,text=f"hello {file_url}")
        print('image sent!')
    except SlackApiError as oopsies:
        print(f"oopsie daisy {oopsies.response['error']}")
@sock.event
def handle_message(event,say):
    text = 'ghghgh'
    if event['type'] == 'message' and 'text' in event:
        text = event['text']
        print(text)
    if text in ["w",'a','s','d','a','b','x','y']:
        if text == "w":
            pyboy.button('up')
        if text == "a":
            pyboy.button("left")
        if text == "s":
            pyboy.button('down')
        if text == 'd':
            pyboy.button('right')
        if text == 'a':
            pyboy.button('a')
        if text == 'b':
            pyboy.button('b')
        if text == 'x':
            pyboy.button('start')
        if text == 'y':
            pyboy.button('select')
        for i in range(20):
            pyboy.tick()
        image = pyboy.screen.image
        image.save("screen.png")
        send_mon(channel_id,"screen.png")
        print(text)

sock.socket_mode_request_listeners.append(handle_message)
sock.connect()
from threading import Event
Event().wait()