from flask import Blueprint,request,jsonify,render_template
from sqlalchemy import exc
from models import Images
from app import db
from auth import tokenCheck
import base64

imagenuser = Blueprint('imagenuser',__name__,template_folder="templates")

def render_imagen(data):
    render_img = base64.b64encode(data).decode('ascii')
    return render_img

@imagenuser.route('/displayimage',methods=["GET"])
@tokenCheck
def search_page(usuario):
    search_image = Images.query.filter_by(user_id=usuario['user_id']).first()
    if search_image:
        image = search_image.rendered_data
        return render_template('perfilusuario.html',image=image)
    else:
        return jsonify({'message':'no image'})
    
@imagenuser.route('/uploadperfil',methods=["POST"])
@tokenCheck
def upload(usuario):
    search_image = Images.query.filter_by(user_id=usuario['user_id']).first()
    if search_image:
        file = request.files['inputFile']
        data = file.read()
        render_file = render_imagen(data)
        search_image.rendered_data = render_file
        search_image.data = data
        db.session.commit()
        return jsonify({'message':'imagen actualizada'})
    else:
        file = request.files['inputFile']
        print("checkpoint :D")
        data = file.read()
        print("checkpoint :D")
        render_file = render_imagen(data)
        newfile = Images()
        print("checkpoint :D")
        newfile.type = "Perfil"
        print("checkpoint :D")
        newfile.rendered_data = render_file
        print("checkpoint :D")
        newfile.data = data
        newfile.user_id=usuario['user_id']
        db.session.add(newfile)
        db.session.commit()
        return jsonify({"message":"Imagen agregada"})

