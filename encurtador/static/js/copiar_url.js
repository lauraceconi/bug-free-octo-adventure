var btnCopiar = document.getElementById('copiarUrl')
if (btnCopiar) btnCopiar.addEventListener('click', copiar_url);

function copiar_url(e) {
    e.preventDefault();
    var url = document.getElementById('urlCurta');
    var textarea = document.createElement('textarea');
    textarea.value = url.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('Copy');
    textarea.remove();
}