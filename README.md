#DJANGP CV APP BY TODOROSCEAN DRAGOS
python3 -m venv venv 
source venv/bin/activate 
pip install django
python3 manage.py makemigrations    
python3 manage.py migrate  
python3 manage.py runserver 9000       
