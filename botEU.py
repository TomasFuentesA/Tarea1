import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login():
  driver = webdriver.Chrome()
  driver.get("https://cuenta.elcorteingles.es/")
  driver.maximize_window()

  time.sleep(5)
  
  usr = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[1]/div[2]/div/input")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  psw = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[1]/div[3]/div[1]/input")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  print(str)
  clk = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[2]/div/input").click()

def registro():
  driver = webdriver.Chrome()
  driver.get("https://cuenta.elcorteingles.es/registro/")
  driver.maximize_window()
  time.sleep(5)

  usr = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/main/form/div[1]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/input")
  usr.clear()
  login = input("Ingrese mail: ")
  usr.send_keys(login)
  psw = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/main/form/div[1]/div[2]/div[1]/fieldset[1]/div[2]/div[1]/div/input")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  psw_c = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/main/form/div[1]/div[2]/div[1]/fieldset[1]/div[2]/div[2]/input")
  str_c = input("Repita password: ")
  psw_c.send_keys(str_c)
  name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/main/form/div[1]/div[2]/div[1]/fieldset[2]/div[1]/div/input")
  str_n = input("Ingrese nombre: ")
  name.clear()
  name.send_keys(str_n)
  last = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/main/form/div[1]/div[2]/div[1]/fieldset[2]/div[2]/div[1]/div/input")
  last.clear()
  str_l = input("Ingrese apellido: ")
  last.send_keys(str_l)
  accept = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/main/form/div[1]/div[2]/section/div/div/div[1]/div/label").click()
  clk = driver.find_element(By.XPATH,"/html/body/div[4]/main/div[3]/div/div[4]/div[1]/form/fieldset[3]/div[8]/div/button").click()

def cambio():
  driver = webdriver.Chrome()
  driver.get("https://cuenta.elcorteingles.es/")
  driver.maximize_window()
  time.sleep(5)
  
  usr = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[1]/div[2]/div/input")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  psw = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[1]/div[3]/div[1]/input")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  print(str)
  clk = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[2]/div/input").click()

  change = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div/nav/div[2]/div[5]/div[6]/div[2]/div[1]/a").click()

  psw = driver.find_element(By.ID,"password")
  str = input("Ingrese password actual: ")
  psw.send_keys(str)
  psw = driver.find_element(By.ID,"change-password")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  psw_c = driver.find_element(By.ID, "repeat-change-passwor")
  time.sleep(2)
  str_c = input("Repita password: ")
  psw_c.send_keys(str)
  accept = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/div[1]/form[2]/div[3]/input").click()
  
def recuperar():
  driver = webdriver.Chrome()
  driver.get("https://cuenta.elcorteingles.es/")
  driver.maximize_window()
  time.sleep(5)

  rec = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[1]/div[3]/div[2]/a").click()
  usr = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div[2]/form/fieldset/div/div[1]/div/input")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  clk = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[2]/form/fieldset/div/div[2]/input").click()
  


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

