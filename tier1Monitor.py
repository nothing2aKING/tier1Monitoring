import requests 

from datetime import date

import tkinter as tk
#from PIL import Image, ImageTk



#creates frame
window =tk.Tk()
#creates frame geometry
window.geometry("500x400")
#title of frame
window.title("Monitor Tier 1 Customer")

#adding labels
yearlabel = tk.Label(text='Environment Name')
yearlabel.grid(column=0, row=1)

text_answer = tk.Text(master=window, height=20, width=60)
text_answer.grid(column=1, row=5)


data = [
    { 'env_name': 'Delhaize', 'url':'https://delhaize.relexsolutions.com/auth/support'},
    { 'env_name': 'Morrisons', 'url':'https://morrisons.relexsolutions.co.uk/auth/support'},
 ]




def Tier_1(url):

    r = requests.get(url)

    if r.status_code == 200:
         pg_up = "Responsive"
         return pg_up
    else:
        pg_down = "Unresponsive"
        return pg_down
    
    
    
for i in data:
  #print("Environment Name: {} \nStatus of Environment: {}".format(i['env_name'],Tier_1(i['url'])))
    status = "Environment Name: {} \nStatus of Environment: {}\n".format(i['env_name'],Tier_1(i['url']))
    text_answer.insert(tk.END, status)


'''server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("your username", "your password")
server.sendmail(
  "from@address.com", 
  "to@address.com", 
  "this message is from python")
server.quit()'''
    
   

window.mainloop()


    

#urls = ['http://delhaize.relexsolutions.com/auth/support', 'http://morrisons.relexsolutions.co.uk/auth/support',]

#env_name = ['Delhaize','Morrisons']



#today = date.today() 
#print(today)

   




 