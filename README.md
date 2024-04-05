### Multiple CCTV Streaming

Relay RSTP  output from IP Camera (Dahua and Hikvision) and displayed to the website

### Instruction
1. Install the requirement, first :

   `pip -r requirements.txt `
   
2. Run the main python script by executing :

   `python3 ipcamera.py or python ipcamera.py`

   Debian Linux uses python3 instead python


4. Open the streaming web address i.e
   
   http://domain.ip/live2?source=123
   http://domain.ip/live?source=8
         

### Embed to a website 

`<iframe src="http://rstp-relay-server/live?source=1"></iframe>`

### Suggestion

use the uwsgi web server if you have high traffic/many ip camera, very recommended than using flask's built in web server.

