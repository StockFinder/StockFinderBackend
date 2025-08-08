#!/bin/bash
gunicorn  -c create_db.py --workers 4 --bind 0.0.0.0:5000 server:app