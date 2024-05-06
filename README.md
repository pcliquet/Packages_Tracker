# md-proj-sql-template
Megadados - Projeto SQL - Template


# Projeto de Gerenciamento de Encomendas - FastAPI

Este projeto é uma aplicação FastAPI que implementa um sistema de gerenciamento de encomendas e histórico de localização. Nesta versão, integramos a aplicação com um banco de dados MySQL usando o ORM SQLAlchemy.

## Configuração do Ambiente

Para configurar e rodar a aplicação, siga os passos abaixo:

### Requisitos

- Python 3.8+
- MySQL
- Bibliotecas Python listadas em `requirements.txt`

### Instalação

1. **Clone o Repositório**:
   ```
   git clone https://github.com/insper-classroom/24-1-md-eng-proj-sql-projetosql_caio_vitor.git
   ```

2. **Crie um Ambiente Virtual**:
   ```
   python -m venv venv
   ```

3. **Ative o Ambiente Virtual**:
   - Windows:
     ```
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Instale as Dependências**:
   ```
   pip install -r requirements.txt
   ```

### Configuração do Banco de Dados

1. **Configuração de Variáveis de Ambiente**:
   - Crie um arquivo `.env` na raiz do projeto.
   - O arquivo `.env` deve incluir a seguinte variável de ambiente para definir a conexão ao banco de dados MySQL:

   ```
   DATABASE_URL=mysql://username:password@localhost/dbname
   ```

   **Observações**:
   - Substitua `username` pelo nome do usuário do banco de dados.
   - Substitua `password` pela senha do banco de dados.
   - Substitua `dbname` pelo nome do banco de dados que você criou.

2. **Criar o Banco de Dados**:
   - Crie um banco de dados no MySQL.
   - As tabelas serão geradas automaticamente ao iniciar a aplicação.

### Executar a Aplicação

1. **Inicie o Servidor**:
   ```
   uvicorn main:app --reload
   ```

2. **Acesse a Documentação**:
   - Acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para visualizar e testar os endpoints disponíveis através da interface interativa do Swagger.

### Diagrama ER

O diagrama de relacionamento das entidades (ER) pode ser encontrado no arquivo `diagrama_er.png` incluído no repositório.

### Vídeo de Demonstração

Confira o vídeo de demonstração das atualizações do Handout 02 no [link](url_do_video_aqui).
