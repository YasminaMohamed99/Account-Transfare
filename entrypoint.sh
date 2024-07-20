#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate

echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass') if not User.objects.filter(username='admin').exists() else print('Superuser already exists')" | python manage.py shell

echo "Starting server..."
exec "$@"
