
## Código para o servidor

# Import das dependências
import pickle  # Para carregar o modelo pré-treinado
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist


# Criamos uma instância da classe FastAPI, ela vai lidar com todas as funcionalidades do servidor
app = FastAPI(title='Predicting Wine Class')


# Classe para representar um vinho, com suas caracteristicas (dados)
class Wine(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float


# Classe para representar um lote de vinhos
# conlist impõe a restrição de tipo e tamanho dos itens
class WineBatch(BaseModel):
    batches: List[conlist(item_type=float, min_items=13, max_items=13)]


# Carrega o classificador na memória para que possa ser usado para previsão
# Esse decorator garante que a função seja executada na inicialização do servidor
@app.on_event("startup")
def load_clf():
    with open("/app/wine.pkl", "rb") as file:
        global clf  # tornamos a variável global
        clf = pickle.load(file)


# Função que realizará as previsões de um único vinho
# Ela será acionada quando for chamado o endpoit /predict e espera um objeto Wine
@app.post("/predict")
def predict(wine: Wine):

    # Converte dados para matriz numpy de 1 linha x 13 colunas
    data_point = np.array(
        [
            [
                wine.alcohol,
                wine.malic_acid,
                wine.ash,
                wine.alcalinity_of_ash,
                wine.magnesium,
                wine.total_phenols,
                wine.flavanoids,
                wine.nonflavanoid_phenols,
                wine.proanthocyanins,
                wine.color_intensity,
                wine.hue,
                wine.od280_od315_of_diluted_wines,
                wine.proline,
            ]
        ]
    )

    # previsão deve ser lançada em uma lista usando o método tolist (serializado)
    pred = clf.predict(data_point).tolist()
    pred = pred[0]
    print(pred)
    return {"Predição": pred}


# Função que realizará as previsões de um lote de vinhos
@app.post("/predict-batch")
def predict_batch(wine: WineBatch):
    batches = wine.batches
    np_batches = np.array(batches)
    pred = clf.predict(np_batches).tolist()
    return {'Predição': pred}
