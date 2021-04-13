from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def build_firefox() -> Firefox:
    opts = Options()
    opts.headless = True
    assert opts.headless  # Operating in headless mode
    return Firefox(executable_path='C:\\Users\\Trym\\drivers\\gecko\\geckodriver.exe', options=opts)


def hello_vg():
    browser = build_firefox()
    browser.get('https://vg.no')
    browser.implicitly_wait(2)
    headline = browser.find_element_by_class_name('headline')
    print(headline.text.replace("\n", " "))


if __name__ == '__main__':
    hello_vg()
