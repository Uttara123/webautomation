# webautomation
sample code using python and selenium to create a web driver, start off a chrome or firefox browser and take an action 
pull this repo, it will download the browsers dir that contain chrome and firefox driver
pre-requisites 
  install python
  install selenium  using command pip install selenium or pip install -U selenium (if you already have seleinium)
  this code works with selenium 3.4.3 and python 2.7
  to check your selenium version start a python shel
      ctl-utamhank-m:webautomation utamhank$ python
      Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
      [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import selenium
       >>> help(selenium)
       response will contain
       DATA
        __version__ = '3.4.3'

      VERSION
          3.4.3
so lets say you pulled this into a dir /home/user/webautomation
now set PATH to contain the drivers : 
export PATH=$PATH://home/user/webautomation/browsers
cd  /home/user/webautomation/browsers
./chromedriver

from another terminal
cd /home/user/webautomation
python weblib.py

this will invoke :
  firefox and go to https://www.google.com/xhtml
  input ChromeDriver in search field of goodle
  then do the same for chrome 
  then do same for chrome but in a remote way
  
