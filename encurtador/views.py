from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from encurtador.models import Encurtador
from encurtador.forms import EncutadorForm

def criar_url(request):
    form = EncutadorForm(request.POST or None)
    sucesso = False
    if request.method == 'POST':
        if form.is_valid:
            form = form.save()
            sucesso = True
    else:
        form = EncutadorForm()
    return render(request, 'encurtador/criar.html', {
        'form': form,
        'sucesso': sucesso
    })

def acessar_url(request, url_curta):
    reg_url_curta = get_object_or_404(Encurtador, url_curta=url_curta)
    return HttpResponseRedirect(reg_url_curta.destino)

def gerenciar(request):
    urls_curtas = Encurtador.objects.all()
    return render(request, 'encurtador/gerenciar.html', {
        'urls_curtas': urls_curtas
    })