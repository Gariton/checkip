#!/usr/bin/env python3
import requests
import urllib.request
import json
import socket

url = 'http://httpbin.org/ip'
filepath = '/home/pi/Desktop/git/checkGlobalIp/ip.txt'

def difference():
  try:
    with urllib.request.urlopen(url) as response:
      body = json.loads(response.read())['origin']
      #print('globalIP:' + body)

      f = open(filepath)
      fbody = f.read().replace('\n','')
      #print('fileIP:' + fbody)
      f.close()

      if (body == fbody):
        return False
      else:
        print("unmatch.")
        f = open(filepath, mode='w')
        f.write(body)
        f.close()
        print("updated")

        return body

  except urllib.error.URLError as e:
    print(e.reason)
