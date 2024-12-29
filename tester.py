bot_token = "xoxb-not-telling-you"
app_level_token = "xapp-why-are-you-looking-at-this"

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from pyboy import PyBoy
from io import BytesIO
from PIL import Image as im

pyboy = PyBoy("Pokemon Red.gb",window="null")
with open("hackclub.state","rb") as s:  
    try:
        pyboy.load_state(s)
    except:
        pass
pyboy.set_emulation_speed(1)
inputcounter = 0
channel_id = "getalife"
stats = [0 for i in range(9)]
with open("stats.txt","r") as st:
    if st.read() != "":
        for i in range(len(st.read().split('\n'))):
            stats[i] = st.read().split('\n')[i].split(" ")[-1]
def handle_input(text):
    global inputcounter
    global stats
    if text=="i":
        pyboy.button_press('up')
        pyboy.tick(30)
        pyboy.button_release('up')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[0] += 1
        return img_bytes
    if text == "k":
        pyboy.button_press('down')
        pyboy.tick(30)
        pyboy.button_release('down')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[1] += 1
        return img_bytes
    if text == 'j':
        pyboy.button_press('left')
        pyboy.tick(30)
        pyboy.button_release('left')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[2]+=1
        return img_bytes
    if text == 'l':
        pyboy.button_press('right')
        pyboy.tick(30)
        pyboy.button_release('right')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[3]+=1
        return img_bytes
    if text == "a":
        pyboy.button_press('a')
        pyboy.tick(30)
        pyboy.button_release('a')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[4]+=1
        return img_bytes

    if text == "b":
        pyboy.button_press('b')
        pyboy.tick(30)
        pyboy.button_release('b')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[5]+=1
        return img_bytes

    if text == "x":
        pyboy.button_press('select')
        pyboy.tick(30)
        pyboy.button_release('select')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[6]+=1
        return img_bytes

    if text == "y":
        pyboy.button_press('start')
        pyboy.tick(30)
        pyboy.button_release('start')
        image = pyboy.screen.ndarray
        image = im.fromarray(image)
        image = image.resize((image.width*2,image.height*2))
        img_bytes = BytesIO()
        image.save(img_bytes,format="PNG")
        img_bytes.seek(0)
        stats[7]+=1
        return img_bytes
    if text.split(" ")[0] == "LOOP":
        imgs= []
        key = None
        stats[8]+=1
        if len(text.split(" ")) == 3:
            key = text[-1]
        for i in range(int(text.split(" ")[1])):
            if key is not None:
                img_bytes  = handle_input(key.lower())
            else:
                pyboy.tick(120)
                image = pyboy.screen.ndarray
                image = im.fromarray(image)
                image = image.resize((image.width*2,image.height*2))
                img_bytes = BytesIO()
                image.save(img_bytes,format="PNG")
                img_bytes.seek(0)
            imgs.append(img_bytes)
        return imgs
    inputcounter+=1
    if inputcounter % 20 == 0:
        with open("hackclub.state",'wb') as hc:
            pyboy.save_state(hc)
        s = open("stats.txt","w")
        s.write(f"I: {stats[0]}\n")
        s.write(f"K: {stats[1]}\n")
        s.write(f"J: {stats[2]}\n")
        s.write(f"L: {stats[3]}\n")
        s.write(f"A: {stats[4]}\n")
        s.write(f"B: {stats[5]}\n")
        s.write(f"X: {stats[6]}\n")
        s.write(f"Y: {stats[7]}\n")
        s.write(f"LOOP: {stats[8]}\n")
        s.close()
        


app = App(token=bot_token)
@app.message("RESET")
def m_reset(message,say):
    global pyboy
    say("RESETTING")
    with open("hackclub.state",'wb') as hc:
        pyboy.save_state(hc)
    s = open("stats.txt","w")
    s.write(f"I: {stats[0]}\n")
    s.write(f"K: {stats[1]}\n")
    s.write(f"J: {stats[2]}\n")
    s.write(f"L: {stats[3]}\n")
    s.write(f"A: {stats[4]}\n")
    s.write(f"B: {stats[5]}\n")
    s.write(f"X: {stats[6]}\n")
    s.write(f"Y: {stats[7]}\n")
    s.write(f"LOOP: {stats[8]}\n")
    s.close()
    pyboy = 0
    pyboy = PyBoy("Pokemon Red.gb",window="null")
    with open("hackclub.state","rb") as hc:
        pyboy.load_state(hc)

@app.message("LOOP")
def message_hello(message, say):
    imgs = handle_input(message["text"])
    for img_bytes in imgs:
        upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
        id = upload_response['file']['id']
        response = app.client.chat_postMessage(channel=channel_id,text="",attachments=[{
                        "fallback": "Image could not be displayed",
                        "image_url": upload_response['file']['url_private'],
                        }])
    say("done ticking")

@app.message("I")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("i")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="I Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])
    
@app.message("J")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("j")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="J Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])
    
@app.message("K")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("k")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="K Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])

@app.message("L")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("l")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="L Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])
    
@app.message("X")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("x")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="Select Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])
    
@app.message("Y")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("y")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="Start Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])
    
@app.message("A")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("a")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="A Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])
    
@app.message("B")
def message_hello(message, say):
    say("button registered")
    img_bytes = handle_input("b")
    upload_response = app.client.files_upload_v2(channel=channel_id,file=img_bytes,filename="pokemon.png")
    id = upload_response['file']['id']
    response = app.client.chat_postMessage(channel=channel_id,text="B Pressed",attachments=[{
                    "fallback": "Image could not be displayed",
                    "image_url": upload_response['file']['url_private'],
                    }])

if __name__ == "__main__":
    SocketModeHandler(app, app_level_token).start()

