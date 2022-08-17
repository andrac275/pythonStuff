#!/bin/bash
. venv/Scripts/activate
export FLASK_APP=todo
export FLASK_DEBUG=true
flask run