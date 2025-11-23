import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
import pickle
import os

# Carregar o dataset Energy Efficiency
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx"
data = pd.read_excel(url)

# Separar as variáveis preditoras (X) e as variáveis alvo (y)
X = data.iloc[:, :-2]  # Todas as colunas exceto as duas últimas (Heating & Cooling Load)
y = data["Y1"]  # Carga de aquecimento ("Heating Load")

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o pipeline
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),  # Tratamento de valores ausentes
    ("scaler", StandardScaler()),  # Escalonamento
    ("model", RandomForestRegressor(random_state=42))  # Modelo
])

# Otimização de hiperparâmetros
param_grid = {
    "model__n_estimators": [50, 100, 200],
    "model__max_depth": [None, 10, 20],
    "model__min_samples_split": [2, 5, 10],
    "model__min_samples_leaf": [1, 2, 4],
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring="neg_mean_absolute_error",
    cv=3,
    verbose=2,
    n_jobs=-1
)

# Treinar e encontrar os melhores parâmetros
grid_search.fit(X_train, y_train)
print("Melhores Hiperparâmetros:", grid_search.best_params_)

# Avaliar no conjunto de teste
best_model = grid_search.best_estimator_
predictions = best_model.predict(X_test)
print("Erro Médio Absoluto (MAE):", mean_absolute_error(y_test, predictions))

# Salvar o modelo treinado
model_path = '/model_data/pipeline.pkl'
os.makedirs(os.path.dirname(model_path), exist_ok=True)
with open(model_path, 'wb') as f:
    pickle.dump(best_model, f)
print(f"Modelo salvo em {model_path}")
