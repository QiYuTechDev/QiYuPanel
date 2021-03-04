
poetryRun:=cd panel && poetry run

run-dev:export DJANGO_SERVE_STATIC_FILES=1
run-dev:export DJANGO_DEV=1
run-dev:
	$(poetryRun) python manage.py makemigrations
	$(poetryRun) python manage.py migrate
	# $(poetryRun) gunicorn panel.asgi --reload -w 2 -k uvicorn.workers.UvicornWorker
	$(poetryRun) uvicorn --reload panel.asgi:application
