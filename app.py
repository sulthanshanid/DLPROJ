from flask import Flask, render_template, request, jsonify, redirect, url_for, session as d
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import subprocess
from flask_login import login_required, current_user
import threading
import os
import json
from pyngrok import ngrok
ngrok.set_auth_token("2wfpiN1qtzcfqeX87UaTqXyhAWJ_3AUsK1K7dTcBrWV6XFdGR")
import pytz
from flask import flash
import requests
from lxml.html import soupparser
import re
import shutil
import collections
collections.Callable = collections.abc.Callable
from dateutil import parser
from bs4 import BeautifulSoup
from subprocess import Popen
import os.path
import easyocr
import pandas as pd
import re
from PIL import Image
import os
from anticaptchaofficial.imagecaptcha import *

import subprocess
import datetime
from os import listdir
from string import whitespace
from dateutil import parser
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import subprocess
import threading
import traceback
import subprocess
import logging
import os
from datetime import datetime
import subprocess
import logging
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from flask import Flask, send_from_directory, abort
from functools import wraps
from flask import session, abort

def superadmin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') != 'admin':  # Or check session.get('is_superadmin')
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

from flask import session
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)
scheduler = BackgroundScheduler()
scheduler.start()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Consider hashing passwords
    walletamount = db.Column(db.Float, default=0.0)
    captchaused = db.Column(db.Integer, default=0)
    tgtoken=db.Column(db.String(300), nullable=True)
    chatid=db.Column(db.Integer, nullable=True)
class ScheduledTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applications = db.Column(db.Text, nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    scheduled_date = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(50), default="Pending")
    output = db.Column(db.Text, nullable=True)
    log_file = db.Column(db.String(100), nullable=True)
    cov = db.Column(db.String(50), nullable=True)
    slotdate = db.Column(db.String(10), nullable=False)
    careoff= db.Column(db.String(10), nullable=False)
    proxy = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    extra = db.Column(db.String(255), nullable=True) 
    rundate = db.Column(db.String(255), nullable=True) 
class SchedulingSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scheduling_time = db.Column(db.Time, nullable=False, default="08:55:00")

    
with app.app_context():
    db.create_all()

global active_processes
active_processes = {}
@app.route('/createuserr', methods=['GET'])
def create_admin_user():
    # Check if the admin user already exists
    admin_user = User.query.filter_by(username='admin').first()

    if admin_user:
        # Update the password if user exists
        admin_user.password = "Sahad"
        db.session.commit()
        return jsonify({"message": "Admin user password updated!"}), 200

    # Create a new admin user
    admin_user = User(username='admin', password="Sahad")
    db.session.add(admin_user)
    db.session.commit()

    return jsonify({"message": "Admin user created successfully!"}), 201


@app.route('/')
def index():
    if 'logged_in' not in d:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['logged_in'] = True
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid login credentials", 403

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        username = session['username']
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template(
                'dashboard.html',
                username=user.username,
                walletamount=user.walletamount,
                captchaused=user.captchaused
            )
    return redirect(url_for('login'))


