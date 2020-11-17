@echo off
echo This script will test and deploy Evaluation as a package to SSPA pypi server
echo Activating venv
call venv\Scripts\activate.bat
call python setup.py bdist_wheel
