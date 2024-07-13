from flask import Blueprint
from controllers.predictController import index, predict

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/ping', methods=['GET'])(index)
blueprint.route('/predict', methods=['POST'])(predict)
