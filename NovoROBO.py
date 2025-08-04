from playwright.sync_api import Playwright, sync_playwright
from time import sleep
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def credenciais():
    return {
        "NTH": int(os.getenv("NTH")),
        "login": os.getenv("Login"),
        "senha": os.getenv("senha")
    }

dados = credenciais()
nth_value = dados["NTH"]

def run(playwright: Playwright) -> None:
    print(f"Iniciando navegador às {datetime.now()}")

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
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
    page.get_by_role("link", name="OEE Protótipo").click()
    sleep(1)
    page.locator("header i").click()
    sleep(10)

    iframe = page.frame_locator("#frameDash")
    iframe.locator("button:has(svg.animate-spin)").click()
    sleep(3)

    iframe.locator("button:has-text('Modo Tela Cheia')").click()
    sleep(2)

    iframe.locator("button:has(svg.lucide-x)").click()
    sleep(3)

    linha_mqb = iframe.locator("button:has-text('Detalhes')").nth(nth_value)
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
