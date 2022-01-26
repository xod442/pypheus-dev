#!/usr/bin/env python3
# coding=utf-8
# author: @netwookie
# -*- coding: utf-8 -*-
"""
Various monitoring API calls
"""
import urllib3
urllib3.disable_warnings()
from auth import Auth
import json
import requests

class Monitoring(Auth):

    def __init__(
            self, host,
            username, password
            ):

        Auth.__init__(self, host, username, password)
        self.headers = {"Authorization": "BEARER " + self.access_token,'Accept': 'application/json'}
        self.endpoint ='https://' + host +  '/api'


    def get_all_checks(self, id=None):

    	if id:
    		id = str(id)
    		apps_url = self.endpoint + '/monitoring/checks' + '/id'

    	else:

    		apps_url = self.endpoint + '/monitoring/checks'

    	response = requests.get(apps_url, headers=self.headers,verify=False)

    	return response.json()

    def get_all_incidents(self, id=None):

    	if id:
    		id = str(id)
    		apps_url = self.endpoint + '/monitoring/incidents' + '/id'

    	else:

    		apps_url = self.endpoint + '/monitoring/incidents'

    	response = requests.get(apps_url, headers=self.headers,verify=False)

    	return response.json()

    def get_all_alerts(self, id=None):

        if id:
            id = str(id)
            apps_url = self.endpoint + '/monitoring/alerts' + '/id'

        else:

            apps_url = self.endpoint + '/monitoring/alerts'

        response = requests.get(apps_url, headers=self.headers,verify=False)

        return response.json()

    def get_all_contacts(self, id=None):

        if id:
            id = str(id)
            apps_url = self.endpoint + '/monitoring/contacts' + '/id'

        else:

            apps_url = self.endpoint + '/monitoring/contacts'

        response = requests.get(apps_url, headers=self.headers,verify=False)

        return response.json()
