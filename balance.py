from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
#import re

driver = webdriver.Chrome()

driver.get("https://bear.hellomoving.com/wc.dll?mp~NetLogonWc~AONEVAN")
network_username = "kfarsaba"
network_password = "ramla"

id_username = "MANUEL"
id_password = "maria1980"

#Set time frame
#from_date = "11/00/2020"
#to_date = "02/21/2021"

#Network Log in
network_l = driver.find_element_by_name("LOGON_USER").clear()
network_l = driver.find_element_by_name("LOGON_USER").send_keys(network_username)
network_p = driver.find_element_by_name("PASSWORD").clear()
network_p = driver.find_element_by_name("PASSWORD").send_keys(network_password)
driver.find_element_by_name("LOGON").click()

#User Log in
network_l = driver.find_element_by_name("USERNAME").clear()
network_l = driver.find_element_by_name("USERNAME").send_keys(id_username)
network_p = driver.find_element_by_name("PASSWORD").clear()
network_p = driver.find_element_by_name("PASSWORD").send_keys(id_password)
driver.find_element_by_name("btnSubmit").click()

#Get List of Estimates
driver.find_element_by_xpath("/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/font[1]").click()

#Get New Tabs
tabs = driver.window_handles
#print(tabs)

#Switch tab
driver.switch_to.window(tabs[1])

#Set Time Frame
#driver.find_element_by_xpath("//input[@id='Date1']").clear()
#driver.find_element_by_xpath("//input[@id='Date1']").send_keys(from_date)
#driver.find_element_by_xpath("//input[@id='Date2']").clear()
#driver.find_element_by_xpath("//input[@id='Date2']").send_keys(to_date)

#Set Priority
driver.find_element_by_xpath("//select[@name='FUSTATUS']/option[text()='4']").click()

#Submit
driver.find_element_by_id('btnSubmit').click()

#Get All Jobs
tags = driver.find_elements_by_tag_name("a")

#Cretate List of URLs
urls = []
for url in tags[1:]:
	urls.append(url.get_attribute("href"))
#print(urls)

for estimate in urls:

	#Open New Tab
	driver.execute_script('''window.open("","_blank");''')

	#Get New Tabs
	tabs = driver.window_handles
	#print(tabs)
	#input("Press Enter to continue...")
	if len(tabs) == 4:
		driver.switch_to.window(tabs[3])
		driver.close()
		tabs = driver.window_handles

	#Switch tab
	driver.switch_to.window(tabs[2])
	
	#Open th Estimate
	driver.get(estimate)

	#Print Job Number
	print(driver.title)

	sourcecode = driver.page_source
	booked = "Job is Booked"
	removal = "The email is on the removal list"
	closed = "Job is in storage or Closed"
	string = "Your Estimate from A One Van Lines"
	pickup = "Submit Pick-Up"
	manisha = "MANISHA"

	#Check if booked or removed
	if booked in sourcecode:
		print("Job booked. Skiping...\n")
	elif removal in sourcecode:
		print("The email is on the removal list. Skiping...\n")
	elif closed in sourcecode:
		print("Skiping...\n")
	elif manisha in sourcecode:
		print("Manisha's lead. Skiping...\n")
	elif pickup in sourcecode:
		print("Job Booked on Delivery. Skiping...\n")
	else:
		#click Email Center
		#time.sleep(5)
		try:
			driver.find_element_by_xpath("/html[1]/body[1]/table[3]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[1]/a[1]/font[1]/b[1]").click()
		except:
			print("no email found, skipping")
			continue
		#Select Emails-Center Tab
		tabs = driver.window_handles
		#print(tabs)
		#print(len(tabs))
		if len(tabs) == 5:
			driver.switch_to.window(tabs[3])
			driver.close()
			tabs = driver.window_handles
		elif len(tabs) == 6:
			driver.switch_to.window(tabs[4])
			driver.close()
			driver.switch_to.window(tabs[3])
			driver.close()
			tabs = driver.window_handles
		elif len(tabs) == 7:
			driver.switch_to.window(tabs[5])
			driver.close()
			driver.switch_to.window(tabs[4])
			driver.close()
			driver.switch_to.window(tabs[3])
			driver.close()
			tabs = driver.window_handles
		elif len(tabs) == 8:
			driver.switch_to.window(tabs[6])
			driver.close()
			driver.switch_to.window(tabs[5])
			driver.close()
			driver.switch_to.window(tabs[4])
			driver.close()
			driver.switch_to.window(tabs[3])
			driver.close()
			tabs = driver.window_handles
		elif len(tabs) == 9:
			driver.switch_to.window(tabs[7])
			driver.close()
			driver.switch_to.window(tabs[6])
			driver.close()
			driver.switch_to.window(tabs[5])
			driver.close()
			driver.switch_to.window(tabs[4])
			driver.close()
			driver.switch_to.window(tabs[3])
			driver.close()
			tabs = driver.window_handles
		driver.switch_to.window(tabs[3])
		email_sourcecode = driver.page_source
		if string not in email_sourcecode:
			print("Not estimate. Skiping...\n")
			driver.close()
			driver.switch_to.window(tabs[2])
			driver.close()
			driver.switch_to.window(tabs[1])
		else:
			driver.find_element_by_xpath("//input[@value='65630']").click()
			#time.sleep(5)
			#Send Email
			#driver.find_element_by_xpath("//input[@name='SUBMIT_2']").click()
			print("Estimate found. Sending Email...\n")
			driver.close()
			driver.switch_to.window(tabs[2])
			driver.close()
			driver.switch_to.window(tabs[1])

#time.sleep(5)
driver.quit()
os.system('cmd /c "taskkill /T /F /IM chromedriver.exe"')
	#break

#driver.quit()
#taskkill /T /F /IM chromedriver.exe