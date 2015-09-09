"""server.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import logging
import warnings
import ftplib
import urlparse
import getpass
import binascii
import urllib2 as urllib

import logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename='ncbs.log',
    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
_logger = logging.getLogger('ncbs.sync')
_logger.addHandler(console)


def sync_server(args):
    """Sync with given server """
    url = args.sync
    if "http://" in url:
        pass
    elif "ftp://" in url:
        sync_ftp(urlparse.urlparse(url))
    else:
        sync_ftp(urlparse.urlparse(url))

def download_file(con, file):
    """Download single file using ftp"""

    #for c in [ ' ', '&', '%s', '$' ]:
    #    file = file.replace(c, '\%s' % c)

    outfile = file
    _logger.info("Downloading %s as %s" % (file, outfile))
    try:
        f = open(outfile, 'wb')
        con.retrbinary('RETR %s' % file, f.write)
        f.close()
    except Exception as e:
        print("Failed to download")
        print("|- Error was: %s" % e)

def sync_ftp(parsedurl):
    url = parsedurl.path
    if parsedurl.scheme:
        url = parsedurl.netloc
    else:
        url = parsedurl.path

    ftp = ftplib.FTP(url)
    username, password = 'anonymous', 'anonymous'
    username, password = 'student', 'student'
    #username = raw_input("Username [anonymous]:")
    #if not username:
    #    username = 'anonymous'
    #if username != "anonymous":
    #    password = getpass.getpass()

    try:
        ftp.login(username, password)
    except Exception as e:
        print("Failed to login with given username/password")
        quit()

    ftp.retrlines('NLST', lambda x: download_file(ftp, x))
    ftp.quit()



