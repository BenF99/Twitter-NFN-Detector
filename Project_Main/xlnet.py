import csv
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
from scipy.special import softmax

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


class XLNetClassification:

    def __init__(self, model_pn="D:/Language Models/XLNET-LARGE/"):
        self._text = None
        # Hyperparameters
        # model_args = ClassificationArgs(num_train_epochs=2,
        #                                 warmup_ratio=0.1,
        #                                 train_batch_size=12,
        #                                 labels_list=['machine', 'human'],
        #                                 overwrite_output_dir=True,
        #                                 learning_rate=2e-5,
        #                                 save_model_every_epoch=True,
        #                                 use_multiprocessing=False,
        #                                 save_steps=-1)
        self.model = ClassificationModel("xlnet", model_pn, use_cuda=False)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, raw_text):
        if not isinstance(raw_text, str):
            raise TypeError("Error: Invalid Input Type")
        else:
            self._text = raw_text

    def check_probs(self):
        _, logits = self.model.predict([self._text])
        probs = softmax(logits[0])
        return probs

