# multiple-cctv-streaming
RTSP based  multiple CCTV streaming from various IP cameras powered by Flask and OpenCV.
Currently i need to display IP camera output to a website .The IP camera brands are Dahua and Hikvision. The Dahua IP cameras have HTTP streaming output and the Hikvision ip camera only have RTSP based output but since our website is in HTTPS, embedding a HTTP content will trigger a warning http mixed content and the content can't be displayed as well. We can install SSL certificate to the ip camera and the http mixed content will be fixed, unfortunately we dont have access to the dahua IP camera. Fortunately these IP cameras have RTSP output that can be called. However to display RTSP output to the website is not simple , we need to install additional plugins .  

Python comes to the rescue through its well known web framework Flask and openCV library hence i dediced to create a RTSP Relay / streaming proxy server.

Multiple ip cameras streaming need a lot of resource mainly the webserver . we can't use flask built in web server. We use uwsgi server with additional tweak such as the workers connection 

