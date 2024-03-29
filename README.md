# Twitter-NFN-Detector

**A project created during my final year at university that provides a system to detect neural fake news/machine-generated Text on Twitter.**

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
  <img width="580" height="500" src="https://i.gyazo.com/ec12d55f1cf276a85c3286ca521e92fc.png">
</p>
<p align="center">https://twitter-nfn-bf.anvil.app/</p>

**Dissertation Abstract**

Neural Fake News (NFN), defined as neurally-generated misinformation masquerading as legitimate news, can be a critical societal issue. In recent years, unsupervised language models (ULMs) such as Generative Pre-trained Transformer-2 (GPT-2) have proven to generate extremely coherent paragraphs of text. These systems enable malicious actors to scale up their operations by delivering automatically generated disinformation across social media. Developing defence mechanisms against NFN is critical in preventing sites such as Twitter falling victim to an upsurge in the spread of synthetic text. I thus present a system that detects machine generated text that is broadcasted on Twitter, utilising fine-tuned pre-trained language models (PTLM) trained on the classification of outputs released with GPT-2. My system applies the weights released with the OpenAI detector model and two fine-tuned models: DeBERTa and XLNet, to classify real (human-written) and fake (machine-generated) text. I find that DeBERTa achieves a 96% classification accuracy with limited resources, competing with the OpenAI detector model that achieved ~95% across three sampling methods. I argue that with access to more powerful hardware capable of processing large sequence lengths, fine-tuning DeBERTa will likely outperform OpenAI’s detector. I also investigate the presence of machine-generated tweets on Twitter and find that they are not currently ubiquitous on social media. I conclude by discussing the importance of research into the detection of machine generated content and suggest that social media platforms implement classification systems as natural language generative models popularise. 

### Built With

* [Transformers](https://github.com/huggingface/transformers)
* [SimpleTransformers](https://github.com/ThilinaRajapakse/simpletransformers)
* [Anvil.Works](https://anvil.works/)
* [Python-Twitter-Tools](https://github.com/python-twitter-tools/twitter)
* [Firebase](https://firebase.google.com/)
* [OpenAI Detector](https://github.com/openai/gpt-2-output-dataset/tree/master/detector)
* [Trafilatura](https://github.com/adbar/trafilatura)

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

1) Install models and fine-tuned weights:

[OpenAI RoBERTa Detector](https://github.com/openai/gpt-2-output-dataset/tree/master/detector): 
   ```
   wget https://openaipublic.azureedge.net/gpt-2/detector-models/v1/detector-base.pt
   ```
Model: https://huggingface.co/roberta-large
#
Fine-tuned `DeBERTa-large` - (`5e-6`, `batch: 16`, `epochs: 4`, `warmup: 50`, `decay: 0.01`)
   ```
   https://drive.google.com/drive/folders/1P-EewnfcXvQR5UVzgavB9I_py1YFwQc7?usp=sharing
   ```
MCC: `0.913` | Accuracy: `0.956`

Model: https://huggingface.co/microsoft/deberta-large
#
Fine-tuned `XLNet-large-cased` - (`1e-5`, `batch: 16`, `epochs: 2`, `warmup: 100`):
   ```
   https://drive.google.com/drive/folders/1vtJ7Q2GqtOpNM7iIO5nX06we3BQJxUNr?usp=sharing
   ```
MCC: `0.771` | Accuracy: `0.878`

Model: https://huggingface.co/xlnet-large-cased
#
**_(XLNet and DeBERTa were fine-tuned on the outputs from the 1.5B GPT-2 model (xl-1542M) versus WebText, the [dataset](https://github.com/openai/gpt-2-output-dataset) used to train the GPT-2 model)_**
#
2) **Registration**:

* Register for a [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access)
* Register for an [anvil.works](https://anvil.works/) account
* Register and create new [Firebase](https://firebase.google.com/) project
#
### Installation

1) Download models + fine-tuned weights and store in an accessible location 
2) Generate [FireBase SDK Private Key](https://console.firebase.google.com/u/0/project/PROJECT_NAME/settings/serviceaccounts/adminsdk) 
and place credentials file within `Project_Main`
2) Initialize realtime database with `fake` and `real` nodes [(example)](https://i.gyazo.com/5fc0f5819e8f25282ab79661d4088dd5.png)
3) Clone the anvil app:

   ```sh
   https://anvil.works/build#clone:YG6YJDUEBCRAHCKA=Y4ALXWHEKMF34YBT4GEPCXJM
   ```
4) Set Anvil UPLINK key in `main_.py` and Twitter API keys in `TweetGetter.py`
5) Run the server file:
```
# (on the top-level directory of this repository)
pip install -r requirements.txt
python -m main_
```
6) Visit the anvil application link!

<!-- USAGE EXAMPLES -->
## Usage

**Load Tweet**: Pressing 'Load Tweet' requests and classifies (fake/real probablities) the latest available Tweet containing "#news", unless specified otherwise

**Custom Input**: Selecting the 'Custom Input' checkbox provides the option to provide a Twitter URL or any arbitrary input to be classified (fake/real probablities)

<!-- MARKDOWN LINKS AND IMAGES -->
[detector-screenshot]: "https://i.gyazo.com/ec12d55f1cf276a85c3286ca521e92fc.png"
