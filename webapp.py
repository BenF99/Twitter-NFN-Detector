from ._anvil_designer import MainTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import re

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text = None
    self.fake_ = None
    self.real_ = None
    self.finurl_ = None
    self.currtext = None
    self.submit.visible = False
    self.wait_msg = "Retrieving information from server, Please wait..."
    
  def load_tweet_click(self, **event_args):
    ht_valid = True
    if self.hashtag.text:
      if not re.match("^#[\w-]+(?:\s*#[\w-]+)*$", self.hashtag.text):
        ht_valid = False
        alert("Please input hashtag(s) e.g. #Football")
      else:
        ht_valid = True
    if ht_valid:
      self.loadtweet.enabled = False
      self.custom_input.enabled = False
      self.hashtag.enabled = False
      while True:
        with Notification(self.wait_msg):
          self.text, self.fake_, self.real_, self.finurl_ = anvil.server.call("getprobstweet", self.hashtag.text)
        if self.text:
          self.loadtweet.enabled = True
          self.custom_input.enabled = True
          self.hashtag.enabled = True
          break
      self.loadtweet.enabled = True
      self.custom_input.enabled = True
      self.hashtag.enabled = True
      self.currtext = self.tweet_area.text
      self.tweet_area.text = self.text
      self.fake.text = self.fake_
      self.real.text = self.real_
      self.final_url.visible = True
      self.final_url.text, self.final_url.url = "Tweet (Source)", self.finurl_
    pass

  def check_box_1_change(self, **event_args):
    if self.custom_input.checked == True:
      self.tweet_area.enabled = True
      self.hashtag.enabled = False
      self.tweet_area.text = ""
      self.submit.visible = True
      self.final_url.visible = False
      self.loadtweet.enabled = False
      self.fake.text = ""
      self.real.text = ""
    else:
      self.hashtag.enabled = True
      self.tweet_area.text = ""
      self.fake.text = ""
      self.real.text = ""
      self.tweet_area.enabled = False
      self.submit.visible = False
      self.loadtweet.enabled = True
    pass

  def submit_click(self, **event_args):
    if self.tweet_area.text == "":
      alert("Please input text")
    else:
      if self.tweet_area.text != self.currtext:
        self.custom_input.enabled = False
        self.submit.enabled = False
        self.tweet_area.enabled = False
        with Notification(self.wait_msg):
          self.fake_, self.real_ = anvil.server.call('getprobscustom', self.tweet_area.text)
          self.fake.text = self.fake_
          self.real.text = self.real_
          self.currtext = self.tweet_area.text
        self.custom_input.enabled = True
        self.submit.enabled = True
        self.tweet_area.enabled = True
    pass