@app.route('/fetch_task_data', methods=['POST'])
def fetch_task_data():
                        caperror = "Enter Valid Captcha.".encode()
                        data = request.json
                        print(data)
                        response_data = []
                        total_captcha_attempts = 0 
                        for task in data:
                            ispassed=0
                            applicationid = task['applno']
                            dobfinal = task['dob']
                            while ispassed==0:
                               total_captcha_attempts += 1
                               t=requests.Session()
                               rewww01_url = "https://sarathi.parivahan.gov.in/sarathiservice/jsp/common/captchaimage.jsp"
                               rewww01_header = {"Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do",
                                                  "Connection": "close"}
                               burp_req = t.get(rewww01_url, headers=rewww01_header)
                               with open('CAPTCHA.jpg', 'wb') as out_file:
                                   for chunk in burp_req.iter_content(chunk_size=128):
                                       out_file.write(chunk)

                               solver = imagecaptcha()
                               solver.set_verbose(1)
                               solver.set_key("977a77e4f59ad05bbdd91b80c9bccc89")

                               # Specify softId to earn 10% commission with your app.
                               # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
                               solver.set_soft_id(0)
                               solver.set_case("true")
                               
                               captchaa = solver.solve_and_return_solution('CAPTCHA.jpg')
                               
                               #captchaa=input("enter c : ")
                               if captchaa != 0:
                                   print("captcha text " + captchaa)
                               else:
                                   print("task finished with error " + solver.error_code)
                               # captchaa = input("captcha : ")
                               print(captchaa)
                               cov_url = "https://sarathi.parivahan.gov.in:443/sarathiservice/applViewStages.do"
                               cov_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                                "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/applCancel.do",
                                                "Connection": "close"}
                               cov_data = {"applNum": applicationid, "dateOfBirth": dobfinal, "entcaptxt": captchaa,"newll.submit": "Submit"}

                               cov1_req = t.post(cov_url, headers=cov_headers,data=cov_data)
                               response123 = cov1_req.content


                               if caperror  in response123:
                                   print("Captcha error")
                                   continue
                               else:
                                   ispassed =1
                                   print("Captcha success")
                                   break



                          
                            soup = BeautifulSoup(cov1_req.content, 'html.parser')
                            #print(cov1_req.content)
                            try:
                                table = soup.find_all('table', class_="table table-bordered table-hover")[0]

                            except Exception as e:
                                try:
                                  error_message = soup.select_one('.errorMessage li span').text.strip()
                                  print('Error Message Cov:', e,error_message)
                                  username = session.get('username')
                                  user = User.query.filter_by(username=username).first()
                                  if user:
                                            user.captchaused += total_captcha_attempts
                                            db.session.commit()
                                  
                                except Exception as e:
                                    username = session.get('username')
                                    user = User.query.filter_by(username=username).first()
                                    if user:
                                            user.captchaused += total_captcha_attempts
                                            db.session.commit()

                                
                                

                                # Convert the table to a DataFrame
                            df = pd.read_html(str(table))[0]
                            #print(df)
                            name = df.iat[1, 1]
                            print(name)
                            appdate =df.iat[0,3]
                            today = datetime.today()
                            current_year = datetime.now().year
                            print(appdate)
                                


                            # Extract the year from the given date
                            appdate = int(appdate.split('-')[2])
                            oldapplicationid = applicationid
                            

                            # Check if the given year matches the current year
                            try:
                                try:

                                    table=soup.find_all('table', class_="table table-bordered")[1]


                                except Exception as e:
                                    try:
                                        table = soup.find_all('table', class_="table table-bordered")[0]
                                    except  Exception as e:
                                        error_message = soup.select_one('.errorMessage li span').text.strip()
                                        print('Error Message:', error_message)
                                        username = session.get('username')
                                        user = User.query.filter_by(username=username).first()
                                        if user:
                                            user.captchaused += total_captcha_attempts
                                            db.session.commit()
                                        



                                df = pd.read_html(str(table).upper())[0]
                                vauleofcov = df.at[0, 'CLASS OF VEHICLES']
                                try:
                                 table = soup.find_all('table', class_="table table-bordered table-hover marginStyle")[0]
                                except Exception as e:
                                    applicationid=oldapplicationid
                                    response_data.append({"applno": applicationid, "name": name, "cov": vauleofcov})
                                    username = session.get('username')
                                    user = User.query.filter_by(username=username).first()
                                    if user:
                                        user.captchaused += total_captcha_attempts
                                        db.session.commit()
                                    continue
                                df = pd.read_html(str(table).upper())
                                #print(df)
                                df = df[0]
                                df = df[::-1]
                                df.columns = df.iloc[0]
                                df = df[1:]
                                #print(df)
                                filtered_df = df[(df['TRANSACTION'] == 'LEARNER AND DRIVING LICENCES')]


                                filtered_df1 = df[df['TRANSACTION'] == 'ISSUE OF LEARNERS LICENCE']
                                if not filtered_df.empty:
                                    print("FINDING OLD APPID")
                                    print("Value of 'OLD APPLICATION NO.':",
                                            filtered_df.iloc[0]['APPLICATION NO.'])

                                    oldapplicationid = filtered_df.iloc[0]['APPLICATION NO.']
                                    print(oldapplicationid)
                                # Convert 'APPLICATION DATE' to datetime
                                filtered_df1['APPLICATION DATE'] = pd.to_datetime(filtered_df1['APPLICATION DATE'],
                                                                                    format='%d-%m-%Y')
                                if not filtered_df1.empty:
                                    latest_application = filtered_df1.loc[filtered_df1['APPLICATION DATE'].idxmax()]
                                    print("Value of 'new APPLICATION NO.':", latest_application['APPLICATION NO.'])
                                    applicationid = latest_application['APPLICATION NO.']

                            except Exception as e:
                                

                                traceback.print_exc()
                                response_data.append({"applno": applicationid, "error": error_message})
                                username = session.get('username')
                                user = User.query.filter_by(username=username).first()
                                if user:
                                    user.captchaused += total_captcha_attempts
                                    db.session.commit()
                                pass
                            applicationid=oldapplicationid
                            response_data.append({"applno": applicationid, "name": name, "cov": vauleofcov})
                            username = session.get('username')
                            user = User.query.filter_by(username=username).first()
                            if user:
                                user.captchaused += total_captcha_attempts
                                db.session.commit()
                        return jsonify(response_data)
                            

from datetime import datetime, timedelta, time


# Assuming `scheduler` has been initialized as an instance of BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()



