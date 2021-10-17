import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login():
  driver = webdriver.Chrome()
  driver.get("https://www.abcdin.cl/customer/account/login/")

  time.sleep(5)
  
  usr = driver.find_element(By.ID,"email")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  psw = driver.find_element(By.ID,"pass")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  print(str)
  clk = driver.find_element(By.ID,"send2").click()

def registro():
  driver = webdriver.Chrome()
  driver.get("https://www.abcdin.cl/customer/account/create/")
  time.sleep(5)
  tyc = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[3]/div/div[4]/div[1]/form/fieldset[3]/div[6]/input").click()
  name = driver.find_element(By.XPATH,"/html/body/div[4]/main/div[3]/div/div[4]/div[1]/form/fieldset[1]/div[2]/div/input")
  str_n = input("Ingrese nombre: ")
  name.clear()
  name.send_keys(str_n)
  last = driver.find_element(By.XPATH,"/html/body/div[4]/main/div[3]/div/div[4]/div[1]/form/fieldset[1]/div[3]/div/input")
  last.clear()
  str_l = input("Ingrese apellido: ")
  last.send_keys(str_l)
  rut = driver.find_element(By.XPATH,"/html/body/div[4]/main/div[3]/div/div[4]/div[1]/form/fieldset[1]/div[8]/div/input")
  rut.clear()
  rut_s = input("Ingrese rut: ")
  rut.send_keys(rut_s)
  cel = driver.find_element(By.XPATH,"/html/body/div[4]/main/div[3]/div/div[4]/div[1]/form/fieldset[1]/div[10]/div/input")
  cel.clear()
  str_c = input("Ingrese telefono: ")
  cel.send_keys(str_c)
  usr = driver.find_element(By.ID,"email_address")
  usr.clear()
  login = input("Ingrese mail: ")
  usr.send_keys(login)
  psw = driver.find_element(By.ID,"password")
  psw_c = driver.find_element(By.ID, "password-confirmation")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  psw_c.send_keys(str)
  print(str_n, str_l , str_c , login , psw )
  clk = driver.find_element(By.XPATH,"/html/body/div[4]/main/div[3]/div/div[4]/div[1]/form/fieldset[3]/div[8]/div/button").click()

def cambio():
  driver = webdriver.Chrome()
  driver.get("https://www.abcdin.cl/customer/account/login/")

  time.sleep(5)
  
  usr = driver.find_element(By.ID,"email")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  psw = driver.find_element(By.ID,"pass")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  print(str)
  clk = driver.find_element(By.ID,"send2").click()
  change = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[2]/div[1]/div[3]/div[2]/div/div[2]/a[2]").click()
  psw = driver.find_element(By.ID,"current-password")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  psw = driver.find_element(By.ID,"password")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  psw_c = driver.find_element(By.ID, "password-confirmation")
  time.sleep(2)
  str_c = input("Repita password: ")
  psw_c.send_keys(str)
  accept = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[2]/div[1]/form/div[2]/div[1]/button").click()
  
def recuperar():
  driver = webdriver.Chrome()
  driver.get("https://www.abcdin.cl/customer/account/login/")
  time.sleep(5)
  rec = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[3]/div/div[4]/div[1]/div[2]/form/fieldset/div[3]/div[2]/a").click()
  usr = driver.find_element(By.ID,"email_address")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  


i = True
while i:
    print("""
    1.Login
    2.Registro
    3.Recuperar
    4.Cambiar
    """)
    j= input("Que quieres hacer: ")
    if j=="1": 
      login() 
    elif j=="2":
      registro()
    elif j=="3":
      recuperar()
    elif j == "4":
      cambio()
    elif j == "5":
      i = False
    elif j !="":
      print("\n Not Valid Choice Try again") 
