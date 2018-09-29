# CV-Imageai
Steps to install 
1.- Descargar Anaconda
2.- Iniciar Anaconda Prompt
3.- crear un ambiente usando conda create -n retinanet python=3.6 anaconda
4.- activa el ambiente con el siguiente comando source activate retinanet
5.- Instala los paquetesde python necesarios con conda install tensorflow numpy scipy opencv pillow matplotlib h5py keras
6.- Installa la libreria de ImageAI con pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl 
7.- Descarga YOLO y anexalo al folder del proyecto desde https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
8.- Corre el comando python cam.py para utilizar el programa

Notas: Cambia la linea 110 camera = cv2.VideoCapture(1) donde 1 es la segunda camara integrada a la computadora, para usar la webcam integrada
de la laptop cambialo a 0
