TOKEN = '913582527:AAHpQtZsNTsb17MjuzopzxF9nwq8IDLaQZ0'
PROXY = {'https':'socks5://modulproxyuser1:95UM47aAjooGpRf@external.fintechcrm.ru:1080'}
USE_PROXY = False
USE_WEB_HOOK = False

PROXY_USER = 'modulproxyuser1'
PROXY_PASS = '95UM47aAjooGpRf'

WEBHOOK_HOST = 'xxxxx.ru'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = './source/cert/webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './source/cert/webhook_pkey.pem'  # Path to the ssl private key

# Quick'n'dirty SSL certificate generation:
#
# openssl genrsa -out webhook_pkey.pem 2048
# openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in WEBHOOK_HOST

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (TOKEN, )
'''
REQUEST_KWARGS={
    'proxy_url': 'https://external.fintechcrm.ru:1080',
    # Optional, if you need authentication:
    'username': 'modulproxyuser1',
    'password': '95UM47aAjooGpRf',
}
'''
REQUEST_KWARGS={
    'proxy_url': 'socks5 OR socks5h://external.fintechcrm.ru:1080',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': 'PROXY_USER',
        'password': 'PROXY_PASS',
    }
}
