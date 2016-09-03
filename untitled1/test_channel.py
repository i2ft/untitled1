from django.http import HttpResponse
from channels.handler import AsgiHandler
from post.models import Post
from django.core import serializers

def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)




def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    text = message.content['text']

    a = text.split('/')
    s = a[2]+"-"+a[0]+"-" + a[1]
    post_list = Post.objects.all()
    print(s==str(post_list[0].start_date))
    final = post_list.filter(start_date=s)
    qs_json = serializers.serialize('json', final)
    print(type(final))
    print(type(qs_json))
    message.reply_channel.send({
        "text": qs_json,
    })