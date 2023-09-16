import csv
import os

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="app/main/templates")



@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@router.get('/apps/')
def apps_page(request: Request):
    # Read data from the CSV file
    data_file_path = '/Users/mike/code/web-app-2/app/main/static/data/apps.csv'
    apps_data = []
    with open(data_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            apps_data.append(row)
            
    return templates.TemplateResponse('apps.html', {'request': request, 'apps': apps_data})


@router.get('/news/')
def news_page(request: Request):
    return templates.TemplateResponse('news.html', {'request': request})

@router.get('/learn/')
def learn_page(request: Request):
    return templates.TemplateResponse('learn.html', {'request': request})

@router.get('/about/')
def about_page(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})

