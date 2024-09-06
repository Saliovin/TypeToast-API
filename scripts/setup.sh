#!/bin/sh

alembic upgrade head

fastapi run app/main.py --port 80 --root-path /api