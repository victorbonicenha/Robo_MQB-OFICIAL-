from playwright.sync_api import Playwright, sync_playwright
from time import sleep
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
home = os.path.expanduser("~")
chrome_path = os.path.join(home, ".cache", "ms-playwright", "chromium-1169", "chrome-linux", "chrome")
nth_value = int(os.getenv("NTH"))

def credenciais():
    return {
        "NTH": int(os.getenv("NTH")),
        "login": os.getenv("Login"),
        "senha": os.getenv("senha")
    }

dados = credenciais()

def run(playwright: Playwright) -> None:
    print(f"Iniciando navegador às {datetime.now()}")
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], executable_path=chrome_path)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://datadriven.datawake.com.br:8057/data-driven/login.html")
    sleep(1)
    page.get_by_role("textbox", name="Email:").fill(dados["login"])
    sleep(1)
    page.get_by_role("textbox", name="Senha").fill(dados["senha"])
    sleep(1)
    page.get_by_role("button", name="Login").click()
    sleep(5)
    page.locator("header i").click()
    sleep(1)
    page.get_by_role("link", name="DASHBOARD ").click()
    sleep(1)
    page.get_by_role("link", name="MANUFATURA ").click()
    sleep(1)
    page.get_by_role("link", name="OEE Online").click()
    sleep(1)
    page.locator("header i").click()
    sleep(10)
    page.locator("iframe[title=\"OEE Online Dashboard\"]").content_frame.locator(".header-expand-icon").click()
    sleep(10)
    linha_mqb = page.locator("iframe[title=\"OEE Online Dashboard\"]").content_frame.locator(".btn-unit").nth(nth_value)
    linha_mqb.click()
    sleep(20)
    
    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        pass  

    browser.close()
    print(f"Navegador fechado às {datetime.now()}\n")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)

 