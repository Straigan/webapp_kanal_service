#!/bin/sh
celery -A webapp.celery_app flower --port=5555