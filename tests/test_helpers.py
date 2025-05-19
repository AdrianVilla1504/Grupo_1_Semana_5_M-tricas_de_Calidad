import pytest
from utils.helpers import cargar_pagina, completar_campo, esperar_elemento, hacer_clic, obtener_mensaje
import os
from selenium.webdriver.common.by import By

def test_obtener_mensaje_elemento_no_existe(driver):
    """Prueba que obtener_mensaje maneje correctamente cuando el elemento no existe"""
    cargar_pagina(driver, "formulario_registro_mock.html")
    mensaje = obtener_mensaje(driver, "#elemento-inexistente")
    assert mensaje == ""

def test_obtener_mensaje_elemento_existente(driver):
    """Prueba que obtener_mensaje obtenga correctamente el texto de un elemento existente"""
    cargar_pagina(driver, "formulario_registro_mock.html")
    # Primero hacemos visible un mensaje
    driver.execute_script("document.getElementById('mensaje-exito').classList.remove('oculto');")
    driver.execute_script("document.getElementById('mensaje-exito').textContent = 'Mensaje de prueba';")
    
    mensaje = obtener_mensaje(driver, "#mensaje-exito")
    assert mensaje == "Mensaje de prueba"
