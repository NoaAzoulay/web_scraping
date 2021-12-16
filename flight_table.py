
import json
import time
from selenium import webdriver
import os
import create_table
import search_model

url ="http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
global driver
driver = webdriver.Chrome()
class_airline="td-airline"
class_flight="td-flight"
class_city="td-city"
class_terminal="td-terminal"
class_sch_time="td-scheduledTime"
class_upd_time="td-updatedTime"
class_status= "td-status"
class_table='table-responsive'
class_even_row="flight_row css-row_even"
class_odd_row="flight_row"
button_load_more_xpath = '//*[@id="next"]'
num_of_results_id='numOfResults'
total_items='totalItems'
button_stop_auto_update_xpath='//*[@id="toggleAutoUpdate"]'
counter=0

airline_list=[]
flight_list=[]
city_list=[]
terminal_list=[]
sch_time_list=[]
updt_time_list=[]
status_list=[]

class flights_table_detailes:
    def __init__(self, airline, flight, city, terminal, scheduled_time, updated_time, status):
        self.airline = airline
        self.flight = flight
        self.city=city
        self.terminal=terminal
        self.scheduled_time= scheduled_time,
        self.updated_time = updated_time
        self.status=status

# open fully page to get all table rows
def fully_open_page(button_stop_auto_update, button_load_more):
    button_stop_auto_update.click()
    results_num = driver.find_element_by_id(num_of_results_id)
    total_num = driver.find_element_by_id(total_items)
    while results_num!= total_num:
        # time.sleep(8)
        try:
            if button_load_more.click():
                results_num=driver.find_element_by_id(num_of_results_id)
                total_num=driver.find_element_by_id(total_items)
        except:
            break


def create_data_lists_by_class_name(list_name, class_name ):
    data= driver.find_elements_by_class_name(class_name)
    for d in data:
        ar=d.text
        list_name.append(ar)


# create objects of data and write to file
def create_objects_of_every_row(counter):
    for i in range(len(city_list)):
        flight=flights_table_detailes(airline_list[i],flight_list[i],city_list[i],
                                      terminal_list[i],sch_time_list[i],updt_time_list[i],status_list[i])
        create_table.create_folder('flight_files')
        write_to_json_file(flight, counter)

# write content in jn json format
def write_to_json_file(flight, counter):
        file_name = 'flight_files/flights_table' +str(counter)+ '.json'
        with open(file_name, 'a', encoding="utf-8") as outfile:
            json.dump(flight.__dict__, outfile, ensure_ascii=False)
            outfile.write('\n')


# compare pages content to check if there are cupdates
def compare_tables(current):
        driver = webdriver.Chrome()
        new = driver.find_elements_by_class_name(class_table)
        if current!=new:
            driver.close()
            return True
        else:
            driver.close()
            return False



def start(counter):
    global current_content
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    button_load_more =driver.find_elements_by_xpath(button_load_more_xpath)[0]
    button_stop_auto_update=driver.find_elements_by_xpath(button_stop_auto_update_xpath)[0]
        #     # open all rows in page
    fully_open_page(button_stop_auto_update,button_load_more)
    current_content = driver.find_elements_by_class_name(class_table)
        #     # create data list of each column
    create_data_lists_by_class_name(airline_list, class_airline)
    create_data_lists_by_class_name(flight_list, class_flight)
    create_data_lists_by_class_name(city_list, class_city)
    create_data_lists_by_class_name(terminal_list, class_terminal)
    create_data_lists_by_class_name(sch_time_list, class_sch_time)
    create_data_lists_by_class_name(updt_time_list, class_upd_time)
    create_data_lists_by_class_name(status_list, class_status)
        #     # create objects of every row and write it to json file
    create_objects_of_every_row(counter)
    driver.close()

# enter string to search in files
def search():
    path = os.getcwd()
    str=""
    search_model.search_string_in_files(str,'flight_files', path)


# main
start(counter)
while(True):
    counter+=1
    if(compare_tables(current_content)):
        start(counter)
    else:
        time.sleep(60)







