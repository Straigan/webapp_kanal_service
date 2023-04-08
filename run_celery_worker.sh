#!/bin/sh
celery -A webapp.celery_app worker --loglevel=info