@app.route('/schedule', methods=['POST']) 
def schedule_task():
    if 'username' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.json
    tasks = data.get('tasks')
    rundate_str = data.get('rundate')  # <-- Get rundate from POST
    if not tasks or not rundate_str:
        return jsonify({'message': 'Tasks and rundate are required'}), 400

    task_count = len(tasks)

    # Fetch user and check wallet
    user = User.query.filter_by(username=session['username']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user.walletamount < task_count:
        return jsonify({'message': 'Insufficient wallet balance to schedule tasks'}), 403

    # Time calculations
    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)

    try:
        rundate = datetime.strptime(rundate_str, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({'message': 'Invalid rundate format. Use YYYY-MM-DD'}), 400

    # Determine run time based on rundate
    if rundate == now.date():
        run_time = (now + timedelta(seconds=30)).astimezone(pytz.utc)
    else:
        run_datetime_ist = india.localize(datetime.combine(rundate, time(8, 44)))
        run_time = run_datetime_ist.astimezone(pytz.utc)

    # Schedule tasks
    for task in tasks:
        new_task = ScheduledTask(
            applications=task['applno'],
            dob=datetime.strptime(task['dob'], "%d-%m-%Y").strftime("%d-%m-%Y"),
            cov=str(task['cov']).replace(" ", ""),
            scheduled_date=now.strftime("%Y-%m-%d"),
            status="Pending",
            slotdate=datetime.strptime(task['slotdate'], "%Y-%m-%d").strftime("%d-%m-%Y"),
            careoff=user.username,
            proxy=task['proxy'],
            name=task['name'],
            rundate=run_time
        )
        db.session.add(new_task)
        db.session.flush()

        scheduler.add_job(run_game_script, 'date', run_date=run_time, args=[new_task.id])

    # Deduct wallet after successful scheduling
    user.walletamount -= task_count
    db.session.commit()

    return jsonify({
        'message': 'Tasks scheduled successfully',
        'scheduled_time': run_time.strftime('%Y-%m-%d %H:%M:%S UTC')
    }), 201

@app.route('/schedule1', methods=['POST']) 
def schedule_task1():
    if 'username' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.json
    tasks = data.get('tasks')
    if not tasks:
        return jsonify({'message': 'No tasks provided'}), 400

    task_count = len(tasks)

    # Fetch user and check wallet
    user = User.query.filter_by(username=session['username']).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user.walletamount < task_count:
        return jsonify({'message': 'Insufficient wallet balance to schedule tasks'}), 403

    # Time calculations
    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)
    today_9am = india.localize(datetime.combine(now.date(), time(9, 0)))
    tomorrow_6am = india.localize(datetime.combine(now.date() + timedelta(days=1), time(6, 0)))

    # Determine run time
    if now < today_9am:
        run_time = (now + timedelta(seconds=30)).astimezone(pytz.utc)
    else:
        run_time = (now + timedelta(seconds=30)).astimezone(pytz.utc)

    # Schedule tasks
    for task in tasks:
        new_task = ScheduledTask(
            applications=task['applno'],
            dob=datetime.strptime(task['dob'], "%d-%m-%Y").strftime("%d-%m-%Y"),
            cov=str(task['cov']).replace(" ", ""),
            scheduled_date=now.strftime("%Y-%m-%d"),
            status="Pending",
            slotdate=datetime.strptime(task['slotdate'], "%Y-%m-%d").strftime("%d-%m-%Y"),
            careoff=user.username,
            proxy=task['proxy'],
            name=task['name'],
            extra=datetime.strptime(task['slotdate1'], "%Y-%m-%d").strftime("%d-%m-%Y")
        )
        db.session.add(new_task)
        db.session.flush()  # get ID before commit

        scheduler.add_job(run_game_script1, 'date', run_date=run_time, args=[new_task.id])

    # Deduct wallet only after successful scheduling
    user.walletamount -= task_count
    db.session.commit()

    return jsonify({
        'message': 'Tasks scheduled successfully',
        'scheduled_time': run_time.strftime('%Y-%m-%d %H:%M:%S UTC')
    }), 201




# Ensure the 'logs' directory exists
os.makedirs('logs', exist_ok=True)
import sqlite3
def retry_commit(session, retries=5, delay=1):
    for attempt in range(retries):
        try:
            session.commit()
            return  # If commit succeeds, return
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e):
                time.sleep(delay)  # Wait before retrying
                continue
            else:
                raise  # Re-raise other database errors
    raise sqlite3.OperationalError("Failed to commit to the database after multiple retries.")

import subprocess
import logging
from datetime import datetime





def run_game_script(task_id):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S%f')
    log_file = f'logs/{task_id}_{timestamp}.log'

    logger = logging.getLogger(f'task_{task_id}')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    captcha_used = 0
    user = None

    with app.app_context():
        task = ScheduledTask.query.get(task_id)
        if not task:
            logger.error(f"Task ID {task_id} not found.")
            return

        task.status = "Running"
        task.log_file = log_file
        retry_commit(db.session)

        logger.info(f"Starting task ID {task_id} for application {task.applications}")

        command = [
            "python", "-u", "game.py",
            task.applications, task.cov, task.dob, task.slotdate, task.careoff, task.proxy
        ]

        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            active_processes[task_id] = process

            stdout_lines = []
            stderr_lines = []

            # Read stdout live
            while True:
                line = process.stdout.readline()
                if line:
                    stdout_lines.append(line)
                    logger.info(line.strip())
                    if "CAPTCHA_USED:" in line:
                        try:
                            captcha_used = int(line.strip().split("CAPTCHA_USED:")[1])
                        except Exception as e:
                            logger.warning(f"Failed to parse captcha used: {e}")
                elif process.poll() is not None:
                    break

            # Ensure all remaining output is read
            for line in process.stdout.read().splitlines():
                logger.info(line.strip())

            for line in process.stderr.read().splitlines():
                stderr_lines.append(line)
                logger.error(line.strip())

            
            print(process.returncode,"hiii")
            if process.returncode == 0:
                task.status = "Completed"
            else:
                task.status = "Failed"
                if user:
                    user.walletamount += 1

        except FileNotFoundError:
            task.status = "Failed"
            logger.error("game.py not found")

        finally:
            if captcha_used > 0 and user:
                user.captchaused += captcha_used

            task.log_file = log_file
            retry_commit(db.session)
            logger.info(f"Task ID {task_id} status updated to {task.status}")
            logger.handlers.clear()
