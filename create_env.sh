#!/bin/bash
deactivate
rm -rf marxgpt-env
python3 -m venv marxgpt-env
source marxgpt-env/bin/activate
pip install transformers torch ebooklib accelerate
