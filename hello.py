from flask import Flask, flash, redirect, render_template, request, session, url_for
from celery import Celery
from mail_handler import Message


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.secret_key = b'\xe7ArPu\x01u\x12\xe0\x9d\x91\x10i\x94\x9e{\x12\x87\xd2\x1d\xa5\xb0\x82\xac'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/celery_email', methods=['GET', 'POST'])
def celery_email():
    if request.method == 'GET':
        return render_template('celery_email.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    # send the email
    email_data = {
        'subject': 'Hello from Flask',
        'to': email,
        'body': 'This is a test email sent from a background Celery task.'
    }
    if request.form['submit'] == 'Send':
        # send right away
        print('sending right away')
        send_async_email.delay(email_data)
        send_async_email(email_data)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[email_data], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('celery_email'))

@celery.task
def send_async_email(email_data):
    """Background task to send an email with Flask-Mail."""
    msg = Message(email_data['subject'],
                  sender='joe@moma.com',
                  recipients=[email_data['to']])
    msg.body = email_data['body']
    with app.app_context():
        msg.send()
        # mail.send(msg)