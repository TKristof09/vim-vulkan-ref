try:
  import vim
except:
  print("No vim module available outside vim")
  pass

from sys import stderr
from selenium import webdriver
BASE_URL = "https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/"
driver = webdriver.Chrome()

"""
In vimrc
map <silent> <Key> :OpenRefPage<CR>
"""
def open_ref_page():
  ok = False
  i = 0
  inp = vim.eval('expand("<cWORD>"')
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
        try:
          elem = driver.find_element_by_id(queries[i])
          print(elem.text)
        except:
          print("Element not found by id: " + queries[i])
          pass
  if not ok:
    print("Reference page not found for " + KEYWORD, file=stderr)


driver.close()