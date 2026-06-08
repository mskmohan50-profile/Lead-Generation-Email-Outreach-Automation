# 📧 Lead Generation & Email Outreach Automation

A Python-based automation tool that finds leads from a CSV contact list and sends personalized cold emails automatically using Gmail SMTP.

---

## 🚀 Project Overview

This project was built as part of the **SDE Intern task for SubSpace / Vocallabs** on Internshala.

The goal was to:
- Find potential contacts (name, company, email, LinkedIn) using **Prospeo**
- Store them in a structured CSV file
- Automate personalized cold email outreach using **Python**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core scripting language |
| Pandas | Read and process CSV contact list |
| smtplib | Send emails via Gmail SMTP |
| Prospeo | Lead generation (LinkedIn + Email finder) |
| Gmail SMTP | Email delivery |

---

## 📁 Project Structure

```
lead-automation/
│
├── send_emails.py        # Main automation script
├── Contact_List.csv      # Lead data (Name, Company, Email, LinkedIn)
└── README.md             # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mskmohan50-profile/Lead-Generation-Email-Outreach-Automation.git
cd Lead-Generation-Email-Outreach-Automation
```

### 2. Install Dependencies
```bash
pip install pandas openpyxl
```

### 3. Setup Gmail App Password
1. Go to [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
4. Generate a new App Password
5. Copy the 16-digit password

### 4. Configure Your Credentials
Open `send_emails.py` and update:
```python
MY_EMAIL    = "your@gmail.com"
MY_PASSWORD = "your16digitapppassword"
```

### 5. Prepare Your Contact List
Make sure `Contact_List.csv` has these columns:
```
Full name | Company name | Email | Email status | Job title | Person LinkedIn URL
```

---

## ▶️ Run the Script

```bash
python send_emails.py
```

### Expected Output:
```
✅ Sent to Sanskriti (Strategy & Operations Manager) at Revolut
✅ Sent to Akanksha (Training and Development Specialist) at Revolut
✅ Sent to Rohit (FinCrime Analyst) at Revolut
...
🎉 All emails sent!
```

---

## 📧 Email Template Used

```
Subject: SDE Intern Application — Mohan Raj G

Hi [First Name],

I am Mohan Raj G, a final year CS student 
at Coimbatore Institute of Technology (2026).

My skills:
→ React.js, Node.js, Python
→ Flask, Django, PostgreSQL
→ Docker, AWS, REST APIs

I would love to explore SDE Intern opportunities 
at [Company Name].

Can we connect?

Thanks,
Mohan Raj G
LinkedIn: linkedin.com/in/mohan-raj-g-6670b7299
GitHub:   github.com/mskmohan50-profile
```

---

## 📊 Results

| Company | Emails Sent |
|---|---|
| Revolut | 25 |
| Deloitte | 21 |
| Zoho | 1 |
| **Total** | **47** |

---

## ⚠️ Important Notes

- Send a maximum of **50 emails per day** to avoid Gmail spam restrictions
- Only emails with **VERIFIED** status are sent
- A **3-second delay** is added between each email to avoid being flagged as spam
- Never commit your real App Password to GitHub

---

## 👤 Author

**Mohan Raj G**
- 🎓 B.E. Computer Science — Coimbatore Institute of Technology (2026)
- 💼 LinkedIn: [linkedin.com/in/mohan-raj-g-6670b7299](https://linkedin.com/in/mohan-raj-g-6670b7299)
- 🐙 GitHub: [github.com/mskmohan50-profile](https://github.com/mskmohan50-profile)

---

## 📄 License

This project is for educational and internship task purposes only.
