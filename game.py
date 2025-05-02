import requests
import shutil
import sys
import datetime
import easyocr
import random
import collections
collections.Callable = collections.abc.Callable
import pytesseract
import requests
import shutil
import sys
import datetime
import easyocr
import random
import collections
collections.Callable = collections.abc.Callable
import pytesseract
from PIL import Image
import requests
import time
from bs4 import BeautifulSoup
import telegram
import os
from datetime import date
from PIL import Image
import tempfile
from anticaptchaofficial.imagecaptcha import *
import requests
from requests.exceptions import ConnectionError, Timeout
import time
'''
proxy = 'http://127.0.0.1:8080'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.environ['REQUESTS_CA_BUNDLE'] = "C:\\Users\\User\\Desktop\\cacert.pem"
'''
TYPE = sys.argv[2]
APPLNO = sys.argv[1]
DOB = sys.argv[3]
SLOTDATE = sys.argv[4]
CAREOFF = sys.argv[5]
PROXYCON = sys.argv[6]
if PROXYCON == "YES":
    SLEEPCON = 2
else:
    SLEEPCON = 1
STARTBEFOREONLY = "TRUE"

from datetime import datetime
print(APPLNO,DOB,TYPE,SLOTDATE,CAREOFF,PROXYCON,STARTBEFOREONLY,SLEEPCON)
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time

STARTBEFOREONLY = "TRUE"

if STARTBEFOREONLY == "TRUE":
    india = ZoneInfo("Asia/Kolkata")
    
    while True:
        now = datetime.now(india)
        target_time = now.replace(hour=8, minute=47, second=0, microsecond=0)

        # If current time is past the target, start
        if now >= target_time:
            print("\n Time reached: Starting the code...\n")
            break
        else:
            remaining = target_time - now
            print(f"\r Code starts at 8:47 AM IST. Time remaining: {str(remaining).split('.')[0]}", end='')
            time.sleep(1)


TIMESLOT = ["08.00-08.10", "08.11-08.20", "08.21-08.30", "08.31-08.40"]
caperror = "Invalid Captcha. Please Enter Correct Captcha".encode()
ispassed=0
failed=0
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
from swiftshadow import QuickProxy


 # Output: https://<ip>:<port>
import requests

# Your API key (consider storing it securely)
API_KEY = "z322kjc94sqjzejq7hlu2n4qbxyw5yhqqcpyo9s0"

# Check if proxy usage is enabled
  # Change this based on your logic

if PROXYCON == "YES":
    response = requests.get(
        "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25",
        headers={"Authorization": f"Token {API_KEY}"}
    )

    if response.status_code == 200:
        data = response.json()

        # Extract proxies
        proxies = [
            f"http://{item['username']}:{item['password']}@{item['proxy_address']}:{item['port']}"
            for item in data.get("results", [])
        ]

        # Select a random proxy
        if proxies:
            proxy = {'https': random.choice(proxies)}
        else:
            print("No proxies available.")
            proxy = {}
    else:
        print(f"Error {response.status_code}: {response.text}")
        proxy = {}
else:
    proxy = {}  # Use an empty dictionary if proxies are disabled

# Print the selected proxy
print("\nSelected Proxy:", proxy) # Use an empty dictionary if proxies are disabled

# Print the proxy being used
print(proxy)
s = requests.Session()


def make_request(url, method='GET', headers=None, data=None):
    retries = 0

    while retries < MAX_RETRIES:
        try:
            if method == 'GET':
                response = s.get(url, headers=headers, data=data,proxies=proxy)
            elif method == 'POST':
                response = s.post(url, headers=headers, data=data,proxies=proxy)
            else:
                raise ValueError("Unsupported HTTP method. Use GET or POST.")

            response.raise_for_status()  # Raise an exception for bad responses (non-2xx status codes)
            return response
        except (ConnectionError, Timeout) as e:
            print(f"Connection error: {e}")
            retries += 1
            if retries < MAX_RETRIES:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    print("Max retries exceeded. Could not complete the request.")
    return None
