from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import re

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    set_default_error_handling(self.error_handler)
    self.text = None
    self.fake_ = None
    self.real_ = None
    self.finurl_ = None
    self.submit.enabled = False
    self.wait_msg = "Retrieving information from server, Please wait..."
    
  def error_handler(self, err):
    admin = "1811288@brunel.ac.uk"
    err = str(err)
    if "disconnected" in err:
      alert("The server is not currently available, please contact: " + admin,
            title = "Error: Server not runnning")
    else:
      alert(err + ", please contact: " + admin, title="An error has occurred")
      
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
          self.text, self.fake_, self.real_, self.finurl_ = anvil.server.call("response",
                                                                              self.hashtag.text,
                                                                              self.lm_dropdown.selected_value)
        if self.text:
          self.loadtweet.enabled = True
          self.custom_input.enabled = True
          self.hashtag.enabled = True
          break
      self.loadtweet.enabled = True
      self.custom_input.enabled = True
      self.hashtag.enabled = True
      self.tweet_area.text = self.text
      self.fake.text = self.fake_
      self.real.text = self.real_
      self.final_url.visible = True
      self.final_url.text, self.final_url.url = "Tweet (Source)", self.finurl_
    pass

  def custom_input_change(self, **event_args):
    if self.custom_input.checked == True:
      self.tweet_area.enabled = True
      self.hashtag.enabled = False
      self.tweet_area.text = ""
      self.submit.enabled = True
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
      self.submit.enabled = False
      self.loadtweet.enabled = True
    pass

  def submit_click(self, **event_args):
    if self.tweet_area.text == "":
      alert("Please input text")
    else:
        self.custom_input.enabled = False
        self.submit.enabled = False
        self.tweet_area.enabled = False
        with Notification(self.wait_msg):
          self.fake_, self.real_ = anvil.server.call('response', self.tweet_area.text,
                                                     self.lm_dropdown.selected_value, False)
          self.fake.text = self.fake_
          self.real.text = self.real_
        self.custom_input.enabled = True
        self.submit.enabled = True
        self.tweet_area.enabled = True
    pass

  def info_button_click(self, **event_args):
    alert("""INFO:
     1) Specify the input!
     
      - Load a random tweet
      - Input your own text
      
      2) Select a fine-tuned language model!
      
      - RoBERTa (OpenAI) : ~95% Accuracy
      - DeBERTa : 96% Accuracy
      - XLNet : 87% Accuracy
    
      3) Evaluate the text!
      
      - A greater HUMAN/REAL probability 
        indicates that your input was likely 
        HUMAN-written
        
      - A greater MACHINE/FAKE probability
        indicates that your input was likely
        MACHINE-written""")
      
    pass
