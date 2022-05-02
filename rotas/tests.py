from django.test import Client
import requests


def test_home_status_code(client: Client):
    """
    Teste status code 200 (OK), na página inicial.
    """
    resposta = client.get('/')
    assert resposta.status_code == 200


class TestLocal:
    url_base_local = 'http://127.0.0.1:8000/api/v1/local/'

    def test_get_locais(self):
        """
        Teste status code 200 (OK) para todos os locais.
        """
        locais = requests.get(url=self.url_base_local)
        assert locais.status_code == 200

    def test_get_local(self):
        """
        Teste status code 200 (OK) para um local específico.
        """
        local = requests.get(url=f'{self.url_base_local}1/')
        assert local.status_code == 200

    def test_get_registros(self):
        """
        Teste para confirmar 5 locais como exemplo.
        """
        registros = requests.get(url=self.url_base_local)
        assert registros.json()[-1]['id'] == 5

    def test_get_local_invalido(self):
        """
        Teste para confirmar que não há dados no id=6, retornando
        o erro 404 (Página não encontrada).
        """
        local = requests.get(url=f'{self.url_base_local}6/')
        assert local.status_code == 404


class TestRota:
    url_base_local = 'http://127.0.0.1:8000/api/v1/rota/'

    def test_get_rotas(self):
        """
        Teste status code 200 (OK) para todas as rotas.
        """
        rotas = requests.get(url=self.url_base_local)
        assert rotas.status_code == 200
