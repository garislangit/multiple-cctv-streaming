from flask import Flask, Response, jsonify, request, abort
import cv2

class VideoCamera(object):
    def __init__(self, address):
        self.video = cv2.VideoCapture(address)

    def __del__(self):
        self.video.release()

    def check_camera(self):
        ret, frame = self.video.read()
        if not ret:
           return False
        else:
           return True

    def get_frame(self):
        if self.check_camera():
           _, frame = self.video.read()
           _, jpeg = cv2.imencode('.jpg', frame)
           return jpeg.tobytes()

app = Flask(__name__)

def gen_frame(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame)

@app.route("/")
def index():
    return "IP Camera proxy"

@app.route('/live')
def live():
    if 'source' in request.args:
       source = request.args['source']
       if source == '':
          return "Invalid source parameter"
       else:
          CAMERA_URL = 'rtsp://user:password@ip_address:' + source + '/cam/realmonitor?channel=1&subtype=1'
          camera = VideoCamera(f'{CAMERA_URL}')
          if camera.check_camera():
             return Response(gen_frame(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
          else:
              return "Camera error/invalid source"
    else:
       return "Invalid parameter"
@app.route('/live2')
def live2():
    if 'source' in request.args:
       source = request.args['source']
       if source == '':
          return "Invalid source parameter"
       else:
          CAMERA_URL = 'rtsp://user:password@ip_address:port/Streaming/Channels/' + source
          camera = VideoCamera(f'{CAMERA_URL}')
          if camera.check_camera():
             return Response(gen_frame(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
          else:
              return "Camera error/invalid source"
    else:
       return "Invalid parameter"

@app.route('/status1')
def checkstatus1():
    if 'source' in request.args:
       source = request.args['source']
       if source == '':
          return "Invalid source parameter"
       else:
           CAMERA_URL = 'rtsp://user:password@ip_address:' + source + '/cam/realmonitor?channel=1&subtype=1'
          camera = VideoCamera(f'{CAMERA_URL}')
          if camera.check_camera():
             result = {
                    "group" : 1,
                    "source" : source,
                    "device" : "Dahua",
                    "status" : "up"
             }
             return jsonify(result)
          else:
             result = {
                    "group" : 1,
                    "source" : source,
                    "device" : "Dahua",
                    "status" : "down" 
             }
             return jsonify(result)
    else:
       return "Invalid parameter"

@app.route('/status2')
def checkstatus2():
    if 'source' in request.args:
       source = request.args['source']
       if source == '':
          return "Invalid source parameter"
       else:
          CAMERA_URL = 'rtsp://user:password@ip_address:port/Streaming/Channels/' + source
          camera = VideoCamera(f'{CAMERA_URL}')
          if camera.check_camera():
             result = {
                    "group" : 2,
                    "source" : source,
                    "device" : "Hikvision",
                    "status" : "up"
             }
             return jsonify(result) 
          else:
             result = {
                    "group" : 2,
                    "source" : source,
                    "device" : "Hikvision",
                    "status" : "down"
             }
             return jsonify(result)
    else:
       return "Invalid parameter"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
