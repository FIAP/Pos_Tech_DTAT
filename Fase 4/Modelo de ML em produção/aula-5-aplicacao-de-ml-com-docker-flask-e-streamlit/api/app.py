from flask import Flask, request, jsonify, Response
from pydantic import BaseModel, ValidationError
import pickle

app = Flask(__name__)

# Carregar o pipeline do modelo treinado
pipeline_path = '/model_data/pipeline.pkl'
with open(pipeline_path, 'rb') as f:
    pipeline = pickle.load(f)

# Classe para validar as entradas
class InputData(BaseModel):
    RelativeCompactness: float
    SurfaceArea: float
    WallArea: float
    RoofArea: float
    OverallHeight: float
    Orientation: int
    GlazingArea: float
    GlazingAreaDistribution: int

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = InputData(**request.get_json())
        features = [[
            input_data.RelativeCompactness,
            input_data.SurfaceArea,
            input_data.WallArea,
            input_data.RoofArea,
            input_data.OverallHeight,
            input_data.Orientation,
            input_data.GlazingArea,
            input_data.GlazingAreaDistribution
        ]]
        prediction = pipeline.predict(features)
        status_code = 200
        status_message = Response(status=status_code).status
        return jsonify({
            "status": status_message,
            "data": {"prediction": prediction[0]}
        }), status_code

    except ValidationError as e:
        status_code = 400
        return jsonify({"error": e.errors()}), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
