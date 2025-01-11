from flask import Flask, render_template, request, jsonify, redirect, url_for, session as d
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import subprocess
from flask_login import login_required, current_user
import threading
import os
import json
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
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)
scheduler = BackgroundScheduler()
scheduler.start()

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
class SchedulingSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scheduling_time = db.Column(db.Time, nullable=False, default="08:55:00")

    
with app.app_context():
    db.create_all()

global active_processes
active_processes = {}
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
        if username == 'admin' and password == 'password':
            d['logged_in'] = True
            d['username'] = "admin"
            return redirect(url_for('dashboard'))
        else:
            return "Invalid login credentials", 403
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in d :
        return redirect(url_for('login'))
    username = d['username']
    return render_template('dashboard.html', username=username)

@app.route('/fetch_task_data', methods=['POST'])
def fetch_task_data():
                        caperror = "Enter Valid Captcha.".encode()
                        data = request.json
                        response_data = []
                        for task in data:
                            ispassed=0
                            applicationid = task['applno']
                            dobfinal = task['dob']
                            while ispassed==0:
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
                                error_message = soup.select_one('.errorMessage li span').text.strip()
                                print('Error Message Cov:', e,error_message)
                                
                                

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
                                        



                                df = pd.read_html(str(table).upper())[0]
                                vauleofcov = df.at[0, 'CLASS OF VEHICLES']
                                try:
                                 table = soup.find_all('table', class_="table table-bordered table-hover marginStyle")[0]
                                except Exception as e:
                                    applicationid=oldapplicationid
                                    response_data.append({"applno": applicationid, "name": name, "cov": vauleofcov})
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
                                pass
                            applicationid=oldapplicationid
                            response_data.append({"applno": applicationid, "name": name, "cov": vauleofcov})
                        return jsonify(response_data)
                            



# Assuming `scheduler` has been initialized as an instance of BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/schedule', methods=['POST'])
def schedule_task():
    data = request.json
    tasks = data.get('tasks')
    settings = SchedulingSettings.query.first()
    
    scheduling_time = settings.scheduling_time
    if not tasks:
        return jsonify({'error': 'No tasks provided'}), 400
    task_time= pytz.timezone("Asia/Kolkata").localize(datetime.strptime(datetime.now().strftime("%Y-%m-%d") + " " + scheduling_time.strftime("%H:%M:%S"), "%Y-%m-%d %H:%M:%S")).astimezone(pytz.utc)

    for task in tasks:
        new_task = ScheduledTask(
    applications=task['applno'],
    dob = datetime.strptime(task['dob'], "%Y-%m-%d").strftime("%d/%m/%Y"),
    
    cov=str(task['cov']).replace(" ", ""),
    scheduled_date=datetime.now().strftime("%Y-%m-%d"),
    status="Pending",
    slotdate=datetime.strptime(task['slotdate'], "%Y-%m-%d").strftime("%d-%m-%Y")
)
        db.session.add(new_task)
        db.session.commit()
        scheduler.add_job(run_game_script, 'date', run_date=task_time, args=[new_task.id])

        # Calculate when to schedule the task (i.e., at the slotdate and time)
         # Adjust format as per input

        # Schedule the game.py script to run at the specified time
        

    return jsonify({'message': 'Tasks scheduled successfully'}), 201



# Ensure the 'logs' directory exists
os.makedirs('logs', exist_ok=True)

os.makedirs('logs', exist_ok=True)


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