from logging.handlers import RotatingFileHandler

def run_game_script1(task_id):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S%f')
    log_file = f'logs/{task_id}_{timestamp}.log'

    logger = logging.getLogger(f'task_{task_id}')
    logger.setLevel(logging.INFO)

    # Use RotatingFileHandler to limit log file size (1MB here)
    file_handler = RotatingFileHandler(log_file, maxBytes=1*1024*1024, backupCount=0)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    captcha_used = 0
    user = None  # Define user early so it's in scope

    with app.app_context():
        task = ScheduledTask.query.get(task_id)
        if not task:
            logger.error(f"Task ID {task_id} not found.")
            return

        task.status = "Running"
        task.log_file = log_file
        retry_commit(db.session)

        logger.info(f"Starting task ID {task_id} for application {task.applications}")

        command = ["python", "-u", "c.py", task.applications, task.dob, task.cov, task.slotdate, task.extra]
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            active_processes[task_id] = process

            for line in iter(process.stdout.readline, ''):
                logger.info(line.strip())

                # Capture "CAPTCHA_USED:" lines
                if "CAPTCHA_USED:" in line:
                    try:
                        captcha_used = int(line.strip().split("CAPTCHA_USED:")[1])
                        logger.info(f"Parsed captcha used: {captcha_used}")
                    except Exception as e:
                        logger.warning(f"Failed to parse captcha used: {e}")

            process.wait()

            if process.returncode == 0:
                task.status = "Completed"
            else:
                task.status = "Failed"
                for error_line in iter(process.stderr.readline, ''):
                    logger.error(error_line.strip())
                user = User.query.filter_by(username=session.get('username')).first()
                if user:
                    user.walletamount += 1  # refund

        except FileNotFoundError:
            task.status = "Failed"
            logger.error("c.py not found")

        finally:
            if captcha_used > 0 and user:
                user.captchaused += captcha_used

            task.log_file = log_file
            retry_commit(db.session)
            logger.info(f"Task ID {task_id} status updated to {task.status}")
            logger.handlers.clear()

@app.route('/fetch_slot_checkdate', methods=['POST'])

def fetch_slot_checkdate():
    slots = ['SLOT1 (08.00-08.10)', 'SLOT2 (08.11-08.20)', 'SLOT3 (08.21-08.30)', 'SLOT4 (08.31-08.40)']
    
    # Simulate fetching slotdate and checkdate
    s = requests.Session()
    burp0_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?id=sardlenq"
    burp0_headers = {"Referer": "https://sarathi.parivahan.gov.in/sarathiservice/stateSelectBean.do",
                     "Connection": "close"}
    burp0_request = s.get(burp0_url, headers=burp0_headers)
    burp0_response = burp0_request.headers
    # print(burp0_response)
    Cookie = (burp0_response['Set-Cookie'])
    # print(Cookie)

    burp1_url = "https://sarathi.parivahan.gov.in:443/slots/stateBean.do"
    burp1_headers = {"Content-Type": "application/x-www-form-urlencoded",
                     "Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.dO", "Connection": "close"}
    burp1_data = {"stCode": "KL", "stName": "Kerala", "rtoCode": "KL14", "rtoName": "0"}
    burp1_req = s.post(burp1_url, headers=burp1_headers, data=burp1_data)
    # print(burp1_req)

    burp2_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&opernType=loadCOVs&trackCode=0"
    burp2_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
    burp2_req = s.get(burp2_url, headers=burp2_headers,data=None)
    # print(burp2_req.content)

    burp3_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=checkSlotTimes"
    burp3_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
    burp3_req = s.get(burp3_url, headers=burp3_headers,data=None)
    # print(burp3_req.content)

    burp4_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=loadDLQuotaDet&trackCode=0&trkrto=0&radioType=RTO"
    burp4_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
    REQ = s.get(burp4_url, headers=burp4_headers,data=None)
    DATA = REQ.content
    #print(DATA)
    soup = BeautifulSoup(REQ.content, 'html.parser')
    table = soup.find('table', class_='table-mod1')
    df = pd.read_html(str(table).upper())[0]
    df.columns = df.iloc[0]
    print(df)
    df = df.tail(-1)
    #print(df)
    df[slots] = df[slots].astype(float)

# Filter the DataFrame based on the condition
    filtered_df = df[df[slots].gt(-0).any(axis=1)]
    print(filtered_df)
    
    # Save the filtered DataFrame to CSV
    filtered_df.to_csv('SLOT_TABLE.csv', sep='\t', index=False)

    # Check if there are any rows in the filtered DataFrame
    if not filtered_df.empty:
        # Read the filtered CSV file back into a DataFrame
        df3 = pd.read_csv('SLOT_TABLE.csv', sep='\t')
        df3.set_index('DATE', inplace=True)
    
        # Iterate through the rows and print the dates where slots contain positive values
        for rowIndex, row in df3.iterrows():
            for columnIndex, value in row.items():
                try:
                    if value > 0:
                        print(f"SLOTDATE : {rowIndex}")
                        SLOTDATE=str(rowIndex)
                except TypeError:
                    pass
    else:
        # If the filtered DataFrame is empty, prompt the user to enter a date
        SLOTDATE = "" 
    return jsonify({"slotdate": SLOTDATE})
from flask import g

