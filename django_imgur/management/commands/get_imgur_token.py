from django.core.management.base import NoArgsCommand
from dropbox import rest, session
from django_imgur.settings import CONSUMER_ID, CONSUMER_SECRET
from imgurpython import ImgurClient

class Command(NoArgsCommand):
    """ Before using this command, the application need to be registered
        by an imgur user. See https://api.imgur.com/oauth2 """

    def handle_noargs(self, *args, **options):
        client = ImgurClient(CONSUMER_ID, CONSUMER_SECRET)

        url = client.get_auth_url('pin')
        print "Url:", url
        print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
        pin = raw_input().strip()

        # This will fail if the user didn't visit the above URL and hit 'Allow'
        credentials = client.authorize(pin, 'pin')

        print "IMGUR_ACCESS_TOKEN = '%s'" % credentials['access_token']
        print "IMGUR_ACCESS_TOKEN_REFRESH = '%s'" % credentials['refresh_token']