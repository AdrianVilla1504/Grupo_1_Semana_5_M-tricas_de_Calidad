import os
import sys
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
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Detecta el sistema operativo y usa el ejecutable correcto
    if sys.platform.startswith("win"):
        chrome_driver_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "chromedriver.exe"
        )
        service = Service(executable_path=chrome_driver_path)
    else:
        # En Linux (GitHub Actions), el chromedriver está en el PATH
        service = Service(executable_path="chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  # Espera implícita

    yield driver

    driver.quit()