from flask import Flask, render_template

# Inicializar
app = Flask( __name__)

# Rutas -- Paginas -- Funciones
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/warranty")
def warranty():
    return render_template("warranty.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")    

@app.route("/recoveracc")
def recoveracc():
    return render_template("recoveracc.html")

def page_not_found(error):
    return render_template("error.html")

# Inicio de la aplicacion
if __name__ == '__main__':
    app.run(debug=True,port=3000)