@app.route('/live_status/<int:task_id>')
def live_status(task_id):
    task = ScheduledTask.query.get(task_id)
    
    # Ensure task exists
    if not task or not task.log_file:
        return jsonify({'error': 'Task or log file not found'}), 404

    # AUTHORIZATION: check if the logged-in user is the task's careoff
    

    # Stream logs if user owns the task
    def stream_logs():
        with open(task.log_file, 'r') as log_file:
            while True:
                line = log_file.readline()
                if not line:
                    break
                yield f"{line.strip()}\n"

    return app.response_class(stream_logs(), mimetype='text/plain')


@app.route('/add_task')
def add_task():
    # Query all scheduled tasks from the database
    
    
    # Return tasks in a simple HTML table view
    return render_template('addtask.html')
@app.route('/add_task_check')
def add_task1():
    # Query all scheduled tasks from the database
    
    
    # Return tasks in a simple HTML table view
    return render_template('addtaskcheck.html')
from flask import session, redirect, url_for

@app.route('/view_tasks')
def view_tasks():
    if 'username' not in session:
        return redirect(url_for('login'))  # redirect to login if not logged in

    username = session['username']

    # Only get tasks for this user
    tasks = ScheduledTask.query.filter_by(careoff=username).all()
    careoffs = sorted(set(task.careoff for task in tasks))

    return render_template("view_tasks.html", tasks=tasks, careoffs=careoffs)

    # Return tasks in a simple HTML table view
    
from flask import session, abort

