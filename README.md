# django-with-metrics
Middleware for sending request\response metrics to Graphite.

This is example how to send application metrics i.e. requests\response types to Graphite.
You can just run it by docker-compose up and open:
* http://localhost:8000/app/200
* http://localhost:8000/app/500
* http://localhost:8000/app/random

Info about request and response will be send in Graphite and you can check it by:
* Graphana interface http://localhost:80 (admin/admin)
* Graphite-web http://localhost:81

I recommend to use UDP protocol for sending metrics, cz TCP adds some freezes in middleware. Just modify code in middleware (you'll see it), but keep in mind that it needs some tweaks in carbon.conf, like ENABLE_UDP_LISTENER = True. Sending metrics by UDP is not presented in this example.
