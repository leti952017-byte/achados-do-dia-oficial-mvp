from flask import Blueprint, jsonify

usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@usuarios_bp.route("/", methods=["GET"])
def listar_usuarios():
    return jsonify({
        "mensagem": "Rota de usuários funcionando"
    }), 200


@usuarios_bp.route("/<int:usuario_id>", methods=["GET"])
def consultar_usuario(usuario_id):
    return jsonify({
        "usuario_id": usuario_id
    }), 200
