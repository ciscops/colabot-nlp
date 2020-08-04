#!/bin/bash
source venv/bin/activate
python build_model.py
exec gunicorn -b :5005 -w 2 app:app
