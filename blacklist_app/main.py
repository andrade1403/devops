from blacklist_app import create_app

#Creamos app
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)
