#!/bin/bash
python3 freeze.py && git add docs && git commit -a -m 'updating' && git push

