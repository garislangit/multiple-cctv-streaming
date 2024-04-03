RTSP based multiple CCTV streaming from various IP cameras powered by Flask and OpenCV.
I needed to display IP camera output to a website .The IP cameras brand are Dahua and Hikvision. The Dahua IP cameras have HTTP/RTSP streaming output and the Hikvision IP cameras only have RTSP based output but since our website is in HTTPS, embedding a HTTP content will trigger a http mixed content warning  and the content can't be displayed as well. Indeed, we can install SSL certificate to the IP camera and the HTTP mixed content will be fixed, unfortunately we dont have access to the dahua IP camera admin panel. Fortunately these IP cameras have RTSP output that can be called. However to display RTSP output to the website is not simple , we need to install additional client plugin in order to work.

Python comes to the rescue through its well known web framework Flask and openCV library. Hence i dediced to create a RTSP Relay / streaming proxy server.

Multiple ip cameras streaming need a lot of resource mainly the webserver . we can't use flask's built in web server. We use uwsgi server with additional tweak such as the workers connection

to embed to the website we can use iframe tag

<iframe src="http://rstp-relay-server/live?source=1"></iframe>
