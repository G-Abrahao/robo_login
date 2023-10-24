from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ava.mg.senac.br/edu/")
    page.fill('xpath=//*[@id="username"]', "seu_usuario@senacminas.edu.br")
    page.fill('//*[@id="password"]',"sua senha") 
    page.locator('xpath=//*[@id="boxForm"]/div/form/div[3]/button').click()
    page.wait_for_timeout(60000)