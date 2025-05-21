#!/bin/bash

pytohn3 -m venv .venv

source .venv/bin/activate 

pip install -r reqruirement.txt

python -m spacy download es_core_news_sm --quiet
python -m spacy download xx_sent_ud_sm --quiet
