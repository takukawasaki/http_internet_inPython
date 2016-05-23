#!/usr/local/bin/python


import urllib
import sys
URL = 'https://www.github.com'
PROXY_ADDRESS = "165.24.10.8:8080" # By Googling free proxy server


if __name__ == '__main__':
  #a1 = sys.argv[1]
  resp = urllib.urlopen(URL, proxies = {"http" : PROXY_ADDRESS})
  print("Proxy server returns response headers: {!s} ".format(resp.headers))

