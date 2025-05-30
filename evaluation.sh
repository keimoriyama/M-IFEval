#!/bin/bash

set -e
source .venv/bin/activate

MODEL="sft-fLF6PZCG4i"

# python get_responses.py --model_name=../models/nemo-to-hf/sft-saZ2antXFW/

python -m evaluation_main --input_data=./data/ja_input_data.jsonl \
       	--input_response_data=./data/ja_input_response_data_..__models__nemo-to-hf__${MODEL}__.jsonl \
	--output_dir=./evaluation/ \
	--wandb_name=${MODEL}_eval