while failed==0:
    try:
        print("start")
        TELEGRAM_BOT_TOKEN = '5362509728:AAGws5rqxn4nWeAQ6x2An__YM7AdBGWNCl8'
        TELEGRAM_BOT_TOKEN1 = '5682723989:AAFom9BjZJDUIaRcHVhW4xPC7iKO7xb6iiU'
        TELEGRAM_CHAT_ID = '631331311'
        TELEGRAM_CHAT_ID1 = '631331311'
        PHOTO_PATH = 'SLOT_TABLE_NONEMPTY.png'
        today = date.today()
        today = str(today.strftime("%d-%m-%Y"))
        PDF_FOLD = today+'/'+CAREOFF+'/'
        PDF_PATH = today+'/'+CAREOFF+'/'+APPLNO + CAREOFF + '.pdf'
        if not os.path.exists(PDF_FOLD):
           os.makedirs(PDF_FOLD)

        s = requests.Session()
        rewww0_url = "https://sarathi.parivahan.gov.in:443/slots/dlslotbook.do"
        rewww0_headers = {"Upgrade-Insecure-Requests": "1",
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                          "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/sarathiHomePublic.do",
                          "Connection": "close"}
        make_request(rewww0_url, method='GET', headers=rewww0_headers,data=None)
        while ispassed == 0:
            rewww01_url = "https://sarathi.parivahan.gov.in/slots/jsp/common/captchaimage.jsp"
            rewww01_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do",
                               "Connection": "close"}
            burp_req = s.get(rewww01_url, headers=rewww01_headers, stream=True,proxies=proxy)
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
            #captchaa = input("captcha : ")
            print(captchaa)
            rewww02_url = "https://sarathi.parivahan.gov.in:443/slots/dldetsubmit.do"
            rewww02_headers = {"Content-Type": "application/x-www-form-urlencoded",
                               "Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do"}
            rewww02_data = {"subtype": "1", "applno": APPLNO, "llno": '', "dob": DOB,
                            "uName": '', "hexUsrid": '', "captcha": captchaa}
            cov1_req = make_request(rewww02_url, method='POST', headers=rewww02_headers,data=rewww02_data)
            response123 = cov1_req.content

            if caperror in response123:
                print("Captcha error")
                os.remove(temp_img_path)
                continue
            else:
                ispassed = 1
                print("Captcha success")
                os.remove(temp_img_path)
                break
        while True:
            rewww02_url = "https://sarathi.parivahan.gov.in:443/slots/dldetsubmit.do"
            rewww02_headers = {"Content-Type": "application/x-www-form-urlencoded",
                               "Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do"}
            rewww02_data = {"subtype": "1", "applno": APPLNO, "llno": '', "dob": DOB,
                            "uName": '', "hexUsrid": '', "captcha": captchaa}
            rewww0_req = make_request(rewww02_url, method='POST', headers=rewww02_headers,data=rewww02_data)
            source = rewww0_req.content
            Keyword = 'Invalid Captcha. Please Enter Correct Captcha.'.encode()
            Keyword1 = 'Slot Booking is allowed only during 9.00 AMRTO,KASARAGOD as stipulated by the RTO Authority. Please try during the above time period.'.encode()
            Keyword3 = 'Thanks for using Online Driving Licence test slot booking facility.'.encode()
            takenmsg = ' Appointment Already taken for " + APPLNO + " </h3> </div> <!-- c'.encode()
            if Keyword in source:
                print("CAPTCHA ERROR")
                ispassed = 0

                break
            else:
                    if Keyword1 in source:
                        print("BOOKING NOT OPENED YET",random.randint(3, 10000))
                        continue
                    elif takenmsg in source:
                        reqpc3_url = 'https://sarathi.parivahan.gov.in:443/sarathiservice/printAck.do?applNum=' + APPLNO + '&dateOfBirth=' + DOB + '&type=dlslotack'
                        reqpc3_headers = {"Referer": "https://sarathi.parivahan.gov.in/sarathiservice/applViewStages.do",
                                          "Connection": "close"}
                        make_request(reqpc3_url, method='GET', headers=reqpc3_headers,data=None)
                        reqpc4_url = "https://sarathi.parivahan.gov.in:443/slots/jsp/slotbook/DLApmntRptPdf.jsp"
                        reqpc4_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/viewDlSlotBookDet.do",
                                          "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                        PDF = s.get(reqpc4_url, headers=reqpc4_headers,proxies=proxy)
                        with open(PDF_PATH, 'wb') as m:
                                m.write(PDF.content)
                        ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                        ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                        #bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PDF_PATH, 'rb'))
                        exit()

                    else:
                        FIRSTREQ = rewww0_req.content
                        FIRST_STATUS = BeautifulSoup(FIRSTREQ, 'html.parser')
                        if (FIRST_STATUS.find('h3', {'style': 'color: red'})):
                            statusmsg = FIRST_STATUS.find('h3', {'style': 'color: red'})
                            if not (statusmsg.text.isspace()):
                               print(statusmsg.text)
                               continue
                            else:
                             pass

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
                        mcwg_procceddata = purp0_data = {"iscov": "3", "__checkbox_iscov": "3",
                                                         "covcd": "3,", "trkcd": '',
                                                         "method:proceedBookslot": "  PROCEED TO BOOK  "}
                        lmv_procceddata = {"iscov": "4", "__checkbox_iscov": "4", "covcd": "4,",
                                           "trkcd": '',
                                           "method:proceedBookslot": "  PROCEED TO BOOK  "}

                        if TYPE == "MCWG,LMV":
                            proceeddata = mcwglmv_procceddata
                        if TYPE == "LMV,MCWG":
                            proceeddata = mcwglmv_procceddata

                        if TYPE == "LMV":
                            proceeddata = lmv_procceddata

                        if TYPE == "MCWOG,LMV":
                            proceeddata = mcwoglmv_procceddata
                        if TYPE == "LMV,MCWOG":
                            proceeddata = mcwoglmv_procceddata

                        if TYPE == "MCWOG":
                            proceeddata = mcwog_procceddata

                        if TYPE == "MCWG":
                            proceeddata = mcwg_procceddata

                        purp0_data = proceeddata
                        reqqqq = s.post(purp0_url, headers=purp0_headers, data=purp0_data,allow_redirects=False,proxies=proxy)
                        mcwglmv_bookdata = {"MCWG, LMV": random.choice(TIMESLOT) + ",MCWG, LMV,18",
                                            "bookslotstr": random.choice(TIMESLOT) + ",MCWG, LMV,18;",
                                            "save": "  BOOK SLOT  "}
                        mcwoglmv_bookdata = {"MCWOG, LMV": random.choice(TIMESLOT) + ",MCWOG, LMV,18",
                                             "bookslotstr": random.choice(TIMESLOT) + ",MCWOG, LMV,18;",
                                             "save": "  BOOK SLOT  "}
                        mcwog_bookdata = {"MCWOG": random.choice(TIMESLOT) + ",MCWOG,18",
                                          "bookslotstr": random.choice(TIMESLOT) + ",MCWOG,18;",
                                          "save": "  BOOK SLOT  "}
                        mcwg_bookdata = {"MCWG": random.choice(TIMESLOT) + ",MCWG,18",
                                         "bookslotstr": random.choice(TIMESLOT) + ",MCWG,18;", "save": "  BOOK SLOT  "}
                        lmv_bookdata = {"LMV": random.choice(TIMESLOT) + ",LMV,18",
                                        "bookslotstr": random.choice(TIMESLOT) + ",LMV,18;", "save": "  BOOK SLOT  "}
                        purp1_url = 'https://sarathi.parivahan.gov.in:443/slots/fetchdlslotinfo.do?date=' + SLOTDATE
                        purp1_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/fetchdltnextmnth.do?nextdateval=1654057812699","Connection": "close"}
                        s.get(purp1_url, headers=purp1_headers, allow_redirects=False,proxies=proxy)

                        purp3_url = "https://sarathi.parivahan.gov.in:443/slots/dlsltprev.do"
                        purp3_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                         "Referer": "https://sarathi.parivahan.gov.in/slots/fetchdlslotdetinfo.do"}
                        if TYPE == "MCWG,LMV":
                            bookdata = mcwglmv_bookdata
                        if TYPE == "LMV,MCWG":
                            bookdata = mcwglmv_bookdata
                        if TYPE == "LMV":
                            bookdata = lmv_bookdata
                        if TYPE == "MCWOG,LMV":
                            bookdata = mcwoglmv_bookdata
                        if TYPE == "LMV,MCWOG":
                            bookdata = mcwoglmv_bookdata
                        if TYPE == "MCWOG":
                            bookdata = mcwog_bookdata
                        if TYPE == "MCWG":
                            bookdata = mcwg_bookdata
                        purp3_data = bookdata
                        FINAL1_REQ=s.post(purp3_url, headers=purp3_headers, data=purp3_data, allow_redirects=False,proxies=proxy)
                        purp5_url = "https://sarathi.parivahan.gov.in:443/slots/insdlSlotdet.do"
                        purp5_headers = {"Content-Type": "application/x-www-form-urlencoded","Referer": "https://sarathi.parivahan.gov.in/slots/sendSMS.do","Connection": "close"}

                        if (int(SLEEPCON) == 1):
                            SECS = [8, 9, 10, 11, 12, 13, 14, 15]
                        if (int(SLEEPCON) == 2):
                            SECS = [4, 5, 6, 7, 8]
                        if (int(SLEEPCON) == 3):
                            SECS = [0]


                        time.sleep(random.choice(SECS))
                        FINALREQ = s.post(purp5_url, headers=purp5_headers, allow_redirects=True,proxies=proxy)
                        FINAL_CONTENT1 = FINALREQ.content
                        FINAL_CONTENT =FINAL1_REQ.content


                        # #print(FINAL_CONTENT)
                        status = BeautifulSoup(FINAL_CONTENT, 'html.parser')
                        status1=BeautifulSoup(FINAL_CONTENT1, 'html.parser')
                        if Keyword3 in FINAL_CONTENT1:
                            print("SLOTBOOKED " + APPLNO)
                            ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                            ##bot.send_message(chat_id=TELEGRAM_CHAT_ID,text="BOOKED DATE " + SLOTDATE + " FOR " + APPLNO)
                            q = requests.Session()
                            burp0_url = "https://sarathi.parivahan.gov.in:443/sarathiservice/stateSelectBean.do"
                            burp0_headers = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "Origin": "https://sarathi.parivahan.gov.in",
                                "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/stateSelection.do",
                                "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document",
                                "Sec-Fetch-Mode": "navigate",
                                "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers",
                                "Connection": "close"}
                            burp0_data = {"stName": "KL"}
                            q.post(burp0_url, headers=burp0_headers, data=burp0_data)
                            reqpc3_url = 'https://sarathi.parivahan.gov.in:443/sarathiservice/printAck.do?applNum=' + APPLNO + '&dateOfBirth=' + DOB + '&type=dlslotack'
                            reqpc3_headers = {
                                "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/applViewStages.do",
                                "Connection": "close"}
                            q.get(reqpc3_url, headers=reqpc3_headers, allow_redirects=True)
                            reqpc4_url = "https://sarathi.parivahan.gov.in:443/slots/jsp/slotbook/DLApmntRptPdf.jsp"
                            reqpc4_headers = {
                                "Referer": "https://sarathi.parivahan.gov.in/slots/viewDlSlotBookDet.do",
                                "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                            PDF = q.get(reqpc4_url, headers=reqpc4_headers)
                            with open(PDF_PATH, 'wb') as f:
                                f.write(PDF.content)
                            ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                            ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                            ##bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PDF_PATH, 'rb'))
                            exit()
                        try:
                            bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                            bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)

                            if(status.find('h3',class_='text-danger')):
                                statusmsg=status.find('h3',class_='text-danger')
                                print(statusmsg.text)
                            if(status1.find('h3',class_='text-danger')):
                                statusmsg = status1.find('h3', class_='text-danger')
                                print(statusmsg.text)


                                ##bot1.send_message(chat_id=TELEGRAM_CHAT_ID1, text=statusmsg.text+" "+APPLNO+"\n"+CAREOFF)
                        except Exception as e:
                            import traceback

                            traceback.print_exc()
                            try:
                                    print(e)
                                    ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                                    ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                                    ##bot1.send_message(chat_id=TELEGRAM_CHAT_ID1, text=statusmsg.text+" "+APPLNO+"\n"+CAREOFF)
                            except Exception as e:
                                        print(e)
                                        pass
    except Exception as e:
        import traceback

        traceback.print_exc()
        try:
                print(e)

                ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                ##bot1.send_message(chat_id=TELEGRAM_CHAT_ID1, text=statusmsg.text+" "+APPLNO+"\n"+CAREOFF)
                continue
        except Exception as e:
                    print(e)
                    pass
        #time.sleep(5)
