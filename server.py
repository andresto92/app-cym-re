from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")
    
@app.route("/register_page")
def register_page():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def register_user():
    Raza = request.form["Raza"]
    Nombre = request.form["Nombre"]
    Apellido = request.form["Apellido"]
    Cumpleaños = request.form["Cumpleaños"]
    print(Raza, Nombre, Apellido, Cumpleaños)
    return "Registro completo"
    
@app.route("/consult_page")
def consult_page():
    return render_template("consult.html")

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8080'
    app.run(host, port)



