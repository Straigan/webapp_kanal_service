#!/bin/sh
celery -A webapp.celery_app beat -l info