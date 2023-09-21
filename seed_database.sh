

rm db.sqlite3
rm -rf ./bravoapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations bravoapi
python3 manage.py migrate bravoapi
python3 manage.py loaddata franchises
python3 manage.py loaddata seasons
python3 manage.py loaddata episodes
python3 manage.py loaddata users
python3 manage.py loaddata profiles
python3 manage.py loaddata tokens
python3 manage.py loaddata cast
python3 manage.py loaddata roles
python3 manage.py loaddata season_cast
python3 manage.py loaddata franchise_cast
python3 manage.py loaddata books
python3 manage.py loaddata profile_episodes
python3 manage.py loaddata review