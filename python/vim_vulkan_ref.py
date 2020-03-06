try:
    import vim
except:
    print("No vim module available outside vim")
    pass

import time
from sys import stderr
from threading import Thread
from selenium import webdriver
BASE_URL = "https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/"

"""
In vimrc
map <silent> <Key> :OpenRefPage<CR>
"""

driver = None
started = False

def start_driver():
    global driver, started
    driver = webdriver.Chrome()
    started = True

# TODO multi tab support 
#      (use driver.execute_script("window.open('url', '_blank');") then
#      driver.switch_to.window(window_handle)
#      with window handle being driver.window_handles[tab_number]
def _open_ref_page():
    global driver
    if not started:
        print("Driver isnt started")
        return
    handle = driver.current_window_handle
    ok = False
    i = 0
    inp = vim.eval('expand("<cword>")')
    KEYWORD = "vk" + inp[0].upper() + inp[1:]
    queries = [KEYWORD, KEYWORD[0].upper() + KEYWORD[1:]]
    while not ok and i < len(queries):
        driver.get(BASE_URL + queries[i] + ".html")
        try:
            err = driver.find_element_by_class_name("error_header")
            if "404" in err.text:
                i += 1
        except:
            ok = True
            # TODO maybe do something like paste in the code snippet from the
            # ref page
            # This code get the text from the code snippet on the ref page
            """
            try:
                elem = driver.find_element_by_id(queries[i])
                print(elem.text)
            except:
                print("Element not found by id: " + queries[i])
                pass
            """
    if not ok:
        print("Reference page not found for " + KEYWORD, file=stderr)
    

def close_driver():
    global started
    started = False
    driver.quit()

def open_ref_page():
    if not started:
        start_driver()
    thread = Thread(target=_open_ref_page)
    thread.start()
