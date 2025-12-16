import bentoml
import numpy as np
from bentoml import service, api

iris_model = bentoml.sklearn.get("iris_clf:latest")

@service(name="iris_classifier")
class IrisService:

    @api
    def classify(self, x: list[list[float]]) -> list[int]:
        model = iris_model.load_model()
        preds = model.predict(np.array(x))
        return preds.tolist()

#To run swagger ui --> cmd --> bentoml serve service:IrisService --reload