from PIL import Image
import requests
import time
from bs4 import BeautifulSoup
import telegram
import os
from datetime import date
from PIL import Image
import tempfile
from anticaptchaofficial.imagecaptcha import *
import requests
from requests.exceptions import ConnectionError, Timeout
import time

TYPE = sys.argv[1]
APPLNO = sys.argv[2]
DOB = sys.argv[3]
SLOTDATE = sys.argv[4]
CAREOFF = sys.argv[5]
SLEEPCON = sys.argv[6]
TIMESLOT = ["08.00-08.10", "08.11-08.20", "08.21-08.30", "08.31-08.40"]
caperror = "Invalid Captcha. Please Enter Correct Captcha".encode()
ispassed=0
failed=0
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
s = requests.Session()


def make_request(url, method='GET', headers=None, data=None):
    retries = 0

    while retries < MAX_RETRIES:
        try:
            if method == 'GET':
                response = s.get(url, headers=headers, data=data)
            elif method == 'POST':
                response = s.post(url, headers=headers, data=data)
            else:
                raise ValueError("Unsupported HTTP method. Use GET or POST.")

            response.raise_for_status()  # Raise an exception for bad responses (non-2xx status codes)
            return response
        except (ConnectionError, Timeout) as e:
            print(f"Connection error: {e}")
            retries += 1
            if retries < MAX_RETRIES:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    print("Max retries exceeded. Could not complete the request.")
    return None
