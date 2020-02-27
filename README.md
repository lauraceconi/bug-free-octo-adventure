# Desafio de Código: Instruções de uso

### Requisitos

Os seguintes softwares são necessários para executar este projeto:
- Docker ([Instruções de instalação](https://docs.docker.com/install/linux/docker-ce/ubuntu/))
- Make

### Rodar a aplicação no navegador
1. Clonar o repositório `https://github.com/lceconi/bug-free-octo-adventure`
2. Acessar a pasta.
3. Executar o comando `make setup` e aguardar até o fim da criação da imagem do projeto.
4. Executar o comando `make run` e acessar o endereço `http://localhost:8000` no navegador.

### Rodar testes
1. Na pasta do projeto, executar o comando `make container`. Este comando abre uma instância interativa do container do projeto.
2. No terminal do container, executar o comando `make test`.
