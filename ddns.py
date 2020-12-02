#!/usr/bin/env python3

import ssl
import json
import socket
import urllib.request
import datetime

#onamaeID/Pass
userid = "7531691"
password = "Jp(0117)onamae"

#tarfet dns info
hostname=""
domname="gariton.site"

def getip():
  url = "http://inet-ip.info/ip"
  req = urllib.request.Request(url)
  res = urllib.request.urlopen(req)
  ip = res.read().decode()
  return ip

def getdns(domain):
  url = "https://dns.google.com/resolve?name={domain}&type=A".format(domain=domain)
  req = urllib.request.Request(url)
  res = urllib.request.urlopen(req)
  data = json.loads(res.read().decode())
  return data["Answer"][0]["data"]

def updateip(ip):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(10)
  s = ssl.wrap_socket(sock)
  s.connect(("ddnsclient.onamae.com", 65010))
  #print(s.recv(1024).decode())

  data = """LOGIN
USERID:{uid}
PASSWORD:{pwd}
.
MODIP
HOSTNAME:{h}
DOMNAME:{domain}
IPV4:{ip}
.
LOGOUT
.""".format(uid=userid,pwd=password,h=hostname,domain=domname,ip=ip)

  print("DATA STRINGS:\n", data)

  for line in data.split("\n"):
      s.send(line.encode() + b"\r\n")
      if line == ".":
        print(s.recv(1024).decode())

  s.close()

def foward_lookup():
  try:
    return socket.gethostbyname(domname)
  except:
    return False

def checkDns():
  dnsIp = foward_lookup()

  filepath = '/home/pi/Desktop/git/checkGlobalIp/dns.txt'
  f = open(filepath)
  fbody = f.read().replace('\n','')
  f.close()

  if dnsIp == fbody:
    return False
  else:
    #新しいものに書き換え
    f = open(filepath, mode='w')
    f.write(dnsIp)
    f.close()
    return dnsIp

if __name__ == "__main__":
  print(checkDns())
