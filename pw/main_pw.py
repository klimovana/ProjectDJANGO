from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Запуск в видимом режиме
    context = browser.new_context()
    page = context.new_page()

    try:
        print("Navigating to the page...")
        page.goto("https://guu.ru/", timeout=60000, wait_until="domcontentloaded")
        print("Page loaded successfully.")

        page.get_by_role("link", name="Внеучебная деятельность").click()
        print("Current working directory:", os.getcwd())
        print("Before screenshot")
        page.screenshot(path="C:\\Users\\a2_na\\Desktop\\screenshot.png")
        print("After screenshot")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        context.close()
        browser.close()