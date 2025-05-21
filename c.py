from PIL import Image
import imgkit
import datetime
import pytz
from datetime import datetime
import requests
import shutil
import os
import sys
import requests
import time
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import pandas as pd
import dataframe_image as dfi
import telegram
import tempfile
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import os
from lxml.html import soupparser
from anticaptchaofficial.imagecaptcha import *
from datetime import datetime, timedelta
import sys
from datetime import datetime, timedelta
import pytz

# Read input arguments
APPLNO = sys.argv[1]
DOB = sys.argv[2]
TYPE = sys.argv[3].replace(",", "")
MAXDATE = sys.argv[4].strip()  # Ensure no whitespace
MINDATE = sys.argv[5].strip()

# Timezone aware (IST)
ist = pytz.timezone("Asia/Kolkata")
today = datetime.now(ist)

# Constants
TELEGRAM_TOKEN = '5362509728:AAGws5rqxn4nWeAQ6x2An__YM7AdBGWNCl8'
TELEGRAM_TOKEN_1 = '5865265365:AAHQDbV6qt8hDfWzCsOCMUTwgK2L57SvcUc'
TELEGRAM_CHAT_ID = '631331311'
TELEGRAM_CHAT_ID1 = '846861253'
PHOTO_PATH = 'SLOT_TABLE_NONEMPTY.png'
PDF_PATH = APPLNO+".pdf"

# Debug print
print(f"APPLNO: {APPLNO}, DOB: {DOB}, TYPE: {TYPE}")
print(f"MINDATE: {MINDATE}, MAXDATE: {MAXDATE}")

