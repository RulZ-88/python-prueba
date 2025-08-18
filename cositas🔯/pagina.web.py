from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

# ------------------------
# INICIALIZAR LA BASE DE DATOS
# ------------------------
def init_db():
    conn = sqlite3.connect('base_datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            correo TEXT NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ------------------------
# RUTA PRINCIPAL
# ------------------------
@app.route('/')
def home():
    if 'usuario' in session:
        return render_template('home.html', usuario=session['usuario'])
    return redirect(url_for('login'))

# ------------------------
# LOGIN
# ------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        conn = sqlite3.connect('base_datos.db')
        cursor = conn.cursor()
        cursor.execute('SELECT contrasena FROM usuarios WHERE usuario = ?', (usuario,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado and check_password_hash(resultado[0], contrasena):
            session['usuario'] = usuario
            return redirect(url_for('home'))
        else:
            return 'Credenciales incorrectas'

    return render_template('login.html')

# ------------------------
# REGISTRO
# ------------------------
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        correo = request.form['correo']
        contrasena = generate_password_hash(request.form['contrasena'])

        try:
            conn = sqlite3.connect('base_datos.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (usuario, correo, contrasena) VALUES (?, ?, ?)',
                           (usuario, correo, contrasena))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except:
            return 'Error: el usuario ya existe.'

    return render_template('registro.html')

# ------------------------
# LOGOUT
# ------------------------
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

# ------------------------
# INICIO
# ------------------------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
