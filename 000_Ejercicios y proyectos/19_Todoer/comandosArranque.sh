#!/bin/bash
. venv/Scripts/activate
export FLASK_APP=todo
export FLASK_DEBUG=true
export FLASK_DATABASE_HOST='localhost'
export FLASK_DATABASE_PASSWORD='holamundo'
export FLASK_DATABASE_USER="Andrac"
export FLASK_DATABASE="prueba"
flask init-db
flask run