@ECHO OFF 
TITLE ProCoder All Installation Processing.
ECHO Please wait... Checking system information.
pip install virtualenvwrapper-win && mkvirtualenv procoderenv && workon procoderenv && pip install -r requirements.txt
