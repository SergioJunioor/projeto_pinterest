from fakepinterst import database, app
from fakepinterst.models import Usuario,Foto
 
with app.app_context():
    database.create_all()