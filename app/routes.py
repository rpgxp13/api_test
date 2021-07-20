from flask import request, redirect, url_for, session, flash
from app import app

@app.route('/')
def root():
