from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient
import os

SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings, 'SLACK_BOT_USER_TOKEN', None)
Client = SlackClient(SLACK_BOT_USER_TOKEN)

os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

class Events(APIView):
    def post(self, request, *args, **kwargs):

        slack_message = request.data
        
        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # verification challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,
                            status=status.HTTP_200_OK)
       # greet bot
        if 'event' in slack_message:
            event_message = slack_message.get('event')
            
            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':
                return Response(status=status.HTTP_200_OK)
            
            # process user's message
            user = event_message.get('user')
            text = event_message.get('text')
            channel = event_message.get('channel')
            bot_text = 'Hi <@{}> :wave:'.format(user)
            if 'as' in text.lower():
                Client.api_call(method='chat.postMessage',
                                channel=channel,
                                text=bot_text)
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)