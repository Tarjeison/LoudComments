from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pyttsx3
import time


def build_firefox() -> Firefox:
    opts = Options()
    opts.headless = True
    assert opts.headless  # Operating in headless mode
    return Firefox(executable_path='C:\\Users\\Trym\\drivers\\gecko\\geckodriver.exe', options=opts)


def read_first_comment_in_first_article():
    browser = build_firefox()
    browser.get('https://vg.no')
    browser.implicitly_wait(2)
    browser.find_elements_by_class_name('article-container')[0].click()

    browser.execute_script("arguments[0].scrollIntoView(true);",
                           browser.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div[4]/div')
                           )
    time.sleep(4)

    iframe = browser.find_element_by_class_name('cc-discussion')
    browser.switch_to.frame(iframe)
    comments = browser.find_elements_by_class_name('comment-content')
    first_comment = comments[0].text.replace("\n", " ")
    print(first_comment)
    engine = pyttsx3.init()
    engine.say(first_comment)
    engine.runAndWait()
    browser.close()
    quit()


if __name__ == '__main__':
    read_first_comment_in_first_article()
