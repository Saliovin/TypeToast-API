#!/bin/sh

alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --port 80 --root-path /api --proxy-headers --forwarded-allow-ips=*