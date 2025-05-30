# Algoritmo de Puntos Más Cercanos - Demo Flask

Este proyecto es una aplicación web interactiva desarrollada con Flask, HTML, CSS y JavaScript. Permite visualizar y comparar tres algoritmos clásicos para encontrar el par de puntos más cercanos en un plano 2D: Fuerza Bruta, Divide y Vencerás, y K-D Tree. Los resultados se muestran tanto en una lista como gráficamente, incluyendo animaciones para cada algoritmo.

## Estructura del Proyecto

```
Algoritmo-de-Puntos-cercanos
├── app.py
├── templates
│   └── index.html
├── static
│   └── style.css
└── README.md
```

## Requisitos

- Python 3.x
- Flask
- scipy (para el método K-D Tree)

## Instrucciones de instalación

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd Algoritmo-de-Puntos-cercanos
   ```

2. Instala las dependencias necesarias:
   ```
   pip install Flask scipy
   ```

3. Ejecuta la aplicación:
   ```
   python app.py
   ```

4. Abre tu navegador y accede a [http://127.0.0.1:5000/](http://127.0.0.1:5000/) para ver la aplicación.

## Uso

- Genera puntos aleatorios y visualiza el par de puntos más cercanos.
- Observa la animación de cada algoritmo en su propio recuadro.
- Compara los resultados y el tiempo de ejecución de Fuerza Bruta, Divide y Vencerás y K-D Tree.
- Los resultados y tiempos de cada algoritmo se muestran uno al lado del otro para fácil comparación.
- Puedes personalizar el contenido y la apariencia modificando los archivos `index.html` y `style.css`.

---

**Nota:**  
Si tienes problemas con dependencias, asegúrate de tener instalado `scipy` para el método K-D Tree:

```
pip install scipy
```
