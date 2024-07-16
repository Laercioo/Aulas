from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select


@given(u'que estou na página do instituto joga junto')
def step_on_instituto_page(context):
    context.browser = Firefox()
    context.browser.get('https://www.jogajuntoinstituto.org/')
    
    browser_title = context.browser.title
    assert 'Instituto Joga Junto' in browser_title, "Titulo não encontrado"
    
    
@when(u'prencho p formulario de contato')
def step_impl(context):
    context.browser.find_elements_by(By.name, 'e-mail').send_keys('email@gmail.com')
    context.browser.find_elements_by(By.name, 'nome').send_keys('João da Silva')
    context.browser.find_elements_by(By.name, 'body').send_keys('Minha primeira automação com behave')
    select_subjects = context.browser.find_element_by(By.name, 'assunto'). send_keys('Minha primeira automação com behave')
    select = Select(select_subjets)


@when(u'aperto o botão de enviar')
def step_impl(context):
    pass

@then(u'os dados são recebidos com sucesso')
def step_impl(context):
    pass