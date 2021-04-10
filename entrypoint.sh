#!/bin/bash

echo 'Running tests with firefox'
BROWSER=firefox python -m unittest -v webtests.py
echo 'Running tests with chrome'
BROWSER=chrome python -m unittest -v webtests.py
