import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Cargar el dataset
df = pd.read_csv("rutas_transporte.csv")

print("Dataset cargado correctamente:")
print(df)

# Variables utilizadas para el aprendizaje no supervisado
variables = [
    "distancia_km",
    "tiempo_min",
    "transbordos",
    "congestion",
    "demanda",
    "hora_pico"
]

X = df[variables]

# Estandarizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Crear el modelo K-Means
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Realizar el agrupamiento
df["grupo"] = modelo.fit_predict(X_scaled)

# Mostrar los resultados
print("\nResultados del agrupamiento:")
print(df[variables + ["grupo"]])

# Mostrar cantidad de registros por grupo
print("\nCantidad de registros por grupo:")
print(df["grupo"].value_counts().sort_index())

# Mostrar características promedio de cada grupo
print("\nCaracterísticas promedio de cada grupo:")
promedios = df.groupby("grupo")[variables].mean()
print(promedios)

# Crear gráfica
plt.figure(figsize=(8, 5))

plt.scatter(
    df["distancia_km"],
    df["tiempo_min"],
    c=df["grupo"]
)

plt.xlabel("Distancia (km)")
plt.ylabel("Tiempo (min)")
plt.title("Agrupamiento de rutas de transporte masivo")
plt.colorbar(label="Grupo")

plt.tight_layout()
plt.show()
