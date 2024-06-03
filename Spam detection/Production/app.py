from flask import flask, render_template, request
import pickle

model = None
filename = './model/'


