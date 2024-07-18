# personal_assistant
it's a final project of software python course

'''
    Щоб запустити локально сервер для розробки, достатньо виконати команду в консолі 

    python manage.py runserver

    знаходячись всередині папки проекту core
'''
    docker run --name personal_assistant -e POSTGRES_DB=assistant_db -e POSTGRES_USER=goit-project-user -e POSTGRES_PASSWORD=G4d8_p2ssw_049 -p 5432:5432 -d postgres

