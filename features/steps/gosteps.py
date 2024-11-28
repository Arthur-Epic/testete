from behave import given, when, then  # Importando os decoradores do Behave
from selenium import webdriver  # Importando o Selenium WebDriver para interagir com o navegador
from selenium.webdriver.common.by import By  # Para localizar elementos
from selenium.webdriver.common.keys import Keys  # Para enviar teclas, como ARROW_DOWN
from selenium.webdriver.support.ui import WebDriverWait  # Para aguardar até que o elemento esteja disponível
from selenium.webdriver.support import expected_conditions as EC  # Condições de espera, como elemento clicável ou visível
import time  # Para pausas temporárias (caso necessário)

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.jogajuntoinstituto.org/#Contato")


@when(u'Insiro meus dados')
def step_impl(context):
    context.driver.find_element(By.ID , "nome").send_keys("Arthur")
    context.driver.find_element(By.ID , "email").send_keys("arthurtutu464@gmail.com")
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN , Keys.TAB)

@when(u'"Envio a mensagem "Teste - Oi!"')
def step_impl(context):
    context.driver.find_element(By.ID, "mensagem").send_keys("Teste - Oi!")


@then(u'Envio a mensagem "Olá da turma de QA Avançado, Ilhabela Novembro 2024')
def step_impl(context):
    # Preenche a mensagem
    context.driver.find_element(By.ID, 'mensagem').send_keys('Teste de Automação')
    
    # Espera o botão de enviar ser visível e clicável
    botao_enviar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Contato"]/div[1]/form/button'))
    )
    
    # Usar JavaScript para clicar no botão (garante que o clique seja executado mesmo se houver bloqueios visuais)
    context.driver.execute_script("arguments[0].click();", botao_enviar)


    
