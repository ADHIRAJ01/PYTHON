# REFFERAL VIDEO LINK ---- https://www.youtube.com/watch?v=s8XjEuplx_U

#       -------------------------          TCHING DETAILS FROM A WEBPAGE       ------------------------

# # http requests
# from urllib import response
# import requests   


# # web scrapping
# from bs4 import BeautifulSoup   





# #email content placeholder
content = ''

# # extract Hacker News Stories 
# # HERE THE DETAILS WILL BE FETCHED AFTER FETCHING AS CONTENT TO SEND AS AN EMAIL 
# def extract_news(url):
#     # print('Extracting Hacker News ...... ')
#     cnt = '' 
#     cnt +=('<b>TOP STORIES</b>\n'+'<br>'+'-'*50+'<br>')
#     response = requests.get(url)
#     # print(" response is = ", response)
#     content = response.content   

#     # print( " content = \n",content )      // WORKING GIVING CONTENTS OF THAT WEBPAGE 
#     # print("emailid is = ",emailid )
    
#     soup = BeautifulSoup(content , 'html.parser') # PARSING CONTENT THROUGH HTML PARSER
    
#     for i , tag in enumerate(soup.find_all(attrs={'class':'home-title'})):      # mapping every thing i for index and tag for detail , attrs for id to be fetched from webpage 
#         cnt += tag.text+'<br>'
#     return cnt
    


# # print("time now is =", now)
# url='https://thehackernews.com/' 
# newsextracted = extract_news(url)
# # print("newsextracted= ", newsextracted ) 
# # SUCCESSFULLY FETCHED THE DETAILS FROM THE WEBPAGE USING URL  


#------------------------------------------------------------------------------------------------------------------

#                       ---------------------  EMAIL AUTHENTICATION  --------------------------- 

# # send email
import smtplib    

# # email body 
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText 

# # date time manipulation
import datetime  
now = datetime.datetime.now()

#lets send email
print(" COMPOSING MAIL ..... ")

#UPDATE EMAIL DETAILS 

SERVER = 'smtp.gmail.com' # your smtp server 
PORT = 587 # your port number  587
FROM = 'kingbash671@gmail.com' # your email id 
TO = 'kingbash671@gmail.com'  # to email id , can be a list 
PASS = 'adhirajA@1'  # your email id passsword 


# read file 
fp = open('file1', 'r')
file1 = fp.read()
print(" file fp = ", file1)

#CREATE A TEXT PLAIN MESSAGE 
msg = MIMEMultipart()

#msg.add_header('content-disposition', 'attachment',filename='Fußballer.ppt'))
msg['Subject'] = 'Top Stories '+ ' ' + str(now.day) + " --- " + str(now.month) + ' ' + str(now.year)
msg['From'] = FROM
msg['To'] = TO 

msg.attach(file1)

# msg.attach(MIMEText(content , 'html'))
#fp.close()

# print("message is = ",msg.as_string)
print("message" , file1)

# INITIALISING SERVER ...
print("initialising server ... ")

server = smtplib.SMTP(SERVER , PORT )
server.set_debuglevel(0)            # 1 - getting debug msg if server having prblm while connecting , 0 - not getting any debug msg 
server.ehlo()
server.starttls()       # START TLS CONNECTION WHICH IS SECURED CONNECTION 
# server.ehlo
print("server....  ")

server.login(FROM,PASS)
print("login successful ...")
server.sendmail(FROM , TO , msg['Subject'] , file1)
print("EMAIL SENT .... ")

server.quit() 

# EMAIL BHEJ GAYA BUT FORMAT SHI KARNA BACHA HA 

# SENDING THROUGH CMD --- pyhton3 <file_name>

#------------------------------------------------------------------------------------------------------------------------

#vAUTOMATING THE PROCESS USING BASH SCRIPT OR CRON JOB THEN NO NEED TO RUN SCRIPT EVERYDAY , IT WILL BE AUTOMATED 