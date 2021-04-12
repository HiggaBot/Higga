@echo off
py -3 -m poetry install -q
py -3 -m poetry run py -3 -u .\main.py
