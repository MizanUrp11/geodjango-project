# geodjango-project
This is an improvement of my django project

    pip install virtualenv

    virtualenv lifeingis

    cd scripts

    activate

    pip install django==1.10.5

    pip install psycopg2==2.7

install_postgresql9.3_postgis2.1_ubuntu.md 
https://gist.github.com/hewerthomn/aa97dbf686a1c4f9ce49


    python manage.py ogrinspect Incidences/data/Boundary.shp areas --srid=4326 --mapping --multi


#Requirements

    astroid==1.6.6
    backports.functools-lru-cache==1.6.1
    configparser==4.0.2
    Django==1.10.5
    django-leaflet==0.25.0
    enum34==1.1.6
    futures==3.3.0
    isort==4.3.21
    lazy-object-proxy==1.4.3
    mccabe==0.6.1
    psycopg2==2.7
    pylint==1.9.5
    singledispatch==3.4.0.3
    six==1.13.0
    wrapt==1.11.2
