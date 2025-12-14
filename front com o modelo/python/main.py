from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

modelo = joblib.load("modelo_preco.pkl")
scaler = joblib.load("scaler_preco_casas.pkl")

app = FastAPI(title="API de Predição de Preço de Casas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class CasaInput(BaseModel):
    tamanho_m2: float
    quartos: int
    banheiros: int
    ano: int
    
@app.post("/predict")
def predict_preco(dados: CasaInput):
    square_footage = dados.tamanho_m2 * 10.7639

    entrada = pd.DataFrame({
        "Square_Footage": [square_footage],
        "Num_Bedrooms": [dados.quartos],
        "Num_Bathrooms": [dados.banheiros],
        "Year_Built": [dados.ano]
    })

    entrada_scaled = scaler.transform(entrada)

    preco = modelo.predict(entrada_scaled)[0]

    return {
        "preco_estimado": round(float(preco), 2)
    }