try:
    min_date = datetime.strptime(MAXDATE, "%d-%m-%Y")
    max_date = datetime.strptime(MINDATE, "%d-%m-%Y")

    if min_date > max_date:
        print("Error: MINDATE is after MAXDATE")
        sys.exit(1)

    delta_days = (max_date - min_date).days
    DATES = [(min_date + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(delta_days + 1)]

    print(f"Generated {len(DATES)} dates:")
    print(DATES)

except ValueError as e:
    print("Date parsing error:", e)
    sys.exit(1)

#DATES = ["10-04-2025","11-04-2025","12-04-2025","13-04-2025","14-04-2025","15-04-2025","16-04-2025","17-04-2025","18-04-2025","19-04-2025","20-04-2025"]
last_successful_captcha = None
last_successful_captcha_timestamp = None
bot = telegram.Bot(token=TELEGRAM_TOKEN_1)
bot1 = telegram.Bot(token=TELEGRAM_TOKEN)

while True:
    try:

        #moi
        '''
        proxy = '127.0.0.1:8080'
        os.environ['http_proxy'] = proxy
        os.environ['HTTP_PROXY'] = proxy
        os.environ['https_proxy'] = proxy
        os.environ['HTTPS_PROXY'] = proxy
        os.environ['REQUESTS_CA_BUNDLE'] = "C:\\Users\\User\\Desktop\\cacert.pem"
        '''
        s = requests.Session()
        e = requests.Session()
       

        
        

# Specify the IST time zone
        ist_timezone = pytz.timezone('Asia/Kolkata')

# Get the current time in IST
        current_time = datetime.now(ist_timezone)
        print("Current time in IST:", current_time.strftime('%Y-%m-%d %H:%M:%S'))


        print(current_time)
        # Extract the current hour and minute
        current_hour = current_time.hour
        current_minute = current_time.minute
        print("start")
        # Check if the current time is between 10 AM and 8 PM
        print(current_hour,current_minute)
        if 9 <= current_hour < 20:
            # Check if the minutes are between 50 and 5 (inclusive)
            if (0 <= current_minute <= 60) or (0 <= current_minute <= 5):

                

                burp0_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?id=sardlenq"
                burp0_headers = {"Referer": "https://sarathi.parivahan.gov.in/sarathiservice/stateSelectBean.do","Connection": "close"}
                burp0_request = e.get(burp0_url, headers=burp0_headers)
                burp0_response = burp0_request.headers
                # print(burp0_response)

                # print(Cookie)

                burp1_url = "https://sarathi.parivahan.gov.in:443/slots/stateBean.do"
                burp1_headers = {"Content-Type": "application/x-www-form-urlencoded","Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.dO", "Connection": "close"}
                burp1_data = {"stCode": "KL", "stName": "Kerala", "rtoCode": "KL14", "rtoName": "0"}
                burp1_req = e.post(burp1_url, headers=burp1_headers, data=burp1_data)
                # print(burp1_req)

                burp2_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&opernType=loadCOVs&trackCode=0"
                burp2_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
                burp2_req = e.get(burp2_url, headers=burp2_headers)
                # print(burp2_req.content)

                burp3_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=checkSlotTimes"
                burp3_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
                burp3_req = e.get(burp3_url, headers=burp3_headers)
                # print(burp3_req.content)

                burp4_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=loadDLQuotaDet&trackCode=0&trkrto=0&radioType=RTO"
                burp4_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
                REQ = e.get(burp4_url, headers=burp4_headers)
                DATA = REQ.content
                # print(DATA)
                soup = BeautifulSoup(REQ.content, 'html.parser')
                table = soup.find('table', class_='table-mod1')
                df = pd.read_html(str(table).upper())[0]
                df.columns = df.iloc[0]
                # print(df)
                df = df.tail(-1)
                #print(df)
                SLOT = df.loc[(df['SLOT1 (08.00-08.10)'] != '0') | (df['SLOT2 (08.11-08.20)'] != '0') | (df['SLOT3 (08.21-08.30)'] != '0') | (df['SLOT4 (08.31-08.40)'] != '0')]
                SLOT.to_csv('SLOT_TABLE.csv', sep='\t')
                print(SLOT)
                if  not SLOT.empty:
                    
                    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
                    ax = plt.gca()
                    ax.axis('tight')
                    ax.axis('off')
                    plt.table(cellText=SLOT.values, colLabels=SLOT.columns, cellLoc='center', loc='center')
                    plt.tight_layout()
                    plt.savefig(PHOTO_PATH, bbox_inches='tight', pad_inches=0.1)
                    plt.close()
                    saved_image = Image.open(PHOTO_PATH)
                    

                    bot = telegram.Bot(token=TELEGRAM_TOKEN)
                    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="SLOT FOUND")
                    #bot.send_message(chat_id=TELEGRAM_CHAT_ID1, text="SLOT FOUND")
                    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))
                    #bot.send_photo(chat_id=TELEGRAM_CHAT_ID1, photo=open(PHOTO_PATH, 'rb'))
                    df3 = pd.read_csv('SLOT_TABLE.csv', sep='\t')
                    df3 = df3.iloc[:, 1:]
                    df3.set_index('DATE', inplace=True)
                    for rowIndex, row in df3.iterrows():
                        for columnIndex, value in row.items():
                            try:
                                ispassed = 0
                                if str(value).isdigit() :
                                    # Convert the value to an integer
                                    int_value = int(value)
                                    # Check if the integer value is greater than 0
                                    if int_value > 0:

                                        
                                        TIMESLOT = columnIndex[7:18]
                                        if rowIndex in DATES:
                                            #print(f"Row: {rowIndex} Column: {columnIndex}")

                                            print(rowIndex,TIMESLOT)
                                            
                                            if last_successful_captcha is not None and \
                                                    (datetime.now(
                                                        ist_timezone) - last_successful_captcha_timestamp).total_seconds() < 1200:
                                                captchaa = last_successful_captcha
                                                print("use old")
                                            else:


                                                while ispassed == 0:
                                                    rewww01_url = "https://sarathi.parivahan.gov.in/slots/jsp/common/captchaimage.jsp"
                                                    rewww01_headers = {
                                                        "Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do",
                                                        "Connection": "close"}
                                                    burp_req = s.get(rewww01_url, headers=rewww01_headers, stream=True)
                                                    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_img:
                                                        temp_img_path = temp_img.name

                                                        # Save the downloaded image to the temporary file
                                                        with open(temp_img_path, 'wb') as img_file:
                                                            shutil.copyfileobj(burp_req.raw, img_file)
                                                            del burp_req

                                                    image_path = temp_img_path
                                                    '''
                                                    reader = easyocr.Reader(['en'])
                                                    result = reader.readtext(image_path)
                                                    captchaa = ' '.join([res[1] for res in result])
                                                    '''

                                                    solver = imagecaptcha()
                                                    solver.set_verbose(1)
                                                    solver.set_key("977a77e4f59ad05bbdd91b80c9bccc89")

                                                    # Specify softId to earn 10% commission with your app.
                                                    # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
                                                    solver.set_soft_id(0)
                                                    solver.set_case("true")
                                                    captchaa = solver.solve_and_return_solution(image_path)
                                                    if captchaa != 0:
                                                        print("captcha text " + captchaa)
                                                    else:
                                                        print("task finished with error " + solver.error_code)
                                                    # captchaa = input("captcha : ")
                                                    print(captchaa)
                                                    rewww0_url = "https://sarathi.parivahan.gov.in:443/slots/dlslotbook.do"
                                                    rewww0_headers = {"Upgrade-Insecure-Requests": "1",
                                                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                                                                      "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/sarathiHomePublic.do",
                                                                      "Connection": "close"}
                                                    s.get(rewww0_url, headers=rewww0_headers)
                                                    captcha_url = "https://sarathi.parivahan.gov.in:443/slots/reloadCaptcha.do?captchaId=slotBooking"
                                                    captcha_headers = {"Cache-Control": "max-age=0",
                                                                       "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/stateSelectBean.do",
                                                                       "Connection": "close"}
                                                    #captchareq = s.get(captcha_url, headers=captcha_headers)
                                                    #response_captcha = captchareq.json()
                                                    #captchatext = response_captcha["reloadCap"]
                                                    #print(captchaa)
                                                    rewww02_url = "https://sarathi.parivahan.gov.in:443/slots/dldetsubmit.do"
                                                    rewww02_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                                                       "Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do"}
                                                    rewww02_data = {"subtype": "1", "applno": APPLNO, "llno": '', "dob": DOB,
                                                                    "uName": '', "hexUsrid": '', "captcha": captchaa}
                                                    rewww0_req = s.post(rewww02_url, headers=rewww02_headers, data=rewww02_data)
                                                    source = rewww0_req.content
                                                    Keyword = 'Invalid Captcha. Please Enter Correct Captcha.'.encode()
                                                    Keyword1 = 'Slot Booking is allowed only during 10.00 AM and 20.00 PM for RTO,KASARAGOD as stipulated by the RTO Authority. Please try during the above time period.'.encode()
                                                    Keyword3 = 'Thanks for using Online Driving Licence test slot booking facility.'.encode()
                                                    if Keyword in source:
                                                        print("CAPTCHA ERROR")
                                                    else:
                                                        if Keyword1 in source:
                                                            print("BOOKING NOT OPENED YET")
                                                        else:
                                                            ispassed = 1
                                                            last_successful_captcha = captchaa
                                                            last_successful_captcha_timestamp = datetime.now(ist_timezone)

                                            rewww02_url = "https://sarathi.parivahan.gov.in:443/slots/dldetsubmit.do"
                                            rewww02_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                                               "Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do"}
                                            rewww02_data = {"subtype": "1", "applno": APPLNO, "llno": '', "dob": DOB,
                                                            "uName": '', "hexUsrid": '', "captcha": last_successful_captcha}
                                            rewww0_req = s.post(rewww02_url, headers=rewww02_headers, data=rewww02_data)
                                            purp0_url = "https://sarathi.parivahan.gov.in:443/slots/proceeddlapmnt.do"
                                            purp0_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                                             "Referer": "https://sarathi.parivahan.gov.in/slots/dldetsubmit.do",
                                                             "Connection": "close"}
                                            mcwglmv_procceddata = {"iscov": "3", "__checkbox_iscov": "3", "iscov": "4",
                                                                   "__checkbox_iscov": "4",
                                                                   "covcd": "3,4,", "trkcd": '',
                                                                   "method:proceedBookslot": "  PROCEED TO BOOK  "}
                                            mcwoglmv_procceddata = {"iscov": "2", "__checkbox_iscov": "2", "iscov": "4",
                                                                    "__checkbox_iscov": "4",
                                                                    "covcd": "2,4,", "trkcd": '',
                                                                    "method:proceedBookslot": "  PROCEED TO BOOK  "}
                                            mcwog_procceddata = {"iscov": "2", "__checkbox_iscov": "2", "covcd": "2,",
                                                                 "trkcd": '',
                                                                 "method:proceedBookslot": "  PROCEED TO BOOK  "}
                                            erick_procceddata = {"iscov": "69", "__checkbox_iscov": "69", "covcd": "69,",
                                                                 "trkcd": '',
                                                                 "method:proceedBookslot": "  PROCEED TO BOOK  "}
                                            mcwg_procceddata = purp0_data = {"iscov": "3", "__checkbox_iscov": "3",
                                                                             "covcd": "3,", "trkcd": '',
                                                                             "method:proceedBookslot": "  PROCEED TO BOOK  "}
                                            lmv_procceddata = {"iscov": "4", "__checkbox_iscov": "4", "covcd": "4,",
                                                               "trkcd": '',
                                                               "method:proceedBookslot": "  PROCEED TO BOOK  "}
                                            if TYPE in ("LMVMCWG", "MCWG+LMV", "LMV+MCWG"):
                                                   TYPE = "MCWGLMV"
                                            elif TYPE in ("LMVMCWOG", "MCWOG+LMV", "LMV+MCWOG"):
                                                   TYPE = "MCWOGLMV"

                                            if TYPE == "erick":
                                                proceeddata = erick_procceddata
                                            if TYPE == "MCWGLMV" :
                                                proceeddata = mcwglmv_procceddata

                                            if TYPE == "LMV":
                                                proceeddata = lmv_procceddata

                                            if TYPE == "MCWOGLMV":
                                                proceeddata = mcwoglmv_procceddata

                                            if TYPE == "MCWOG":
                                                proceeddata = mcwog_procceddata

                                            if TYPE == "MCWG":
                                                proceeddata = mcwg_procceddata

                                            purp0_data = proceeddata
                                            reqqqq = s.post(purp0_url, headers=purp0_headers, data=purp0_data,allow_redirects=False)
                                            purp1_url = 'https://sarathi.parivahan.gov.in:443/slots/fetchdlslotinfo.do?date=' + rowIndex
                                            purp1_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/fetchdltnextmnth.do?nextdateval=1654057812699","Connection": "close"}
                                            s.get(purp1_url, headers=purp1_headers, allow_redirects=False)
                                            mcwglmv_bookdata = {"MCWG, LMV": TIMESLOT + ",MCWG, LMV,18",
                                                                "bookslotstr": TIMESLOT + ",MCWG, LMV,18;",
                                                                "save": "  BOOK SLOT  "}
                                            mcwoglmv_bookdata = {"MCWOG, LMV": TIMESLOT + ",MCWOG, LMV,18",
                                                                 "bookslotstr": TIMESLOT + ",MCWOG, LMV,18;",
                                                                 "save": "  BOOK SLOT  "}
                                            mcwog_bookdata = {"MCWOG": TIMESLOT + ",MCWOG,18",
                                                              "bookslotstr": TIMESLOT + ",MCWOG,18;",
                                                              "save": "  BOOK SLOT  "}
                                            mcwg_bookdata = {"MCWG": TIMESLOT + ",MCWG,18",
                                                             "bookslotstr": TIMESLOT + ",MCWG,18;", "save": "  BOOK SLOT  "}
                                            lmv_bookdata = {"LMV": TIMESLOT + ",LMV,18",
                                                            "bookslotstr": TIMESLOT + ",LMV,18;", "save": "  BOOK SLOT  "}
                                            erick_bookdata={"eRIKSH": TIMESLOT + ",eRIKSH,18",
                                                            "bookslotstr": TIMESLOT + ",eRIKSH,18;", "save": "  BOOK SLOT  "}
                                            purp3_url = "https://sarathi.parivahan.gov.in:443/slots/dlsltprev.do"
                                            purp3_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                                             "Referer": "https://sarathi.parivahan.gov.in/slots/fetchdlslotdetinfo.do"}
                                            if TYPE == "erick":
                                                bookdata = erick_bookdata
                                            if TYPE == "MCWGLMV":
                                                bookdata = mcwglmv_bookdata
                                            if TYPE == "LMV":
                                                bookdata = lmv_bookdata
                                            if TYPE == "MCWOGLMV":
                                                bookdata = mcwoglmv_bookdata
                                            if TYPE == "MCWOG":
                                                bookdata = mcwog_bookdata
                                            if TYPE == "MCWG":
                                                bookdata = mcwg_bookdata
                                            purp3_data = bookdata
                                            s.post(purp3_url, headers=purp3_headers, data=purp3_data, allow_redirects=False)
                                            purp5_url = "https://sarathi.parivahan.gov.in:443/slots/insdlSlotdet.do"
                                            purp5_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                                             "Referer": "https://sarathi.parivahan.gov.in/slots/sendSMS.do",
                                                             "Connection": "close"}
                                            print("hi")
                                            FINALREQ = s.post(purp5_url, headers=purp5_headers, allow_redirects=True)
                                            FINAL_CONTENT = FINALREQ.content
                                            # print(FINAL_CONTENT)
                                            status = BeautifulSoup(FINAL_CONTENT, 'html.parser')
                                            if Keyword3 in FINAL_CONTENT:
                                                print("SLOTBOOKED " + APPLNO)
                                                bot1.send_message(chat_id=TELEGRAM_CHAT_ID,text="BOOKED DATE " + rowIndex + " FOR " + APPLNO)
                                                q = requests.Session()
                                                reqpc_url = "https://sarathi.parivahan.gov.in:443/sarathiservice/applViewStatus.do"
                                                reqpc_headers = {
                                                    "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/sarathiHomePublic.do",
                                                    "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                                                s.get(reqpc_url, headers=reqpc_headers)

                                                reqpc2_url = "https://sarathi.parivahan.gov.in:443/sarathiservice/applViewStages.do"
                                                reqpc2_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                                                  "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/applViewStatus.do",
                                                                  "Connection": "close"}
                                                reqpc2_data = {"applNum": APPLNO, "dateOfBirth": DOB, "captreq": "false"}
                                                s.post(reqpc2_url, headers=reqpc2_headers, data=reqpc2_data)

                                                reqpc3_url = 'https://sarathi.parivahan.gov.in:443/sarathiservice/printAck.do?applNum=' + APPLNO + '&dateOfBirth=' + DOB + '&type=dlslotack'
                                                reqpc3_headers = {
                                                    "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/applViewStages.do",
                                                    "Connection": "close"}
                                                s.get(reqpc3_url, headers=reqpc3_headers, allow_redirects=True)
                                                reqpc4_url = "https://sarathi.parivahan.gov.in:443/slots/jsp/slotbook/DLApmntRptPdf.jsp"
                                                reqpc4_headers = {
                                                    "Referer": "https://sarathi.parivahan.gov.in/slots/viewDlSlotBookDet.do",
                                                    "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                                                PDF = s.get(reqpc4_url, headers=reqpc4_headers)
                                                with open(APPLNO + '.pdf', 'wb') as f:
                                                    f.write(PDF.content)
                                                bot1.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PDF_PATH, 'rb'))
                                                exit()
                                            try:
                                                statusmsg = status.find('h3', class_='text-danger')
                                                print(statusmsg.text)
                                                bot.send_message(chat_id=TELEGRAM_CHAT_ID,text=statusmsg.text + " " + APPLNO)
                                            except Exception as f:
                                                try:
                                                    with open(str(APPLNO)+'error.html', 'wb') as file:
                                                     file.write(FINAL_CONTENT)
                                                    import imgkit
                                                    imgkit.from_file(str(APPLNO)+'error.html', str(APPLNO)+'error.jpg')
                                                    bot.send_document(chat_id=TELEGRAM_CHAT_ID, document=open(str(APPLNO)+'error.html', 'rb'))
                                                    print(f)
                                                    continue
                                                except Exception as f:
                                                    print(f)
                                                    continue

                            except Exception as f:
                                try:
                                    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=str(f) + " "+APPLNO)
                                    print(f)
                                    continue
                                except Exception as f:
                                    print(f)
                                    continue
    except Exception as f:
        try:
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=str(f) + " "+APPLNO)
            print(f)
            continue
        except Exception as f:
            print(f)
            continue

