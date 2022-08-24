from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import date
today=date.today()

file=open("googlemapsreport.txt","w")
file.writelines("Report for "+str(today)+"\n")
file.close()

file=open("googlemapsreport.txt","a")


source=input("Enter the starting location  :  ")
destination=input("Enter your destination  :  ")

driver=webdriver.Chrome(r"O:\SORTED\\exe\\chromedriver.exe")

driver.get("https://www.google.com/maps/@18.9661184,73.07264,12z")

time.sleep(2)
directions=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div/button/img")
directions.click()

time.sleep(3)

src=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
src.send_keys(source)

time.sleep(0.5)

dest=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/input")
dest.send_keys(destination)

search=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]")
search.click()

time.sleep(5)
try:
    drive=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/button/img")
    drive.click()
    time.sleep(3)
    times_car=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[1]/span[1]")
    file.writelines("time by car : "+ times_car.text+"\n")
    kilometers_car=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]/div")
    file.writelines("kilometers by car : "+kilometers_car.text+"\n")
    time.sleep(2)
except:
    file.writelines("car not available")

try:
    train=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[3]/button/img")
    train.click()
    time.sleep(3)
    times_train=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[2]/div[1]/div")
    file.writelines("time by train : "+ times_train.text+"\n")
    time.sleep(2)
except:
    file.writelines("train not available"+"\n")



try:
    walking=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[4]/button/img")
    walking.click()
    time.sleep(3)
    times_walking=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[3]/div[1]/div[1]")
    file.writelines("time by walking : "+ times_walking.text+"\n")
    kilometers_walking=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[3]/div[1]/div[2]")
    file.writelines("kilometers by walking : "+kilometers_walking.text+"\n")
except:
    file.writelines("no one has walked their way through..."+"\n")

try:
    flights=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/button/img")
    flights.click()
    time.sleep(3)
    times_flights=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div/div/div[4]/div[2]/div[1]/span[2]")
    file.writelines("time by flight : "+ times_flights.text+"\n")
    fare_flights=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div/div/div[4]/div[2]/div[3]/span[2]/span")
    file.writelines("fare by flight : "+fare_flights.text+"\n")
except:
    file.writelines("not available"+"\n")

file.close

time.sleep(2)
driver.quit()




