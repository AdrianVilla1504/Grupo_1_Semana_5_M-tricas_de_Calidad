import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    """
    Fixture que proporciona un driver de Chrome configurado para las pruebas.
    Se ejecuta antes de cada test y se cierra después.
    """
    # Ruta al chromedriver existente en el proyecto
    chrome_driver_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "chromedriver.exe"
    )
    
    # Configurar opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Ignorar advertencias de compatibilidad de versiones
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Configurar servicio con la ruta explícita
    service = Service(executable_path=chrome_driver_path)
    
    # Iniciar el driver con la ruta explícita y las opciones
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  # Espera implícita
    
    # Ceder el driver al test
    yield driver
    
    # Cerrar el driver después del test
    driver.quit()
