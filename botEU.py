import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def login():
  driver = webdriver.Chrome()
  driver.get("https://www.sprintersports.com/login")
  driver.maximize_window()

  time.sleep(5)
  
  usr = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[1]/input")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  psw = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[2]/input")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  print(str)
  clk = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[3]/button").click()

def registro():
  driver = webdriver.Chrome()
  driver.get("https://www.sprintersports.com/registro")
  driver.maximize_window()
  time.sleep(5)
  

  usr = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/article/div/form/div[1]/input")
  usr.clear()
  login = input("Ingrese mail: ")
  usr.send_keys(login)
  name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/article/div/form/div[5]/input")
  str_n = input("Ingrese nombre: ")
  name.clear()
  name.send_keys(str_n)
  last = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/article/div/form/div[6]/input")
  last.clear()
  str_l = input("Ingrese apellido: ")
  last.send_keys(str_l)
  psw = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/article/div/form/div[7]/input")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  psw_c = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/article/div/form/div[8]/input")
  str_c = input("Repita password: ")
  psw_c.send_keys(str_c)
  
  accept = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/article/div/form/div[9]/label/span[1]").click()
  n_accept = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/article/div/form/div[10]/div[2]/label[2]/span[1]").click()
  clk = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/article/div/form/div[11]/button").click()

def cambio():
  driver = webdriver.Chrome()
  driver.get("https://www.sprintersports.com/login")
  driver.maximize_window()

  time.sleep(5)
  
  usr = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[1]/input")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  psw = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[2]/input")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  print(str)
  clk = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[3]/button").click()

  change = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/section[1]/div/div[2]/button").click()

  psw = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/section[1]/article/form/div[2]/div[1]/div/input")
  str = input("Ingrese password: ")
  psw.send_keys(str)
  psw_c = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/section[1]/article/form/div[2]/div[2]/div/input")
  str_c = input("Repita password: ")
  psw_c.send_keys(str)
  accept = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div/section[1]/article/form/div[5]/button").click()
  
def recuperar():
  driver = webdriver.Chrome()
  driver.get("https://www.sprintersports.com/login")
  driver.maximize_window()
  time.sleep(5)

  rec = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[1]/div/article/p/button").click()
  usr = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[1]/input")
  login = input("Ingrese mail: ")
  usr.clear()
  usr.send_keys(login)
  clk = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[1]/div/article/form/div[2]/button").click()
  


i = True
while i:
    print("""
    1.Login
    2.Registro
    3.Recuperar
    4.Cambiar
    5.Salir
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

