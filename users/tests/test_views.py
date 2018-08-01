from django.urls import reverse
from django.test import TestCase, Client
from model_mommy import mommy


class TestProfileView(TestCase):
    def setUp(self):
        super().setUp()
        # O `prepare` instancia, mas não salva. Precisamos disso
        # para poder trocar a senha do usuário e aí sim salvá-lo.
        self.user = mommy.prepare('users.User', username='test_user')
        self.user.set_password('test_password')
        self.user.save()

        # Cria um Client logado para testarmos views
        # que precisam de um usuário logado
        self.logged_user = Client()
        self.logged_user.login(username=self.user.username, password='test_password')

        # Definimos as variáveis para facilitar os testes
        self.view_url = reverse('users:profile', args=[self.user.pk])

    def test_request_method_200(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_view_loads_correct_user(self):
        user = mommy.make('users.User')
        # Criamos uma nova view_url aqui porque vamos
        # testar algo específico: se o usuário criado
        # na linha acima está sendo carregado corretamente
        view_url = reverse('users:profile', args=[user.pk])
        response = self.client.get(view_url)
        user_in_context = response.context_data.get('profile')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_in_context, user)