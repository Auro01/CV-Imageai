# CV-Imageai
Instalacion
###
1.- Descargar Anaconda
2.- crear un ambiente en anacaconda usando anaconda prompt
```
conda create -n retinanet python=3.6 anaconda
```
3.- activa el ambiente con el siguiente comando 
```
source activate retinanet
```
4.- Instala los paquetesde python necesarios
```
conda install tensorflow numpy scipy opencv pillow matplotlib h5py keras
```
5.- Installa la libreria de ImageAI
```
pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl 
```
6.- Descarga [YOLO](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5)  
7.- Corre el comando python cam.py para utilizar el programa

Notas: Cambia la linea 110 camera = cv2.VideoCapture(1) donde 1 es la segunda camara integrada a la computadora, para usar la webcam integrada
de la laptop cambialo a 0
