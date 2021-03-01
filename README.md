# Atividade Flask

Vocês devem utilizar como base as instruções que foram passadas durante a reunião de sábado (27/02).
Caso haja alguma dúvida em relação a execução da tarefa, me procure no telegram @imfepas.

## Instruções

 - Criem uma branch com o nome da dupla, e nessa branch executem todo o código necessário.  
 - Desenvolvam 3 endpoints na API:
    - O primeiro deve salvar um novo usuário no formato JSON, utilizando o método POST, da seguinte forma: 

        ```js
        {
            "name":"Felipe Campos",
            "birth_day": "14",
            "birth_month": "05",
            "birth_year": "1998"
        }
        ```

        Lembrem-se de utilizar o BODY da requisição para enviar os dados. Essa requisição deve, além de salvar o usuário, retornar uma resposta no formato:

            O usuário <name> foi salvo.

    - O segundo deve ser acessado por uma requisição direto pela URL, utilizando o método GET, da seguinte forma:

            localhost:5000/users

        E deve retornar todos os usuários salvos em forma de uma lista de JSON.


      ```js
            [
                {
                "name":"Felipe Campos",
                "birth_day": "14",
                "birth_month": "05",
                "birth_year": "1998"
                },
                {
                "name":"Natanny Campos",
                "birth_day": "18",
                "birth_month": "01",
                "birth_year": "1991"
                }
            ]
      ```
    - O terceiro deve ser acessado por uma requisição direto pela URL, utilizando o método GET, da seguinte forma: 
    
            localhost:5000/sign/<name>

        E deve retornar um JSON com a estrutura básica de usuário, e um campo a mais no JSON chamado *sign*, que deve ser o signo dessa pessoa.

       ```js
              {
                  "name":"Felipe Campos",
                  "birth_day": "14",
                  "birth_month": "05",
                  "birth_year": "1998",
                  "sign": "Taurus"
              }
       ```

        Caso o usuário não exista, retorne uma mensagem de erro.

        <br>

        Have fun!!


    


            










