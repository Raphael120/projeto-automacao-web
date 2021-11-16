from browser import get_browser
from time import sleep


def load_form():
    get_browser().get('https://forms.gle/ES4EdBg6HLFJVWZQ7')
    sleep(5)


def fill_name(name):
    xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    element = get_browser().find_element_by_xpath(xpath)
    element.send_keys(name)


def fill_email(email):
    xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    element = get_browser().find_element_by_xpath(xpath)
    element.send_keys(email)


def fill_source(source):
    if source == 'Atacado':
        option = 1
    else:
        option = 2
    
    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[{option}]' \
            f'/label/div/div[1]/div/div[3]/div'
    
    element = get_browser().find_element_by_xpath(xpath)
    element.click()


def fill_categories(categories):
    for category in categories.split(', '):
        if category == 'Camisa':
            option = 1
        elif category == 'Calça':
            option = 2
        elif category == 'Vestido':
            option = 3
        else:
            option = 4
        
        xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[{option}]/label/div' \
                f'/div[1]/div[2] '
        
        element = get_browser().find_element_by_xpath(xpath)
        element.click()


def fill_account_type(account_type):
    xpath_open = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    element_open = get_browser().find_element_by_xpath(xpath_open)
    element_open.click()
    
    if account_type == 'Não Cadastrado':
        option = 3
    elif account_type == 'Cadastrado':
        option = 4
    elif account_type == 'Cliente Regular':
        option = 5
    else:
        option = 6
    
    sleep(2)
    xpath_option = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[{option}]/span'
    element_option = get_browser().find_element_by_xpath(xpath_option)
    element_option.click()


def fill_rating(rating):
    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[{rating}]' \
            f'/div[2]/div/div/div[3]/div '
    
    element = get_browser().find_element_by_xpath(xpath)
    element.click()


def send_form():
    xpath = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    element = get_browser().find_element_by_xpath(xpath)
    sleep(2)
    element.click()


def fill_form(sale):
    name = sale["FULL_NAME"]
    email = sale["EMAIL"]
    source = sale["SOURCE"]
    categories = sale["CATEGORIES"]
    account_type = sale["TYPE"]
    rating = sale["RATING"]
    
    load_form()
    fill_name(name)
    sleep(1)
    fill_email(email)
    sleep(1)
    fill_source(source)
    sleep(1)
    fill_categories(categories)
    sleep(1)
    fill_account_type(account_type)
    sleep(1)
    fill_rating(rating)
    sleep(2)
    send_form()


# input()
