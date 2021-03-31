# whatsapp-send-message-app

### App to send a static message for any contat saved in your smarthphone.


Maked following this [tutorial](https://devaprender.com/como-criar-um-bot-no-whatsapp)

### How to Use
---
- Open a terminal, and run the comands below to install dependencies:

```
pip install selenium
```

```
pip install webdriver_manager
```

- Now, run the comand to start the app: 
```
py app.py 'yourMessage' hasEmoticon
```
```yourMessage:``` The message that you want to send. It need to be between '' to represent a string
<br>
<br>
```hasEmoticon:``` If message has a emoticon code, this value need to be True

The command will open a Chrome page, and request your authenticatin by QrCode.
<br>
Make the atutentication and wait for the ```show``` !!! 