while failed==0:
    try:
        print("start")
        TELEGRAM_BOT_TOKEN = '5362509728:AAGws5rqxn4nWeAQ6x2An__YM7AdBGWNCl8'
        TELEGRAM_BOT_TOKEN1 = '5682723989:AAFom9BjZJDUIaRcHVhW4xPC7iKO7xb6iiU'
        TELEGRAM_CHAT_ID = '631331311'
        TELEGRAM_CHAT_ID1 = '631331311'
        PHOTO_PATH = 'SLOT_TABLE_NONEMPTY.png'
        today = date.today()
        today = str(today.strftime("%d-%m-%Y"))
        
        if not os.path.exists(PDF_FOLD):
           os.makedirs(PDF_FOLD)

        s = requests.Session()
        rewww0_url = "https://sarathi.parivahan.gov.in:443/slots/dlslotbook.do"
        rewww0_headers = {"Upgrade-Insecure-Requests": "1",
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                          "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/sarathiHomePublic.do",
                          "Connection": "close"}
        make_request(rewww0_url, method='GET', headers=rewww0_headers,data=None)
        while ispassed == 0:
            rewww01_url = "https://sarathi.parivahan.gov.in/slots/jsp/common/captchaimage.jsp"
            rewww01_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do",
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
            #captchaa = input("captcha : ")
            print(captchaa)
            rewww02_url = "https://sarathi.parivahan.gov.in:443/slots/dldetsubmit.do"
            rewww02_headers = {"Content-Type": "application/x-www-form-urlencoded",
                               "Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do"}
            rewww02_data = {"subtype": "1", "applno": APPLNO, "llno": '', "dob": DOB,
                            "uName": '', "hexUsrid": '', "captcha": captchaa}
            cov1_req = make_request(rewww02_url, method='POST', headers=rewww02_headers,data=rewww02_data)
            response123 = cov1_req.content

            if caperror in response123:
                print("Captcha error")
                os.remove(temp_img_path)
                continue
            else:
                ispassed = 1
                print("Captcha success")
                os.remove(temp_img_path)
                break
        while True:
            rewww02_url = "https://sarathi.parivahan.gov.in:443/slots/dldetsubmit.do"
            rewww02_headers = {"Content-Type": "application/x-www-form-urlencoded",
                               "Referer": "https://sarathi.parivahan.gov.in/slots/dlslotbook.do"}
            rewww02_data = {"subtype": "1", "applno": APPLNO, "llno": '', "dob": DOB,
                            "uName": '', "hexUsrid": '', "captcha": captchaa}
            rewww0_req = make_request(rewww02_url, method='POST', headers=rewww02_headers,data=rewww02_data)
            source = rewww0_req.content
            Keyword = 'Invalid Captcha. Please Enter Correct Captcha.'.encode()
            Keyword1 = '                        Slot Booking is allowed only during 9.00 AM and 17.00 PM for RTO,KASARAGOD as stipulated by the RTO Authority. Please try during the above time period.'.encode()
            Keyword3 = 'Thanks for using Online Driving Licence test slot booking facility.'.encode()
            takenmsg = ('Appointment Already taken for ' + str(APPLNO)).encode()

            if Keyword in source:
                print("CAPTCHA ERROR")
                ispassed = 0

                break
            else:
                    if Keyword1 in source:
                        print("BOOKING NOT OPENED YET",random.randint(3, 10000))
                        continue
                    elif takenmsg in source:
                        reqpc3_url = 'https://sarathi.parivahan.gov.in:443/sarathiservice/printAck.do?applNum=' + APPLNO + '&dateOfBirth=' + DOB + '&type=dlslotack'
                        reqpc3_headers = {"Referer": "https://sarathi.parivahan.gov.in/sarathiservice/applViewStages.do",
                                          "Connection": "close"}
                        make_request(reqpc3_url, method='GET', headers=reqpc3_headers,data=None)
                        reqpc4_url = "https://sarathi.parivahan.gov.in:443/slots/jsp/slotbook/DLApmntRptPdf.jsp"
                        reqpc4_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/viewDlSlotBookDet.do",
                                          "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                        PDF = s.get(reqpc4_url, headers=reqpc4_headers)
                        with open(PDF_PATH, 'wb') as m:
                                m.write(PDF.content)
                        ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                        ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                        #bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PDF_PATH, 'rb'))
                        exit()

                    else:
                        FIRSTREQ = rewww0_req.content
                        FIRST_STATUS = BeautifulSoup(FIRSTREQ, 'html.parser')
                        if (FIRST_STATUS.find('h3', {'style': 'color: red'})):
                            statusmsg = FIRST_STATUS.find('h3', {'style': 'color: red'})
                            if not (statusmsg.text.isspace()):
                               print(statusmsg.text)
                               continue
                            else:
                             pass

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
                        mcwg_procceddata = purp0_data = {"iscov": "3", "__checkbox_iscov": "3",
                                                         "covcd": "3,", "trkcd": '',
                                                         "method:proceedBookslot": "  PROCEED TO BOOK  "}
                        lmv_procceddata = {"iscov": "4", "__checkbox_iscov": "4", "covcd": "4,",
                                           "trkcd": '',
                                           "method:proceedBookslot": "  PROCEED TO BOOK  "}

                        if TYPE == "MCWG,LMV":
                            proceeddata = mcwglmv_procceddata

                        if TYPE == "LMV":
                            proceeddata = lmv_procceddata

                        if TYPE == "MCWOG,LMV":
                            proceeddata = mcwoglmv_procceddata

                        if TYPE == "MCWOG":
                            proceeddata = mcwog_procceddata

                        if TYPE == "MCWG":
                            proceeddata = mcwg_procceddata

                        purp0_data = proceeddata
                        reqqqq = s.post(purp0_url, headers=purp0_headers, data=purp0_data,allow_redirects=False)
                        mcwglmv_bookdata = {"MCWG, LMV": random.choice(TIMESLOT) + ",MCWG, LMV,18",
                                            "bookslotstr": random.choice(TIMESLOT) + ",MCWG, LMV,18;",
                                            "save": "  BOOK SLOT  "}
                        mcwoglmv_bookdata = {"MCWOG, LMV": random.choice(TIMESLOT) + ",MCWOG, LMV,18",
                                             "bookslotstr": random.choice(TIMESLOT) + ",MCWOG, LMV,18;",
                                             "save": "  BOOK SLOT  "}
                        mcwog_bookdata = {"MCWOG": random.choice(TIMESLOT) + ",MCWOG,18",
                                          "bookslotstr": random.choice(TIMESLOT) + ",MCWOG,18;",
                                          "save": "  BOOK SLOT  "}
                        mcwg_bookdata = {"MCWG": random.choice(TIMESLOT) + ",MCWG,18",
                                         "bookslotstr": random.choice(TIMESLOT) + ",MCWG,18;", "save": "  BOOK SLOT  "}
                        lmv_bookdata = {"LMV": random.choice(TIMESLOT) + ",LMV,18",
                                        "bookslotstr": random.choice(TIMESLOT) + ",LMV,18;", "save": "  BOOK SLOT  "}
                        purp1_url = 'https://sarathi.parivahan.gov.in:443/slots/fetchdlslotinfo.do?date=' + SLOTDATE
                        purp1_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/fetchdltnextmnth.do?nextdateval=1654057812699","Connection": "close"}
                        s.get(purp1_url, headers=purp1_headers, allow_redirects=False)

                        purp3_url = "https://sarathi.parivahan.gov.in:443/slots/dlsltprev.do"
                        purp3_headers = {"Content-Type": "application/x-www-form-urlencoded",
                                         "Referer": "https://sarathi.parivahan.gov.in/slots/fetchdlslotdetinfo.do"}
                        if TYPE == "MCWG,LMV":
                            bookdata = mcwglmv_bookdata
                        if TYPE == "LMV":
                            bookdata = lmv_bookdata
                        if TYPE == "MCWOG,LMV":
                            bookdata = mcwoglmv_bookdata
                        if TYPE == "MCWOG":
                            bookdata = mcwog_bookdata
                        if TYPE == "MCWG":
                            bookdata = mcwg_bookdata
                        purp3_data = bookdata
                        FINAL1_REQ=s.post(purp3_url, headers=purp3_headers, data=purp3_data, allow_redirects=False)
                        purp5_url = "https://sarathi.parivahan.gov.in:443/slots/insdlSlotdet.do"
                        purp5_headers = {"Content-Type": "application/x-www-form-urlencoded","Referer": "https://sarathi.parivahan.gov.in/slots/sendSMS.do","Connection": "close"}

                        if (int(SLEEPCON) == 1):
                            SECS = [8, 9, 10, 11, 12, 13, 14, 15]
                        if (int(SLEEPCON) == 2):
                            SECS = [4, 5, 6, 7, 8]
                        if (int(SLEEPCON) == 3):
                            SECS = [0]


                        time.sleep(random.choice(SECS))
                        FINALREQ = s.post(purp5_url, headers=purp5_headers, allow_redirects=True)
                        FINAL_CONTENT1 = FINALREQ.content
                        FINAL_CONTENT =FINAL1_REQ.content


                        # #print(FINAL_CONTENT)
                        status = BeautifulSoup(FINAL_CONTENT, 'html.parser')
                        status1=BeautifulSoup(FINAL_CONTENT1, 'html.parser')
                        if Keyword3 in FINAL_CONTENT1:
                            print("SLOTBOOKED " + APPLNO)
                            ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                            ##bot.send_message(chat_id=TELEGRAM_CHAT_ID,text="BOOKED DATE " + SLOTDATE + " FOR " + APPLNO)
                            q = requests.Session()
                            burp0_url = "https://sarathi.parivahan.gov.in:443/sarathiservice/stateSelectBean.do"
                            burp0_headers = {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "Origin": "https://sarathi.parivahan.gov.in",
                                "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/stateSelection.do",
                                "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document",
                                "Sec-Fetch-Mode": "navigate",
                                "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers",
                                "Connection": "close"}
                            burp0_data = {"stName": "KL"}
                            q.post(burp0_url, headers=burp0_headers, data=burp0_data)
                            reqpc3_url = 'https://sarathi.parivahan.gov.in:443/sarathiservice/printAck.do?applNum=' + APPLNO + '&dateOfBirth=' + DOB + '&type=dlslotack'
                            reqpc3_headers = {
                                "Referer": "https://sarathi.parivahan.gov.in/sarathiservice/applViewStages.do",
                                "Connection": "close"}
                            q.get(reqpc3_url, headers=reqpc3_headers, allow_redirects=True)
                            reqpc4_url = "https://sarathi.parivahan.gov.in:443/slots/jsp/slotbook/DLApmntRptPdf.jsp"
                            reqpc4_headers = {
                                "Referer": "https://sarathi.parivahan.gov.in/slots/viewDlSlotBookDet.do",
                                "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                            PDF = q.get(reqpc4_url, headers=reqpc4_headers)
                            with open(PDF_PATH, 'wb') as f:
                                f.write(PDF.content)
                            ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                            ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                            ##bot.sendDocument(chat_id=TELEGRAM_CHAT_ID, document=open(PDF_PATH, 'rb'))
                            exit()
                        try:
                            bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                            bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)

                            if(status.find('h3',class_='text-danger')):
                                statusmsg=status.find('h3',class_='text-danger')
                                print(statusmsg.text)
                            if(status1.find('h3',class_='text-danger')):
                                statusmsg = status1.find('h3', class_='text-danger')
                                print(statusmsg.text)


                                ##bot1.send_message(chat_id=TELEGRAM_CHAT_ID1, text=statusmsg.text+" "+APPLNO+"\n"+CAREOFF)
                        except Exception as e:
                            import traceback

                            traceback.print_exc()
                            try:
                                    print(e)
                                    ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                                    ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                                    ##bot1.send_message(chat_id=TELEGRAM_CHAT_ID1, text=statusmsg.text+" "+APPLNO+"\n"+CAREOFF)
                            except Exception as e:
                                        print(e)
                                        pass
    except Exception as e:
        import traceback

        traceback.print_exc()
        try:
                print(e)

                ##bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
                ##bot1 = telegram.Bot(token=TELEGRAM_BOT_TOKEN1)
                ##bot1.send_message(chat_id=TELEGRAM_CHAT_ID1, text=statusmsg.text+" "+APPLNO+"\n"+CAREOFF)
                continue
        except Exception as e:
                    print(e)
                    pass
        #time.sleep(5)
