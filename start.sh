#!/bin/bash
uvicorn main:app --reload --reload-dir=app/main/templates --reload-dir=app/main/static

