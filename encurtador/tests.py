from django.test import TestCase, SimpleTestCase
from django.http import HttpResponseRedirect
from django.urls import reverse

from encurtador.models import URLCurta

class EncurtadorTestCase(TestCase):
    def setUp(self):
        """
        Cria os objetos
        """
        for i in range(100):
            URLCurta.objects.create(destino='https://www.globo.com/')

    def teste_redirecionamento(self):
        """
        Testa se o redireciamento está sendo feito
        para o endereço correto
        """
        urls = URLCurta.objects.all()
        for url_curta in urls:
            response = self.client.get(
                reverse('acessar_url', kwargs={
                    'slug': url_curta.slug
                    }
                ), follow=True)
            self.assertRedirects(
                response=response,
                expected_url=url_curta.destino
            )

    def teste_exclusao(self):
        """
        Testa a exclusão de uma URL
        """
        qtd_urls = URLCurta.objects.count()
        url_curta = URLCurta.objects.all()[0]
        self.client.get(reverse('excluir', kwargs={'pk': url_curta.pk}))
        self.assertEqual(
            qtd_urls - 1, 
            URLCurta.objects.count()
        )

    def teste_contador_de_acesso(self):
        """
        Testa o contador de acessos
        """
        url_curta = URLCurta.objects.all()[0]
        url_curta_acessos = url_curta.acessos
        self.client.get(reverse('acessar_url', kwargs={'slug': url_curta.slug}))
        update_url_curta = URLCurta.objects.get(pk=url_curta.pk)
        self.assertEqual(
            url_curta_acessos + 1, 
            update_url_curta.acessos
        )
