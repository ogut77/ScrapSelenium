from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time 
from time import gmtime, strftime
fn=strftime("TripBarcaPrice"+"%Y-%m-%d-%H-%M-%S")
file2= open(fn+'.txt','w+')

driver = webdriver.Firefox()
for im in range(0,31):
 ay=['2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5' , '2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5' , '2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5','2016-5'  , '2016-5' , '2016-5','2016-5','2016-5']
 gun=[   '1'  ,    '2' ,    '3' ,   '4'  ,    '5'  ,  '6'  ,  '7'    ,    '8'  ,    '9' ,  '10'  ,   '11' ,  '12'  ,   '13' ,    '14' ,  '15'   ,  '16'  ,  '17'   ,  '18' ,  '19'  ,    '20' ,  '21' ,  '22' ,  '23'    , '24'    , '25' ,  '26'  ,   '27'  ,  '28'    ,   '29'  ,    '30',    '31' ]
 
 cid='%s' %gun[im]
 ciym='%s'%ay[im]
 cod='%s' %gun[im+1]
 coym='%s' %ay[im+1]
 dng=1
 sf=0
 sr=0
 PK1 = int(time.time())
 PKW="PK;%d;" %PK1
 nm1=im+15
 nm2=nm1+1
 print nm1
 print nm2
 
 file2.write(strftime(PKW+'%Y-%m-%d;%H:%M:%S')+';'+ciym+'-'+cid+';'+coym+'-'+cod) 
 driver.get("https://www.tripadvisor.com.tr/Hotels-g187497-Barcelona_Catalonia-Hotels.html")
 if im==0:
  driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div[2]/ul/li[5]/span").click()
  driver.find_element_by_xpath("/html/body/div[5]/div/div/ul/li[2]/span[1]").click()
  time.sleep(4)
  driver.find_element_by_css_selector("div.xCloseGreen.track_target_x").click()
  driver.find_element_by_xpath("/html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div[1]/span[1]/span/span[1]").click()
  driver.find_element_by_xpath("/html/body/span/div[1]/div/div[1]/span[2]/span[%s]" %nm1).click()
  driver.find_element_by_xpath("/html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div[1]/span[2]/span/span[1]").click()
  driver.find_element_by_xpath("/html/body/span/div[1]/div/div[1]/span[1]/span[%s]" %nm2).click()
  time.sleep(4)
  
 if im>0:
  driver.find_element_by_xpath("/html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div[1]/span[1]/span/span[1]").click()
  driver.find_element_by_xpath("/html/body/span/div[1]/div/div[1]/span[1]/span[%s]" %nm1).click()
  driver.find_element_by_xpath("/html/body/div[3]/div[6]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div/div[1]/span[2]/span/span[1]").click()
  driver.find_element_by_xpath("/html/body/span/div[1]/div/div[1]/span[1]/span[%s]" %nm2).click()
 
 print "Sayfa 1","\n"	

 hr=''
 file= open('TBP.txt','w+')
 file.write(driver.page_source.encode("utf-8"))
 file.close()
 file = open("TBP.txt", "r")
 


 for line in file:
    line2=line
	
  
    if "data-rankinlist=" in line:
        hr=line.split('" id="hotel',1)[0]+';'
        #file2.write('\n'+line.split('" id="hotel',1)[0]+';')

	   
    if 'data-pernight="' in line:
	   file2.write('\n'+PKW+hr) 
	   file2.write(line.split('" data-commerceclickdat',1)[0].split('data-vendorname="',1)[1]+';')
	   file2.write(line.split('" data-taxesvalue',1)[0].split('data-pernight="',1)[1]+';')
       
 file.close()

	  
	
 for sf in range(1,17):
  ra=sf*30
  sf1=sf+1
  driver.get(" https://www.tripadvisor.com.tr/Hotels-g187497-oa%s-Barcelona_Catalonia-Hotels.html" %ra)
  print "Sayfa %s" %sf1,"\n"  
  file= open('TBP.txt','w+')
  file.write(driver.page_source.encode("utf-8"))
  file.close()
  file = open("TBP.txt", "r")
  

  for line in file:
    line2=line
	
    

    if "data-rankinlist=" in line:
       hr=line.split('" id="hotel',1)[0]+';'
       #file2.write('\n'+line.split('" id="hotel',1)[0]+';')


	   
    if 'data-pernight="' in line:
       file2.write(PKW+hr)
       file2.write(line.split('" data-commerceclickdat',1)[0].split('data-vendorname="',1)[1]+';')
       file2.write(line.split('" data-taxesvalue',1)[0].split('data-pernight="',1)[1]+';'+'\n')

  file.close()	   