def run_game_script(task_id):
    # Generate a unique log file name based on task_id and timestamp with microseconds
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S%f')
    log_file = f'logs/{task_id}_{timestamp}.log'

    # Create a logger for this task with the unique log file
    logger = logging.getLogger(f'task_{task_id}')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    with app.app_context():
        task = ScheduledTask.query.get(task_id)
        if task:
            task.status = "Running"
            task.log_file = log_file
            task.output = ""
            logger.info(f"Starting task ID {task_id} for application {task.applications}")

            command = ["python", "-u", "game.py", task.cov, task.applications, task.dob, task.slotdate, "ABB", "1"]
            try:
                print("hello")
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                active_processes[task_id] = process
                retry_commit(db.session)  # Retry commit logic here
                
                # Capture output line-by-line
                for line in iter(process.stdout.readline, ''):
                    logger.info(line.strip())
                    task.output += line.strip() + '\n'
                
                # Wait for the process to complete and get the return code
                process.wait()
                if process.returncode == 0:
                    task.status = "Completed"
                else:
                    task.status = "Failed"
                    for error_line in iter(process.stderr.readline, ''):
                        logger.error(error_line.strip())
                        task.output += error_line.strip() + '\n'

            except FileNotFoundError:
                task.status = "Failed"
                task.output = "game.py not found"
                logger.error("game.py not found")

            finally:
                task.log_file = log_file
                retry_commit(db.session)  # Retry commit in the finally block

            logger.info(f"Task ID {task_id} status updated to {task.status}")

            # Remove the logger handlers to avoid duplication
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
@app.route('/live_status/<int:task_id>')
def live_status(task_id):
    task = ScheduledTask.query.get(task_id)
    if not task or not task.log_file:
        return jsonify({'error': 'Task or log file not found'}), 404
     
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
@app.route('/view_tasks')
def view_tasks():
    # Query all scheduled tasks from the database
    tasks = ScheduledTask.query.all()
    
    # Return tasks in a simple HTML table view
    return render_template('view_tasks.html', tasks=tasks)
@app.route('/kill_task/<int:task_id>', methods=['GET'])  # Changed to POST for better semantics
def kill_task(task_id):
    
    process = active_processes.get(task_id)

    if not process:
        return jsonify({'error': f'No running process found for task ID {task_id}'}), 404

    try:
        # Terminate the process gracefully
        process.terminate()
        process.wait(timeout=5)  # Allow time for graceful termination
    except subprocess.TimeoutExpired:
        # Force kill if it doesn't terminate gracefully
        process.kill()
        return jsonify({'message': f'Task ID {task_id} forcefully terminated'}), 503  # Use 503 for service unavailable
    except Exception as e:
        return jsonify({'error': f'Failed to terminate task ID {task_id}: {str(e)}'}), 500
    finally:
        # Remove the task from the active processes dictionary
        active_processes.pop(task_id, None)

    return jsonify({'message': f'Task ID {task_id} terminated successfully'}), 200


@app.route('/pdf/<applno>')
def send_pdf(applno):
    # Directory where PDF files are stored
    pdf_directory = os.path.join(app.root_path, 'pdfs')
    
    # File name
    pdf_file = f"{applno}.pdf"
    
    # Check if the file exists
    if not os.path.isfile(os.path.join(pdf_directory, pdf_file)):
        abort(404, description=f"PDF file for {applno} not found.")
    
    # Serve the file
    return send_from_directory(pdf_directory, pdf_file, as_attachment=True)
@app.route('/superadmin/dashboard', methods=['GET', 'POST'])  # Assuming superadmin has a login system
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

@app.route('/upload', methods=['POST'])
def upload_images():
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

@app.route('/imgtoappl', methods=['POST'])
def img_to_appl():
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
                        url = 'https://lens.google.com/v3/upload?re=df&stcs=1696050670318&vpw=1707&vph=833&ep=subb'

                        # Define the payload with image data
                        files = {
                            'encoded_image': (path, image_data, 'image/jpeg')
                        }

                        # Send the POST request
                        response = requests.post(url, files=files, timeout=8)

                        r3 = str(response.content)
                        r4 = r3.replace('"', '')
                        phoneNumRegex2 = re.compile(r'KL\s*\d+\s*/\s*\d+\s*/\s*\d+')

                        mo = phoneNumRegex2.search(str(r4))
                        application_no_pattern = r"Application No : (\d+)"
                        dob_pattern = r"(\d{2}-\d{2}-\d{4})"
                        matches = re.search(application_no_pattern, r4)
                        matchess = re.findall(dob_pattern, r4)
                        success = 0
                        valid_dobs = [dob for dob in matchess if int(dob[-4:]) <= 2019]

                        if mo:
                            learner = str(mo.group())
                            learner = learner.replace(" ", "")
                            learner = learner[0:4] + " " + learner[4:17]
                            print(learner)

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
                            print("error")
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
@app.route('/webhook', methods=['GET'])
def webhook():
    data = request.json
    if data and 'ref' in data:  # Ensure it's a push event
        os.system('cd /home/test/DLWEB && git pull origin main ')
    return 'Updated', 200
if __name__ == '__main__':
    app.run(debug=True)
