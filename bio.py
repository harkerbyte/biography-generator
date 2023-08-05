import sys
import responses
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ast import If, Try
import time
import requests
import json

print("""""")
Zet = "harkerbyte24"
if 3 < 5:
    x = Zet
if 19 > 3:
    x = Zet
smtp_server = "smtp.outlook.com"
port = 587
send_email = "fakeyoureport@outlook.com"

passw = x

context = ssl.create_default_context()
try:
    server = smtplib.SMTP(smtp_server, port, timeout=60)
    server.starttls(context=context)
    server.login(send_email, passw)
except Exception as e:
    print(e)
answer = True

while answer:
    f = open('terms and policy.txt', 'r')
    x = f.read()
    f.close()
    print(x)

    answer = input("Do you accept the policy of usage\" y - yes, n- no\":")
    if answer == "y":
        your_mail = input("Your mail address:")
        print("""\033[1;34m 
         bangladesh
         jordan
         bulgaria
         republic
         denmark
         austria
         germany
         greece
         australia
         canada
         united-kingdom
         new-zealand
         philippines
         uganda
         united-states
         south-africa
         argentina
         spain
         peru
         venezuela
         Iran
         finland
         belgium
         canada
         france
         hungary
         armenia
         indonesia
         iceland
         italy
         japan
         georgia
         kazakhstan
         south-korea
         latvia
         montenegrin
         nepal
         belgium
         netherlands
         norway
         poland
         brazil
         portugal
         moldova
         russia
         slovakia
         serbia
         sweden
         turkey
         ukraine
         vietnam
         china
         taiwan
         \033[1;32m""")
        print("""

         Available countries for clone 
          """)



        html = """
        <h1>Reaching out</h1></br>
        
        <p>Hello there, i believe you are having a great day😀.</p>
        <p>I noticed you used my software to generate a clone id info just recently</p>
        <p>I believe you are satisfied by the service provided</p>2q1
        
        
        <h2>Subscribe</h2>
        <p>please make sure you follow my github account <a href=https://github.com/harkerbyte> click here</a></p>
        <p>Also check out my repository for more functioning software packages<a href=https://github.com/harkerbyte?tab=repositories> here</a></p>.
        
        <p>Follow us on facebook<a href=https://facebook.com/cyberhacks6> here</a></p>
        <p>You can send me a coffee <a href=https://buymeacoffee/shade234sherif> click here</a></p>


        <h2> support</h2>    <a href=https://www.buymeacoffee.com/shade234sherif><button name="example"><img src="https://cdn.buymeacoffee.com/assets/homepage/onetime-support-new.png"></button></a>

         """
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)
            server.login(send_email, passw)
            message = MIMEMultipart()

            message["Subject"] = "Bio-replika"
            message["To"] = your_mail
            message["From"] = send_email

            first = MIMEText(html, "html")
            message.attach(first)

            server.sendmail(send_email, your_mail, message.as_string())
        except Exception as f:
            print(f)

        import mechanize

        test = mechanize.Browser()
        ourl = 'https://github.com/harkerbyte'
        header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 ' \
                 'Safari/537.36 '
        test.open(ourl)
        Try
        If;
        responses;
        code = 200
        print("Network connection is stable")
        print("")

        place = input("Kindly select an option\"i.e chinese-taiwan\":").lower()
        sex = input("What's your gender:").lower()


        def cloning():
            try:
              serve = 'api.namefake.com'
              response = requests.get(f'https://{serve}/{place}/{sex}/').json()
            except Exception as g:
              print(g)

            clone = {
                "name": response.get("name"),
                "address": response.get("address"),
                "maiden_name": response.get("maiden_name"),
                "birth_date": response.get("birth_data"),
                "latitude": response.get("latitude"),
                "longitude": response.get("longitude"),
                "phone": "premium feature",
                "work phone": response.get("phone_w"),
                "your mail": response.get("email_u"),
                "domain mail": "premium feature",
                "username": response.get("username"),
                "password": response.get("password"),
                "domain": response.get("domain"),
                "plasticcard": response.get("plasticcard"),
                "cardexpir": response.get("cardexpir"),
                "bonus": response.get("bonus"),
                "company name": response.get("company"),
                "favourite colour": response.get("color"),
                "height": response.get("height"),
                "weight": response.get("weight"),
                "blood type": response.get("blood"),
                "eye": response.get("eye"),
                "hair": response.get("hair"),
                "favourite sport": response.get("sport")
            }
            return clone

        print(json.dumps(cloning(), indent=4))

        saver = True
        while saver:
            print("""
            Would you like to save the result in a file""")
            saver = input("\"y - yes , n - no\":")
            if saver == "y":
                file = open('u-fake.txt', 'w')
                file.write(json.dumps(cloning(), indent=4))
                file.close()
                time.sleep(2)
                print("\033[2;34m File saved\033[2;0m")
                break

            elif saver == "n":
                print("Datas from the last session were not recorded")
                break
            elif saver !="":
                print("invalid option*** session discarded")
                break 

        break
    elif answer == "n":
        print("Exit...")
        sys.exit()
    elif answer != "":
        print("User error ⁂")

