#!/usr/bin/env python
#
# Project: Video Streaming with face recognition
# Author: agametov [at] gmail [dot] com>
# Date: 2016/02/11
# Website: http://www.agametov.ru/
# Usage:
# 1. Install Python dependencies: cv2, flask. (wish that pip install works like a charm)
# 2. Run "python main.py".
# 3. Navigate the browser to the local webpage.
from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

def gen(camera):
    process_this_frame = True
    while True:
        if process_this_frame:
            frame = camera.get_frame()
        process_this_frame = not process_this_frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
