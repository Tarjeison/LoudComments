from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from gtts import gTTS
from pygame import mixer  # Load the popular external library
import pyttsx3
import time


def tts2(word: str):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def tts1(word: str):
    language = 'fr-fr'
    myobj = gTTS(text=word, lang=language, slow=False)
    myobj.save("welcome.mp3")
    mixer.init()
    mixer.music.load('welcome.mp3')
    mixer.music.play()


def build_firefox() -> Firefox:
    opts = Options()
    return Firefox(executable_path='C:\\Users\\Trym\\drivers\\gecko\\geckodriver.exe', options=opts)


def get_text_from_web_element(web_element: WebElement):
    return web_element.text


def find_all_comments_in_article(browser: Firefox) -> [str]:
    try:
        time.sleep(3)
        dismiss_gdpr_if_present(browser)
        time.sleep(1)
        browser.execute_script("arguments[0].scrollIntoView(true);",
                               browser.find_element_by_class_name('css-k5mcwh'))
        time.sleep(1)
        iframe = browser.find_element_by_class_name('cc-discussion')
        browser.find_element_by_class_name('cc-discussion')
        browser.switch_to.frame(iframe)
        browser.find_element_by_class_name('load-more').click()
        time.sleep(1)
        comments = browser.find_elements_by_class_name('comment-content')
        comment_list = list(map(get_text_from_web_element, comments))
        return comment_list
    except NoSuchElementException:
        print("No comments")
        return []


def dismiss_gdpr_if_present(browser: Firefox):
    try:
        frame = browser.find_element_by_id('sp_message_iframe_481243')
        browser.switch_to.frame(frame)
        browser.find_element_by_class_name('button-ok').click()
        browser.switch_to.window(browser.window_handles[-1])
    except Exception:
        pass


def read_first_comment_in_first_article():
    browser = build_firefox()
    browser.get('https://vg.no')
    time.sleep(2)
    dismiss_gdpr_if_present(browser)
    all_articles = browser.find_elements_by_class_name('article-container')
    actions = ActionChains(browser)
    for article in all_articles:
        try:
            print(article.text)
            actions.move_to_element(article)
            browser.execute_script("arguments[0].scrollIntoView(true);", article)
            ActionChains(browser).key_down(Keys.CONTROL).click(article).perform()
            browser.switch_to.window(browser.window_handles[-1])
            time.sleep(2)
            comments = find_all_comments_in_article(browser)
            browser.close()
            browser.switch_to.window(browser.window_handles[-1])
            if len(comments) != 0:
                print(comments[0])
                tts2(comments[0])

        except Exception:
            print("FAIl for article ", article.text)
            pass

    browser.close()
    quit()


if __name__ == '__main__':
    read_first_comment_in_first_article()
