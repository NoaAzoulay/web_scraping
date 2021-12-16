
from selenium import webdriver
import os
import time
import search_model
import create_table

url = 'https://www.bbc.com/'
class_name_title='media__title'
class_name_link='media__link'
url_att ='href'
url_list =[]

def start_driver():
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

# put links of all articles in list
def get_links():
    links = driver.find_elements_by_class_name(class_name_title)
    for link in links:
       url=link.find_element_by_class_name(class_name_link).get_attribute(url_att)
       url_list.append(url)
    print(url_list)
    driver.close()

# write data to file
def write_to_file(arg, file_name):
    file_name="articles_files/"+file_name
    file = open(file_name, 'a', encoding="utf-8")
    if type(arg)==str:
        file.write(arg)
        file.write('\n')
    else:
        for i in arg:
            file.write(i.get_attribute('innerText'))
            file.write('\n')
    file.close()

# write all data to files
def writing_content_to_file():
    for i in range(len(url_list)) :
        driver = webdriver.Chrome()
        driver.get(url_list[i])
        time.sleep(8)
        url_text= url_list[i]
        print(url_text)
        paragraph_text= driver.find_elements_by_tag_name('p')
        header1_text = driver.find_elements_by_tag_name('h1')
        header2_text=driver.find_elements_by_tag_name('h2')
        header3_text=driver.find_elements_by_tag_name('h3')
        header4_text=driver.find_elements_by_tag_name('h4')
        header5_text = driver.find_elements_by_tag_name('h5')
        header6_text = driver.find_elements_by_tag_name('h6')
        article_headline=driver.find_elements_by_class_name('article-headline__collection')
        some_text=driver.find_elements_by_class_name('copyright__text b-reith-sans-font')
        picture_caption= driver.find_elements_by_class_name('ssrcss-1yybcoc-Stack e1y4nx260')
        author= driver.find_elements_by_class_name('author-unit')
        create_table.create_folder('articles_files')
        file_name = 'article' + str(i)+ '.txt'

        write_to_file(url_text, file_name)
        if author:
            write_to_file(author,file_name)
        if article_headline:
            write_to_file(article_headline,file_name)
        if some_text:
            write_to_file(some_text,file_name)
        if picture_caption:
            write_to_file(picture_caption,file_name)
        if header1_text:
            write_to_file(header1_text, file_name)
        if header2_text:
            write_to_file(header2_text, file_name)
        if header3_text:
            write_to_file(header3_text, file_name)
        if header4_text:
            write_to_file(header4_text, file_name)
        if header5_text:
            write_to_file(header5_text, file_name)
        if header6_text:
            write_to_file(header6_text, file_name)
        if paragraph_text:
            write_to_file(paragraph_text, file_name)

        driver.close()


# enter string to search
def search():
    path = os.getcwd()
    str=""
    search_model.search_string_in_files(str, 'articles_files', path)

# main
start_driver()
get_links()
writing_content_to_file()












