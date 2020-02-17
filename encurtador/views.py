from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from encurtador.models import URLCurta
from encurtador.forms import URLCurtaForm

def criar_url(request):
    """
    Renderiza o formulário de geração da URL curta 
    e devolve a url criada
    """
    form = URLCurtaForm(request.POST or None)
    sucesso = False
    if request.method == 'POST':
        if form.is_valid():
            form = form.save()
            sucesso = True
    else:
        form = URLCurtaForm()
    return render(request, 'encurtador/criar.html', {
        'form': form,
        'sucesso': sucesso
    })

def acessar_url(request, slug):
    """
    Verifica a existência da URL curta
    e redireciona para a página de destino.
    Realiza a contagem de acessos às URLs
    """
    url_curta = get_object_or_404(URLCurta, slug=slug)
    url_curta.acessos += 1
    url_curta.save()
    return HttpResponseRedirect(url_curta.destino)

def gerenciar(request):
    """
    Apresentação de todas as URLs curtas já criadas
    """
    urls_curtas = URLCurta.objects.all().order_by('-data_criacao')
    return render(request, 'encurtador/gerenciar.html', {
        'urls_curtas': urls_curtas
    })

def excluir(request, pk):
    """
    View responsável pela exclusão das URLs curtas
    """
    url_curta = get_object_or_404(URLCurta, pk=pk)
    url_curta.delete()
    return HttpResponseRedirect(reverse('gerenciar'))