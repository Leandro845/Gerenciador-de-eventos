Event Manager
Overview

This project is a practical simulation of an event manager, developed as part of the PythonFull course. It allows users to create events, manage participants, generate certificates, and perform various administrative tasks related to event management.
Features

    Create Events: Users can create new events specifying details such as name, description, dates, duration, logo, and color palette.
    Manage Events: Event creators can manage their events, including filtering events by name and viewing participants.
    Participant Registration: Users can register for events, and event organizers can view and manage participants.
    Certificate Generation: Organizers can generate certificates for event participants, individually or in bulk.
    Participant Certificates: Participants can view and download their event certificates.

Technologies Used

    Django: Python web framework for building web applications.
    Bootstrap: Front-end framework for responsive design.
    SQLite: Database management system used by Django for data storage.

Getting Started

To run this project locally, follow these steps:

    Clone the repository:

    bash

git clone https://github.com/your/repository.git
cd event-manager

Set up virtual environment (recommended):

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

bash

pip install -r requirements.txt

Run migrations to set up the database:

bash

python manage.py migrate

Create a superuser (admin) to access the admin interface:

bash

python manage.py createsuperuser

Start the development server:

bash

    python manage.py runserver

    Access the application in your web browser at http://127.0.0.1:8000/.

Contributing

Contributions are welcome! Please follow the standard guidelines:

    Fork the repository
    Create your feature branch (git checkout -b feature/AmazingFeature)
    Commit your changes (git commit -m 'Add some AmazingFeature')
    Push to the branch (git push origin feature/AmazingFeature)
    Open a pull request



## Em portugues



Este projeto é uma simulação prática de um gerenciador de eventos, desenvolvido como parte do curso PythonFull. Ele permite aos usuários criar eventos, gerenciar participantes, gerar certificados e realizar várias tarefas administrativas relacionadas ao gerenciamento de eventos.
Funcionalidades

    Criar Eventos: Usuários podem criar novos eventos especificando detalhes como nome, descrição, datas, duração, logotipo e paleta de cores.
    Gerenciar Eventos: Criadores de eventos podem gerenciar seus eventos, incluindo filtrar eventos por nome e visualizar participantes.
    Inscrição de Participantes: Usuários podem se inscrever em eventos, e organizadores de eventos podem visualizar e gerenciar os participantes.
    Geração de Certificados: Organizadores podem gerar certificados para os participantes do evento, individualmente ou em massa.
    Certificados dos Participantes: Participantes podem visualizar e baixar os certificados de seus eventos.

Tecnologias Utilizadas

    Django: Framework web em Python para construir aplicações web.
    Bootstrap: Framework front-end para design responsivo.
    SQLite: Sistema de gerenciamento de banco de dados utilizado pelo Django para armazenamento de dados.

Como Começar

Para executar este projeto localmente, siga os seguintes passos:

    Clone o repositório:

    bash

git clone https://github.com/seu/repositorio.git
cd gerenciador-de-eventos

Configure o ambiente virtual (recomendado):

bash

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:

bash

pip install -r requirements.txt

Execute as migrações para configurar o banco de dados:

bash

python manage.py migrate

Crie um superusuário (admin) para acessar a interface administrativa:

bash

python manage.py createsuperuser

Inicie o servidor de desenvolvimento:

bash

    python manage.py runserver

    Acesse a aplicação em seu navegador web em http://127.0.0.1:8000/.

Contribuições

Contribuições são bem-vindas! Por favor, siga as diretrizes padrão:

    Fork o repositório
    Crie sua branch de feature (git checkout -b feature/FuncionalidadeIncrivel)
    Commit suas mudanças (git commit -m 'Adiciona uma FuncionalidadeIncrivel')
    Push para a branch (git push origin feature/FuncionalidadeIncrivel)
    Abra um pull request
