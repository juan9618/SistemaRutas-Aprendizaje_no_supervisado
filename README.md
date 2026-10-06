# SistemaRutas-Aprendizaje_no_supervisado
Proyecto de aprendizaje no supervisado aplicado a datos de transporte masivo.
Descripción

El proyecto utiliza un conjunto de datos con información de diferentes rutas de transporte, como distancia, tiempo, transbordos, congestión, demanda y hora pico.

Se utiliza el algoritmo K-Means para agrupar las rutas según sus características y encontrar grupos con comportamientos similares.

Archivos
rutas_transporte.csv: dataset utilizado para el análisis.
modelo_agrupamiento.py: código en Python para cargar los datos, prepararlos y realizar el agrupamiento.
README.md: descripción del proyecto.
Tecnologías utilizadas
Python
Pandas
Scikit-learn
Matplotlib
Modelo utilizado

Se utilizó K-Means con 3 grupos.

Las variables utilizadas fueron:

Distancia en kilómetros
Tiempo en minutos
Número de transbordos
Nivel de congestión
Demanda
Hora pico

Los datos fueron estandarizados antes de aplicar el algoritmo mediante StandardScaler.

Resultados

El modelo encontró tres grupos:

Grupo	Registros	Característica principal
0	6	Rutas cortas y rápidas
1	9	Rutas largas, congestionadas y con mayor demanda
2	5	Rutas de características intermedias

El grupo 1 presentó las rutas con mayor distancia, tiempo, congestión y demanda.

Ejecución

Para ejecutar el proyecto se necesitan las siguientes librerías:

pip install pandas matplotlib scikit-learn

Después, ejecutar:

python modelo_agrupamiento.py

El programa muestra los resultados del agrupamiento y genera una gráfica con los grupos encontrados.

Autor

Juan Moreno
