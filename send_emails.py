import smtplib
import pandas as pd
import time
from email.mime.text import MIMEText

MY_EMAIL    = "mskmohan50@gmail.com"
MY_PASSWORD = "ljzztlozuznvmbqh"  

df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\Documents\Contact_List.csv")

for index, row in df.iterrows():

    name    = row['Full name']       
    company = row['Company name']    
    email   = row['Email']           
    job     = row['Job title']  
    

    if pd.isna(email):
        print(f" Skipping {name} — no email")
        continue

    if row['Email status'] != 'VERIFIED':
        print(f"  Skipping {name} — email not verified")
        continue

    first_name = name.split()[0]

    # Write message
    message = f"""Hi {first_name},

I am Mohan Raj G, a final year CS student 
at Coimbatore Institute of Technology (2026).

My skills:
→ React.js, Node.js, Python
→ Flask, Django, PostgreSQL
→ Docker, AWS, REST APIs

I would love to explore SDE Intern opportunities 
at {"SubSpace"}.

Can we connect?

Thanks,
Mohan Raj G
LinkedIn: linkedin.com/in/mohan-raj-g-6670b7299
GitHub:   github.com/mskmohan50-profile"""

    msg = MIMEText(message)
    msg['Subject'] = "SDE Intern Application — Mohan Raj G"
    msg['From']    = MY_EMAIL
    msg['To']      = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MY_EMAIL, MY_PASSWORD)
            smtp.send_message(msg)
            print(f" Sent to {first_name} ({job}) at {company}")

    except Exception as e:
        print(f" Failed for {name} — {e}")
    time.sleep(0)

print("\n All emails sent!")