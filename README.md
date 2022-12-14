# collapsible_xblock

# XBlock Test Task

Clone a repository:  
```
https://github.com/wQuelS/collapsible_xblock.git
```
Create and activate a virtual environment:  
```
python3 -m venv venv
source venv/bin/activate
```
Clone the XBlock-sdk:  
```
git clone https://github.com/openedx/xblock-sdk.git
```
Change directory to sdk directory and install requirements:
```
cd xblock-sdk
pip install -r requirements/base.txt
```
Make migrations
```
python manage.py migrate
cd ..
```
Inslall simplexblock
```
pip install -e simplexblock
```
Run local server (Note that you should be in sdk-dir)
```
cd xblock-sdk
python manage.py runserver
```
