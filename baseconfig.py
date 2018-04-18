"""
Base config for any environment.
In order to add/overwrite some keys, create config.py file with the following contents:

from baseconfig import Config

class ProductionConfig(Config):
    SOME_KEY = 'value'
"""

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024 # 100 MB limit for uploaded files

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Q1U1[?-blBn:B-b+fP^x+`I|x%l!w7dO&+M0l4x;;A[N4U@gJ|?&[W*kYr%MGtyw'

    DEVELOPMENT = False
    LOCAL_DEVELOPMENT = False
    TEMPLATES_AUTO_RELOAD = False
    DEVELOPER_API_KEYS = (
        # Below listed developer API consumers
        # User should send X-Dev-API-Key header with each request in order to authorize 
        # { 'username': 'developer', 'key': '9bf74896-e760-49a3-a7a1-bcaeab11066e' },
    )

    # Should be set to the directory containing templates from the frontend repo
    CUSTOM_TEMPLATE_FOLDER = None

    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/simpleflask'
    SQLALCHEMY_POOL_TIMEOUT = 120
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    STATISTIC_DATABASE_URI = 'mysql://root@localhost/simpleflask_statistic?max_connections=20&stale_timeout=120'

    ELASTICSEARCH_URI = 'http://localhost:9200/'
    ELASTICSEARCH_INDEX = 'simpleflask_search'

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379

    MAIL_SETTINGS = {
        'default': {
            'host': 'email-smtp.us-east-1.amazonaws.com',
            'port': 465,
            'ssl': True,
            'user': 'nonexistent',
            'password': 'blahblahblah',
            'sender': ('yourdomain.net', 'noreply@yourdomain.net')
        },
        'secondary': {
            'host': 'email-smtp.us-east-1.amazonaws.com',
            'port': 465,
            'ssl': True,
            'user': 'nonexistent',
            'password': 'blahblahblah',
            'sender': ('yourdomain.net', 'noreply@yourdomain.net')
        }
    }

    CUSTOM_TEMPLATE_FOLDER = 'templates'  # Set Jinja templates folder
    FRONTEND_BUILD_LOCATION = 'app/static/assets'  # Set frontend build folder location

    STATIC_FOLDER = os.path.join(BASE_DIR, 'app', 'static')
    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'uploads')
    PROFILE_UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'profile_uploads')
    ORDERS_UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'orders_uploads')
    ALLOWED_PHOTO_EXTENSIONS = ('png', 'jpg', 'jpeg', 'gif')
    ALLOWED_DOCUMENT_EXTENSIONS = ('png', 'jpg', 'jpeg', 'pdf')
    ALLOWED_ATTACHMENT_EXTENSIONS = ('zip', 'rar', 'tgz', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif')
    MAX_ATTACHMENT_SIZE = 100 * 1024 * 1024  # 100 MB
    THUMBNAIL_SIZE = (160, 160)

    ALLOWED_PHOTO_FORMATS = ('JPEG', 'JPEG 2000', 'PNG') # Format from PIL
    PHOTO_SIZE = (670, 320)

    PASSWORD_RSA_PUBLIC_KEY = None  # Specify RSA public key here. Use python multiline string or put \n symbols instead of newlines

    EXCHANGE_RATE_EXPIRATION = 7200  # 2 hours

    MIN_BALANCE = 0
    WITHDRAWAL_THRESHOLD_BTC = 0.01  # 0.01 BTC minimal withdrawal
    WITHDRAWAL_RANGE_WU = (10000.0, 100000.0)  # min. 100 USD, max 1000 USD
    WITHDRAWAL_RANGE_PAYPAL = (10000.0, 100000.0)  # min. 100 USD, max 1000 USD
    WITHDRAWAL_RANGE_SKRILL = (10000.0, 100000.0)  # min. 100 USD, max 1000 USD
    WITHDRAWAL_RANGE_PAYONEER = (10000.0, 100000.0)  # min. 100 USD, max 1000 USD
    WITHDRAWAL_RANGE_PAYZA = (10000.0, 100000.0)  # min. 100 USD, max 1000 USD
    TRANSFER_THRESHOLD = 1000  # min. 10 USD

    ORDER_PENDING_CLEARANCE_DAYS = 14

    ORDER_FEE = 0.05  # 20 percents
    WITHDRAWAL_FEE = 0.02  # 2 percents
    WITHDRAWAL_FEE_WU = 0.05  # 5 percents
    DEPOSIT_FEE = 0.05  # 5 percents
    TRANSFER_FEE = 0.05  # 5 percents
    DISPUTE_FEE = 0.1  # 10 percents

    AFFILIATE_PAYOUT_IMPRESSION = 1  # 0.01 USD per unique impression, 0 to disable
    AFFILIATE_PAYOUT_REGISTRATION = 10  # 0.10 USD per registration, 0 to disable
    AFFILIATE_PAYOUT_BECOME_SELLER = 10  # 0.10 USD per become a seller, 0 to disable

    AFFILIATE_COMISSIONS_RELEASE_THRESHOLD = 10000  # Release all transactions after hitting 100 USD threshold

    SELLER_FEE_USD = 0  # Set to 0 or None to disable one-time seller fee
    PREMIUM_FEE_USD = 10000

    ORDER_ACCEPT_DEADLINE = 14400  # 4 hours
    ORDER_SENT_DEADLINE = 86400  # 1 day

    NEW_ORDER_MODERATION_POLICY = {
        'all_customers': False,  # Moderate orders from any customers
        'new_customers': True,  # Moderate orders from new customers
        'threshold': 10000,  # Amount threshold (cents)
        'new_customers_min_orders_count': 1  # Min. successful orders to consider customer as not new
    }

    LEVEL_PUBLISH_LIMIT = {
        'new_seller': 10,
        'level_1': 20,
        'level_2': 50,
        'top_rated': 100
    }

    SERVICE_PRICE_RANGE = (500, 500000)  # min. 5 USD, max 5000 USD

    NEW_SERVICE_DAYS = 3  # Service is considered new if it has been published within last X days

    # Override the following keys within environment config:

    GALLERY_CATEGORY_IDS = {
        'photo': 1,
        'video': 8
    }

    # Stripe settings
    # WARNING: do not forget to setup WEBHOOKS in stripe account
    # Production URL: https://yourdomain.net/webhooks/stripe
    # Events to subscribe: charge.pending, charge.succeeded, charge.failed, source.chargeable, source.failed, source.canceled

    STRIPE_SECRET_KEY = ''
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_WEBHOOK_SECRET_KEY = ''

    # OAuth settings

    OAUTH_CREDENTIALS = {
        'facebook': {
            'id': '<YOUR APP ID>',
            'secret': '<YOUR APP SECRET_KEY>'
        },
        'twitter': {
            'consumer_key': '<YOUR CONSUMER_KEY>',
            'consumer_secret': '<YOUR CONSUMER_SECRET>',
            'access_token': '<YOUR ACCESS_TOKEN>',
            'access_secret': '<YOUR ACCESS_SECRET>'
        },
        'google': {
            'id': '',
            'secret': ''
        },
        'yahoo': {
            'id': '',
            'secret': ''
        },
        'outlook': {
            'id': '',
            'secret': ''
        },
        'aol': {
            'id': '',
            'secret': ''
        },
        'linkedin': {
            'id': '',
            'secret': ''
        }
    }

    SLACK_WEBHOOK_URL = "<SLACK HOOKS URL>"

    AWS_ACCESS_KEY = ''
    AWS_SECRET_KEY = ''
    AWS_SESSION_TOKEN = ''

    AWS_IMAGES_CONFIGURATION = {
        'bucket': 'selfmarkett',
        'prefix': 'images'
    }

    AWS_PROFILE_IMAGES_CONFIGURATION = {
        'bucket': 'selfmarkett',
        'prefix': 'profile_images'
    }

    AWS_ATTACHMENTS_CONFIGURATION = {
        'bucket': 'selfmarkett',
        'prefix': 'attachments'
    }

    CLOUDINARY_CLOUD_NAME = ''
    CLOUDINARY_API_KEY = ''
    CLOUDINARY_API_SECRET = ''

    USE_JOBDONE_IMAGE_SERVICE = True

    ALERT_EMAIL = '<YOUR ALERT EMAIL>'  # Used for various alerts (incl. contact us form)
    REPLY_TO_EMAIL = '<YOUR REPLY_TO_EMAIL>'  # Used for marketing emails so users can reply

    TWILIO_SID = '<TWILIO_SID>'
    TWILIO_TOKEN = '<TWILIO_TOKEN>'
    TWILIO_PHONE_NUMBER = '<TWILIO_PHONE_NUMBER>'

    SUPPORT_URL = '<YOUR SUPPORT_URL>'

    USER_DELETE_REASONS = (
        dict(reason='other', title='Other'),
    )

    VIDEO_CDN_PREFIX = '<CDN PREFIX>'

    SERVICE_FEATURES = {
        # 'top_search' : {
        #     duration: 86400,
        #     price: 4500
        # },
        'highlight_7': {
            'type': 'highlight',
            'duration': 86400 * 7,
            'price': 500
        },
        'highlight_30': {
            'type': 'highlight',
            'duration': 86400 * 30,
            'price': 1500
        },
        'newsletter' : {
            'type': 'newsletter',
            'duration': 86400 * 1,
            'price': 990
        },
        'social' : {
            'type': 'social',
            'duration': 86400 * 3,
            'price': 990
        }
    }


# Example for production config
class ProductionConfig(Config):
    SERVER_NAME = 'yourdomain.net'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_DOMAIN = 'yourdomain.net'

    STATIC_SERVER_NAME = 'static.yourdomain.net'

    MAIL_SETTINGS = {
        'default': {
            'host': 'email-smtp.us-east-1.amazonaws.com',
            'port': 465,
            'ssl': True,
            'user': 'AKIAIJ7QVLQNRYPLAHOQ',
            'password': 'email-smtp.us-east-1.amazonaws.com',
            'sender': ('yourdomain.net', 'noreply@yourdomain.net')
        },
        'secondary': {
            'host': 'email-smtp.us-east-1.amazonaws.com',
            'port': 465,
            'ssl': True,
            'user': 'AKIAIJ7QVLQNRYPLAHOQ',
            'password': 'email-smtp.us-east-1.amazonaws.com',
            'sender': ('yourdomain.net', 'noreply@yourdomain.net')
        }
    }

    MESSAGING_SERVER_URI = 'https://messaging.yourdomain.net'

    # In case SENTRY_DSN is not set, sentry will be disabled at startup
    # SENTRY_DSN_CLIENT is the same as the first, but without secret part (used on the client side)
    SENTRY_DSN = None
    SENTRY_DSN_CLIENT = None


# Example for development config
class DevelopmentConfig(Config):
    SERVER_NAME = 'localhost:5000'

    DEVELOPMENT = False
    LOCAL_DEVELOPMENT = True
    TEMPLATES_AUTO_RELOAD = True

    DEBUG = True

    MESSAGING_SERVER_URI = 'http://localhost:5001'


# Example for testing config
class TestingConfig(Config):
    # SERVER_NAME = 'localhost:5000'

    TESTING = True
    DEVELOPMENT = False
    LOCAL_DEVELOPMENT = True
    TEMPLATES_AUTO_RELOAD = True

    DEBUG = True

    MESSAGING_SERVER_URI = 'http://localhost:5001'

    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/simpleflask_testing'
    SQLALCHEMY_POOL_TIMEOUT = 120
