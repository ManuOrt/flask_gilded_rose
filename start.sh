#!/bin/bash

exec python migration.py &
exec python app.py
