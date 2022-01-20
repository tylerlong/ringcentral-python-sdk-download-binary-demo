from ringcentral import SDK
import os

sdk = SDK(os.environ['RINGCENTRAL_CLIENT_ID'], os.environ['RINGCENTRAL_CLIENT_SECRET'], os.environ['RINGCENTRAL_SERVER_URL'])
platform = sdk.platform()
platform.login(os.environ['RINGCENTRAL_USERNAME'], os.environ['RINGCENTRAL_EXTENSION'], os.environ['RINGCENTRAL_PASSWORD'])

res = platform.get('/restapi/v1.0/account/~/extension/~')
print(res.json().extensionNumber)