@app.route('/kill_task/<int:task_id>', methods=['GET'])
def kill_task(task_id):
    if 'username' not in session:
        abort(401)  # Unauthorized

    task = ScheduledTask.query.get(task_id)

    if not task:
        return jsonify({'error': f'Task ID {task_id} not found'}), 404

    if task.careoff != session['username']:
        abort(403)  # Forbidden

    # If task is already completed or failed, do not kill
    if task.status in ['Completed', 'Failed']:
        return jsonify({'message': f'Task ID {task_id} has already {task.status.lower()}, cannot be killed.'}), 400

    process = active_processes.get(task_id)

    if not process or process.poll() is not None:
        # Process might have ended but not removed from active_processes
        task.status = "Failed"
        retry_commit(db.session)
        active_processes.pop(task_id, None)
        return jsonify({'message': f'Task ID {task_id} was not running. Status set to Failed in DB.'}), 200

    try:
        process.terminate()
        process.wait(timeout=5)
        task.status = "Failed"
        retry_commit(db.session)
    except subprocess.TimeoutExpired:
        process.kill()
        task.status = "Failed"
        retry_commit(db.session)
        return jsonify({'message': f'Task ID {task_id} forcefully terminated and marked as Failed'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to terminate task ID {task_id}: {str(e)}'}), 500
    finally:
        active_processes.pop(task_id, None)

    return jsonify({'message': f'Task ID {task_id} terminated successfully and marked as Failed'}), 200




from flask import send_file, abort
import os

@app.route('/pdf/<applno>')
def send_pdf(applno):
    # Root directory where PDFs are stored
    pdf_root = os.path.join(app.root_path, '')

    # Walk through all subdirectories
    for root, dirs, files in os.walk(pdf_root):
        for file in files:
            if file.endswith('.pdf') and applno in file:
                pdf_path = os.path.join(root, file)
                return send_file(pdf_path, as_attachment=True)

    # If no matching PDF found
    abort(404, description=f"No PDF found with '{applno}' in filename.")


@app.route('/imgtoappl', methods=['POST'])
def img_to_appl():
    if 'username' not in session:
        abort(401)  # Unauthorized
    # This is a mock implementation. Replace it with your actual logic.
    # The request should include paths to the images for processing.
    data = request.get_json()
    image_paths = data.get('paths', [])

    if not image_paths:
        return jsonify({'error': 'No image paths provided'}), 400

    # Simulate processing and returning application numbers and DOBs
    results = []
    for idx, path in enumerate(image_paths):
        
            try:
                        print("-------------------------------------------------------------------------------------")
                       
                        print("Processing image:", path)

                        # Read the image file in binary mode
                        with open(path, "rb") as image_file:
                            image_data = image_file.read()

                        
                        print("\n")
                        print("Processing image:", path)

                        # Perform OCR on the image
                        headers = {
                            "Cookie": "MMCASM=ID=0103E2B3466B44BDA0639A88496C0909;",  # Replace with a valid cookie
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                        }

                        # Get the current directory
                        folder_dir = os.getcwd()

                        
                        import base64
                        from requests_toolbelt.multipart.encoder import MultipartEncoder


                        # Step 1: Encode the image in Base64
                        with open(path, "rb") as img_file:
                            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

                        # Step 2: Send image to Bing Image Search API
                        url_upload = "https://www.bing.com/images/search?view=detailv2&iss=sbiupload&FORM=SBIVSP"
                        multipart_data = MultipartEncoder(fields={"cbir": "sbi", "imageBin": encoded_image})
                        headers["Content-Type"] = multipart_data.content_type
                        response = requests.post(url_upload, headers=headers, data=multipart_data,
                                                allow_redirects=False)

                        # Step 3: Extract insightsToken from redirect URL
                        if "Location" in response.headers:
                            redirect_url = response.headers["Location"]
                            match = re.search(r"insightsToken=([^&]+)", redirect_url)
                            if match:
                                insights_token = match.group(1)
                                # print("Extracted insightsToken:", insights_token)
                            else:
                                print("insightsToken not found.")
                                continue
                        else:
                            print("No redirect location found.")
                            continue

                        # Step 4: Send request for OCR text extraction
                        url_knowledge = "https://www.bing.com/images/api/custom/knowledge?skey=AgaSJGcgQ131498nAy7btVt_1NdDNxy1QhIqsZbgBrw"
                        knowledge_request_data = {
                            "imageInfo": {"imageInsightsToken": insights_token, "source": "Url",
                                        "cropArea": {"top": "0", "left": "0", "right": "1",
                                                    "bottom": "1"}},
                            "knowledgeRequest": {"invokedSkills": ["OCR"], "index": 2}
                        }
                        multipart_data_2 = MultipartEncoder(
                            fields={"knowledgeRequest": str(knowledge_request_data)})
                        headers["Content-Type"] = multipart_data_2.content_type
                        response_knowledge = requests.post(url_knowledge, headers=headers,
                                                        data=multipart_data_2)

                        # Step 5: Extract and clean OCR results
                        if response_knowledge.status_code == 200:
                            extracted_text = response_knowledge.text.replace("\\", "")
                            extracted_text = extracted_text.replace(".", "")  # Remove escape slashes
                            # print("OCR Extracted Text:", extracted_text)

                            # Use regex patterns
                            phoneNumRegex2 = re.compile(r'KL\s*\d+\s*/\s*\d+\s*/\s*\d+')
                            application_no_pattern = r"Application No : (\d+)"
                            dob_pattern = r"(\d{2}-\d{2}-\d{4})"

                            mo = phoneNumRegex2.search(extracted_text)
                            matches = re.search(application_no_pattern, extracted_text)
                            matchess = re.findall(dob_pattern, extracted_text)

                            success = 0
                            valid_dobs = [dob for dob in matchess if int(dob[-4:]) <= 2019]

                            if mo:
                                learner = str(mo.group()).replace(" ", "")
                                learner = str(learner[:4] + " " + learner[4:17])
                                print("Learner ID:", learner)

                                dob_url = "https://sarathi.parivahan.gov.in:443/sarathiservice/getApplNumAndDobByLicNum.do"
                                dob_headers = {
                                    "Accept": "application/json, text/javascript, */*; q=0.01",
                                    "X-Requested-With": "XMLHttpRequest",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/printlearerslicence.do",
                                    "Connection": "close"
                                }
                                dob_data = {"licNum": learner}
                                dob_req = requests.post(dob_url, headers=dob_headers, data=dob_data)
                                dob = dob_req.text.replace('"', '')
                                dobfinal = dob.split('#')[1]
                                applicationid = dob.split('#')[0]
                                success = 1

                            if valid_dobs:
                                dobfinal = valid_dobs[0]
                                if matches:
                                    applicationid = matches.group(1)
                                    success = 1

                            if success == 0:
                                print("Error: Could not extract required information.")
                                continue

                            print("Application ID:", applicationid)
                            print("Date of Birth:", dobfinal)
                        else:
                            print("Error in OCR extraction:", response_knowledge.status_code)
                            continue
                        print(applicationid + "\n" + dobfinal)
                        dob_object = datetime.strptime(dobfinal, "%d-%m-%Y")
                        dobfinal_new = dob_object.strftime("%Y-%m-%d")
                        results.append({
            'applno': applicationid,  # Mock application number
            'dob': dobfinal_new        # Mock DOB
                     })

            except Exception as e:
                print(e)
                import traceback

                traceback.print_exc()
                continue
    results = list(results)  # Convert set to list
    return jsonify({'data': results})
@app.route('/upload', methods=['POST'])
def upload_images():
    if 'username' not in session:
        abort(401)  # Unauthorized

    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400

    files = request.files.getlist('files[]')
    paths = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            paths.append(filepath)
        else:
            return jsonify({'error': f"File '{file.filename}' is not allowed"}), 400

    return jsonify({'paths': paths})

from flask import send_file
@app.route('/superadmin/dashboard', methods=['GET', 'POST'])
@superadmin_required
  # Assuming superadmin has a login system
def superadmin_dashboard():
    # Fetch the first scheduling settings entry
    settings = SchedulingSettings.query.first()
    
    if not settings:
        # Default scheduling time
        scheduling_time = datetime.strptime("08:55:00", "%H:%M:%S").time()
        settings = SchedulingSettings(scheduling_time=scheduling_time)
        db.session.add(settings)
        db.session.commit()

    if request.method == 'POST':
        new_time = request.form.get('scheduling_time')
        if new_time:
            try:
                # Convert input to time object and update settings
                new_time_obj = datetime.strptime(new_time, "%H:%M").time()
                settings.scheduling_time = new_time_obj
                db.session.commit()
                flash("Scheduling time updated successfully!", "success")
            except ValueError:
                flash("Invalid time format. Please use HH:MM.", "danger")
        else:
            flash("No time provided. Please enter a valid time.", "warning")

    # For both GET and POST, fetch tasks and render the dashboard
    tasks = scheduler.get_jobs()
    schedules = []

# Get jobs from the scheduler
    jobs = scheduler.get_jobs()
    if not jobs:
      print("No jobs found!")
    else:
       for job in jobs:
        jobdict = {
            "job_id": job.id,
            "function": job.func_ref,
            "next_run_time": job.next_run_time
            
        }
        # Safely extract fields
        try:
            for field in job.trigger.fields:
                jobdict[field.name] = str(field)
        except AttributeError:
            print(f"Job {job.id} has no trigger fields.")

        schedules.append(jobdict)

    for schedule in schedules:
     print(schedule) 



# Pass tasks to the template
    return render_template('superadmin_dashboard.html', settings=settings,tasks=schedules)


@app.route('/superadmin/kill_task/<task_id>', methods=['POST'])
def kill_taskk(task_id):
    

    try:
        scheduler.remove_job(task_id)

        flash(f'Task {task_id} has been killed!', 'success')
    except Exception as e:
        flash(f'Error killing task {task_id}: {str(e)}', 'danger')

    return redirect(url_for('superadmin_dashboard'))
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

from flask import session, abort


@app.route('/pdfs/<careoff>')
@superadmin_required
def zip_pdfs_by_careoff(careoff):
    import datetime
    import io
    from zipfile import ZipFile

    # Get today's date as folder name (e.g., '27-10-2025')
    today = datetime.date.today().strftime("%d-%m-%Y")
    
    # Directory path: pdfs/27-10-2025/<careoff>
    pdf_folder = os.path.join(app.root_path, today, careoff)

    # Check if directory exists
    if not os.path.isdir(pdf_folder):
        abort(404, description=f"No PDFs found for careoffff '{careoff}' on {today}.")

    # Collect all .pdf files in the directory
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not pdf_files:
        abort(404, description=f"No PDF files found for careoff '{careoff}' on {today}.")

    # Create in-memory ZIP file
    memory_file = io.BytesIO()
    with ZipFile(memory_file, 'w') as zipf:
        for pdf in pdf_files:
            filepath = os.path.join(pdf_folder, pdf)
            zipf.write(filepath, arcname=pdf)

    memory_file.seek(0)

    # Send the ZIP file as response
    zip_filename = f"{careoff}_pdfs_{today}.zip"
    return send_file(
        memory_file,
        mimetype='application/zip',
        download_name=zip_filename,
        as_attachment=True
    )

from flask import request, redirect, url_for, flash

from flask import request, redirect, url_for, flash
from werkzeug.security import generate_password_hash  # for password hashing

from flask import request, redirect, url_for, flash, render_template


@app.route('/superadmin/user_stats', methods=['GET', 'POST'])
@superadmin_required
def user_stats():
    if request.method == 'POST':
        form = request.form

        # Update existing user: wallet, tgToken, chatid
        if 'new_balance' in form and 'careoff' in form:
            careoff = form.get('careoff')
            new_balance = form.get('new_balance')
            new_tgtoken = form.get('new_tgtoken')
            new_chatid = form.get('new_chatid')

            user = User.query.filter_by(username=careoff).first()
            if user:
                try:
                    user.walletamount = float(new_balance)
                    if new_tgtoken is not None:
                        user.tgtoken = new_tgtoken.strip()
                    if new_chatid is not None:
                        user.chatid = new_chatid.strip()
                    db.session.commit()
                    flash(f"Wallet, tgToken, and chatid for {careoff} updated.", "success")
                except Exception as e:
                    db.session.rollback()
                    flash(f"Error updating user {careoff}: {str(e)}", "danger")
            else:
                flash(f"User {careoff} not found", "danger")

            return redirect(url_for('user_stats'))

        # Add new user: includes chatid
        elif all(k in form for k in ('username', 'password', 'wallet_balance', 'tgtoken')):
            username = form.get('username').strip()
            password = form.get('password')
            wallet_balance = form.get('wallet_balance')
            tgtoken = form.get('tgtoken').strip()
            chatid = form.get('chatid', '').strip()

            if User.query.filter_by(username=username).first():
                flash(f"User {username} already exists.", "danger")
                return redirect(url_for('user_stats'))

            try:
                new_user = User(
                    username=username,
                    walletamount=float(wallet_balance),
                    tgtoken=tgtoken,
                    chatid=chatid if chatid else None
                )
                new_user.set_password(password)
                db.session.add(new_user)
                db.session.commit()
                flash(f"User {username} added successfully.", "success")
            except Exception as e:
                db.session.rollback()
                flash(f"Error adding user: {str(e)}", "danger")

            return redirect(url_for('user_stats'))

    # GET: Display stats
    users = User.query.all()
    stats = []
    for user in users:
        total = ScheduledTask.query.filter_by(careoff=user.username).count()
        failed = ScheduledTask.query.filter_by(careoff=user.username, status='failed').count()
        running = ScheduledTask.query.filter_by(careoff=user.username, status='running').count()

        stats.append({
            'careoff': user.username,
            'total_tasks': total,
            'failed_tasks': failed,
            'running_tasks': running,
            'wallet_balance': user.walletamount,
            'tgtoken': getattr(user, 'tgtoken', ''),
            'chatid': getattr(user, 'chatid', '')
        })

    tasks = ScheduledTask.query.all()
    user_tasks = {}
    for task in tasks:
        if task.status == 'running':
            user_tasks.setdefault(task.careoff, []).append(task)

    return render_template('superadmin_user_stats.html', user_tasks=user_tasks, stats=stats)


@app.route('/superadmin/add_user', methods=['POST'])
@superadmin_required
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    tgtoken = request.form.get('tgtoken')
    chatid=request.form.get('chatid')
    wallet_balance = float(request.form.get('wallet_balance'))

    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        flash("User already exists", 'danger')
        return redirect(url_for('user_stats'))

    # Hash password before storing
    

    # Create a new user
    new_user = User(username=username, password=password)
    new_user.walletamount = wallet_balance
    new_user.tgtoken=tgtoken
    new_user.chatid=chatid
    db.session.add(new_user)
    db.session.commit()

    flash(f"New user {username} added successfully", 'success')
    return redirect(url_for('user_stats'))


@app.route('/superadmin/update_wallet/<careoff>', methods=['POST'])
@superadmin_required
def update_wallet(careoff):
    new_balance = request.form.get('new_balance')
    new_tgtoken = request.form.get('new_tgtoken')
    new_chatid=request.form.get('new_chatid')
    # Validate new_balance
    try:
        new_balance = float(new_balance)
    except (ValueError, TypeError):
        flash(f"Invalid wallet balance for {careoff}.", "danger")
        return redirect(url_for('user_stats'))

    user = User.query.filter_by(username=careoff).first()
    if user:
        user.walletamount = new_balance
        user.tgtoken = new_tgtoken.strip() if new_tgtoken else None
        user.chatid=new_chatid
        try:
            db.session.commit()
            flash(f"Updated wallet balance and tgToken for {careoff}.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Failed to update data for {careoff}: {e}", "danger")
    else:
        flash(f"User {careoff} not found.", "danger")

    return redirect(url_for('user_stats'))

@app.route('/check_slot', methods=['POST'])
def check_slot():
    try:
        input_data = request.get_json()
        date_str = input_data.get("date")  # Expecting format 'YYYY-MM-DD'
        today_plus_one = datetime.strptime(date_str, "%Y-%m-%d")
        print(today_plus_one)
        s = requests.Session()

        # Navigate the slot pages
        s.get("https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?id=sardlenq",
            headers={"Referer": "https://sarathi.parivahan.gov.in/sarathiservice/stateSelectBean.do", "Connection": "close"})

        s.post("https://sarathi.parivahan.gov.in:443/slots/stateBean.do",
            headers={"Content-Type": "application/x-www-form-urlencoded", "Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.dO", "Connection": "close"},
            data={"stCode": "KL", "stName": "Kerala", "rtoCode": "KL14", "rtoName": "0"})

        s.get("https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&opernType=loadCOVs&trackCode=0",
            headers={"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"})

        s.get("https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=checkSlotTimes",
            headers={"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"})

        req = s.get("https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=loadDLQuotaDet&trackCode=0&trkrto=0&radioType=RTO",
                headers={"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"})

        # Parse table
        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.find('table', class_='table-mod1')
        df = pd.read_html(str(table).upper())[0]
        df.columns = df.iloc[0]
        df = df.tail(-1)
        from datetime import date, timedelta
        todaysdate = datetime.today()
        difference =  today_plus_one -todaysdate
        print(int(difference.days))
        # Get last date
        last_slot_date_str = df['DATE'].iloc[-1]
        last_slot_date = datetime.strptime(last_slot_date_str, "%d-%m-%Y")
        slot_plus_one = last_slot_date + timedelta(days=int(difference.days))

        match = slot_plus_one.date() == today_plus_one.date()
        days_diff = (today_plus_one - slot_plus_one).days
        print(days_diff)
        slot_plus_formated = slot_plus_one.strftime('%Y-%m-%d')
        year = slot_plus_one.year
        print(slot_plus_one)
        # Check for holidays
        holiday_url = f"https://sarathi.parivahan.gov.in/slots/fetchholidayList.do?year={year}&servtype=DL&stcode=KL&rtoCode=KL14"
        holiday_resp = s.post(holiday_url, headers={"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"})

        holiday_data =holiday_resp.json()
# Example slot_plus_one date
 # Format: YYYY-MM-DD
        try:
            # Parse the string response into a Python object
            holiday_data = json.loads(holiday_data)
            #print("Holiday Data:", holiday_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        date_list = [entry['date'] for entry in holiday_data]
        if slot_plus_formated in date_list:
            holiday = True
        else:
            holiday = slot_plus_one.weekday() == 6  # Sunday

        return jsonify({
            "last_slot_date": last_slot_date_str,
            "predicted_date": slot_plus_one.strftime("%d/%m/%Y"),
            "booking_date": today_plus_one.strftime("%d/%m/%Y"),
            "holiday": holiday,
            "days_diff_from_start_date": days_diff
        })

    except Exception as e:
        print("json error",e)
        return jsonify({"error": str(e)}), 500
@app.route('/<careoff>/tgToken', methods=['GET'])
def get_tg_info(careoff):
    user = User.query.filter_by(username=careoff).first()
    if user:
        return jsonify({
            "tgtoken": user.tgtoken or "",
            "chatid": user.chatid or ""
        }), 200
    else:
        return jsonify({"error": f"User '{careoff}' not found"}), 404
PORT = 5000

from flask_login import logout_user, login_required

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))
# Start Ngrok with a custom subdomain
#public_url = ngrok.connect(PORT, "http", url="workable-completely-panther.ngrok-free.app")
#print(f" * Ngrok tunnel \"{public_url}\" -> http://127.0.0.1:{PORT}")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
