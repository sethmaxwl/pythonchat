import time

from app import app
from flask import render_template, redirect, request, flash
from app.subscriber import get_messages
from app.publisher import publish_message
from app.chat_box import ChatBox

@app.route('/')
@app.route('/index')
def index():
    form = ChatBox()
    return render_template("index.html", messages=get_messages(), form=form)

@app.route('/publish')
def publish():
    msg = request.args.get('message')
    if (msg != ""):
        publish_message(request.args.get('message'))
    else:
        flash("Cannot send an empty message.", "danger")
    time.sleep(0.4)
    return redirect('/', code=302)
