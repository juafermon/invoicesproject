import subprocess

librerias = ['pyqt5', 'jinja2 ', 'xhtml2pdf', 'psycopg2-binary']

for libreria in librerias:
    try:
        subprocess.check_call(['pip', 'install', libreria])
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar {libreria}: {e}")