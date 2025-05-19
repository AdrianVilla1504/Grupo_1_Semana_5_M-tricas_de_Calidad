import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cargar_pagina(driver, ruta_html):
    """Carga la página HTML desde una ruta local"""
    ruta_absoluta = os.path.abspath(ruta_html)
    driver.get(f"file:///{ruta_absoluta}")
    sleep(1)  # Pequeña pausa para asegurar que la página cargue

def completar_campo(driver, id_campo, valor):
    """Completa un campo del formulario con el valor especificado"""
    campo = driver.find_element(By.ID, id_campo)
    campo.clear()
    campo.send_keys(valor)
    
def esperar_elemento(driver, selector, tiempo=10):
    """Espera a que un elemento esté disponible en la página"""
    return WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )

def hacer_clic(driver, selector):
    """Hace clic en un elemento de la página"""
    elemento = driver.find_element(By.CSS_SELECTOR, selector)
    elemento.click()
    
def obtener_mensaje(driver, selector):
    """Obtiene el texto de un mensaje en la página"""
    try:
        elementos = driver.find_elements(By.CSS_SELECTOR, selector)
        if elementos and elementos[0].is_displayed():
            return elementos[0].text
        return ""
    except:
        return ""
