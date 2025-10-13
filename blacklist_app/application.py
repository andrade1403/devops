from blacklist_app import create_app

#Creamos app
application = create_app()

if __name__ == '__main__':
    application.run(port = 5000, debug = True)
