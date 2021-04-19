from flask import Flask, render_template, request, redirect, session, flash, url_for
#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash:mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica

app = Flask(__name__)
app.secret_key = 'flask'
#chave secreta da sessão

class Person:
    def __init__(self, FirstName, LastName, Participation):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Participation = Participation


#base de dados de pessoas
person1 = Person('Carlos', 'Moura', 5)
person2 = Person('Fernanda', 'Oliveira', 15)
person3 = Person('Hugo', 'Silva', 20)
person4 = Person('Eliza', 'Souza', 20)
person5 = Person('Anderson', 'Santos', 40)

lista = [person1, person2, person3, person4, person5]



#configuração da rota index.
@app.route('/')
def index():
    return render_template('lista.html', persons=lista)
    #renderizando o template lista e as variáveis desejadas. 


#configuração da rpta criar que usa o método post para enviar dados das nossas pessoas
@app.route('/criar', methods=['POST',])
def criar():
    FirstName = request. form['FirstName']
    LastName = request. form['LastName']
    Participation = request. form['Participation']
    person = Person(FirstName, LastName, Participation)
    lista.append(person)
    return redirect(url_for('index'))
#já inclui a nova pessoa na lista e joga na tela inicial



app.run(debug=True)
