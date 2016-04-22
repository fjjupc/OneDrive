#!/usr/bin/env python
# Author:   Carl Fan
# Mail:     fjjupc@gmail.com
# Describe: Get authorized by OneDrive

from get_client_info import client_id, client_secret

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

# See Should be set in your application settings in https://account.live.com/developers/applications/index
redirect_uri = "http://localhost:8080/"

client = onedrivesdk.get_default_client(
	client_id,
    ['wl.signin', #Allows your application to take advantage of single sign-on capabilities.
     'wl.offline_access', #Allows your application to receive a refresh token so it can work offline even when the user isn't active.
     'onedrive.readwrite' # Grants read and write permission to all of a user's OneDrive files, including files shared with the user. To create sharing links, this scope is required.
    ])

auth_url = client.auth_provider.get_auth_url(redirect_uri)

#this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)