import mechanize, pprint
from mechanize._html import MechanizeBs
import pprint
import sys,getopt
import time, datetime
import pdb
import string
import urllib, os, pprint
import urllib2
from bs4 import BeautifulSoup
import html5lib
import codecs

# url = 'https://www.netflix.com/browse'
url = 'https://www.netflix.com/browse/genre/83'

br = mechanize.Browser()
# br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)  # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.set_handle_redirect(True)
br.set_handle_referer(True)


br.open(url)
br.select_form(nr=0)
br.form['email'] = 'dundunmao@gmail.com'
br.select_form(nr=0)
br.form['password'] = '200131083'
response = br.submit()
response_html = response.get_data()
soup = BeautifulSoup(response_html,'html5lib')
f = open('nef83.txt','wb')
f.write(soup.prettify("utf-8"))
f.close()
print soup


start_0 = string.find(response_html, 'id=\"resultStats\">')

# _BL_WARNING_, the following agent is really too old, we shall replace with a newer agent
# br.addheaders =[('User-agent', 'Firefox')]
br.addheaders = [('user-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]



response = urllib2.urlopen(url, timeout=1)
html = response.read()
soup = BeautifulSoup(html,'html5lib')
print soup

req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()


