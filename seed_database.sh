rm db.sqlite3
rm -rf ./bravoapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations bravoapi
python3 manage.py migrate bravoapi
python3 manage.py loaddata franchises
python3 manage.py loaddata seasons
python3 manage.py loaddata episodes