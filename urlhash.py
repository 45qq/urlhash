import codecs
import mmh3
import requests
import hashlib
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        response = requests.get(sys.argv[1])
        favicon = codecs.encode(response.content, 'base64')
        md5hash = hashlib.md5(response.content)

        hashcode = mmh3.hash(favicon.decode('utf-8'))
        md5 = md5hash.hexdigest()
        sha1 = hashlib.sha1(response.content)
        sha256 = hashlib.sha256(response.content)

        print("hash:\t%d" % hashcode)
        print("md5:\t%s" % md5.upper())
        print("sha1:\t%s" % sha1.hexdigest().upper())
        print("sha256:\t%s" % sha256.hexdigest().upper())
    else:
        print("usage: urlhash.py <url>\n")
