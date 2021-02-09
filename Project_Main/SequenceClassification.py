from pprint import pprint

from transformers import RobertaForSequenceClassification, RobertaTokenizer, logging
import torch

logging.set_verbosity_error()


class SequenceClassification:

    def __init__(self, model_pn="D:/Language Models/ROBERTA-LARGE/"):
        self.model = RobertaForSequenceClassification.from_pretrained(model_pn)
        self.tokenizer = RobertaTokenizer.from_pretrained(model_pn)
        self.ft_weights = torch.load('D:/Language Models/ROBERTA-LARGE/detector-large.pt', map_location='cpu')
        self.model.to(torch.device("cpu"))
        self.model.load_state_dict(self.ft_weights['model_state_dict'], strict=False)
        self.model.eval()
        self._text = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, raw_text):
        if not isinstance(raw_text, str):
            raise TypeError("Error: Invalid Input Type")
        else:
            self._text = raw_text

    def add_special_tokens(self, tokens):
        tokens = torch.tensor([self.tokenizer.bos_token_id] + tokens + [self.tokenizer.eos_token_id]).unsqueeze(0)
        return tokens

    def check_probs(self):
        tokens = self.tokenizer.encode(self._text, max_length=510, add_special_tokens=False)
        token_count = len(tokens)
        tokens = self.add_special_tokens(tokens)

        with torch.no_grad():
            logits = self.model(tokens.to("cpu"))[0]
            probs = logits.softmax(dim=-1)

        probs_ = probs.squeeze().tolist()
        probs_2dp = [("{:.2f}".format(i)) for i in probs_]

        return probs_2dp, token_count
