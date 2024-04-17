from bs4 import BeautifulSoup
from selenium import webdriver

def get_text_from_url(url):
    driver = webdriver.Firefox() # или драйвер другого браузера которым вы хотите пользоваться
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    text = '\n'.join(chunk for chunk in chunks if chunk)
    driver.quit()
    return text

url = 'https://habr.com/ru/articles/349864/'
print(get_text_from_url(url))