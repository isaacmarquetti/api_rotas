# Api_rotas

> Status: Concluído (versão 1)

## Aplicação:
https://apirotas.herokuapp.com/api/v1/
## Tecnologias usadas:
<table>
  <tr>
    <td>Django</td>
    <td>Django RF</td>
    <td>Docker-Compose</td>
    <td>Postgres</td>
    <td>Heroku</td>
    <td>Pytest-django</td>

  </tr>
  <tr>
    <td>4.0.4</td>
    <td>3.13.1</td>
    <td> 3.3 </td>
    <td>11</td>
    <td>7.59</td>
    <td>4.5.2</td>

  </tr>
</table>

## Modelos
### Classe Local

Método para atribuir um local como exemplo.

### Classe Rota

Método para criar rotas entre os locais criados como exemplo.

Ao definir um local de origem "source" e um ponto de chegada "target",
é atribuido uma distância entre dois pontos em uma rota unidirecional.

## Testes

Vários testes unitários na pasta tests.py para assegurar
diversas funcionalidades:

#### - Teste para todos os locais.
#### - Teste para um local específico.
#### - Teste para confirmar 5 locais como exemplo.
#### - Teste para confirmar local inválido
#### - Teste para todas as rotas.

## Integração Contínua

Testes de integração com Github Actions e Heroku.

## Observação Importante

Teste prático na construção de uma API
com o Django Rest Framework e desenvolvido por Isaac Marquetti.

#### isaac.marquetti@gmail.com
#### https://www.linkedin.com/in/isaac-marquetti-6298a773/