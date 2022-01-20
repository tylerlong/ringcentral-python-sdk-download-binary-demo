from ringcentral import SDK
import os

sdk = SDK(os.environ['RINGCENTRAL_CLIENT_ID'], os.environ['RINGCENTRAL_CLIENT_SECRET'], os.environ['RINGCENTRAL_SERVER_URL'])
platform = sdk.platform()
platform.login(os.environ['RINGCENTRAL_USERNAME'], os.environ['RINGCENTRAL_EXTENSION'], os.environ['RINGCENTRAL_PASSWORD'])


r = platform.get('/restapi/v1.0/account/~/extension/~/profile-image')
f = open('temp.png', 'wb')
f.write(r.response().content)
f.close()
