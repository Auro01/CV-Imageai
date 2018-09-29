from imageai.Detection import VideoObjectDetection
import os
import cv2
from collections import namedtuple
import sys

#Estructura auxiliar de rectangulos para realizar calculos de posicion
Rectangle = namedtuple('Rectangle', 'xmin ymax xmax ymin')

'''Funcion para detectar di dos rectangulos se empalman'''
def overlap(r1, r2):
    '''Checar si se empalman vertical y horizontal
    '''
    return range_overlap(r1.xmin, r1.xmax, r2.xmin, r2.xmax) and range_overlap(r1.ymax, r1.ymin, r2.ymax, r2.ymin)

def range_overlap(a_min, a_max, b_min, b_max):
    return not ((a_min > b_max) or (b_min > a_max))


'''Funcion que se ejecuta cada frame del video para realizar el calculo de silla
asi como desplegar el video en tiempo real'''
def forFrame(frame_number, output_array, output_count, frame):
    print("FOR FRAME " , frame_number)
    print("FOR FRAME " , output_array)

    #Variable auxiliar para contar la cantidad de rectangulos empalmados
    iCount = 0
    print("iCount = "+str(iCount))

    #por cada objecto detectado en el diccionario recibid
    for iteFirst in range(0,len(output_array)):
    	#Agarrar el primer objecto y guardardo en una variable auxiliar
    	a = output_array[iteFirst]
    	#di el objecto se llama "chair"
    	if(a["name"] == "chair"):
    		#creamos un rectangulo con los box points del objecto
	    	rect1 = Rectangle(a["box_points"][0], a["box_points"][1], 
	    			a["box_points"][2], a["box_points"][3])
	    	#recorremos el diccionario por segunda vez
	    	for iteSec in range(0,len(output_array)):
	    		#Aggaramos el primer objecto
	    		b = output_array[iteSec]
	    		#si el nombre del objecto es diferente al de a
	    		if (a["name"] != b["name"]):
	    			#creamos un segundo rectangulo
		    		rect2 = Rectangle(b["box_points"][0], b["box_points"][1], 
		    			b["box_points"][2], b["box_points"][3])
		    		#checamos si los rectangulos se empalman
		    		if(overlap(rect1,rect2)):
			    		#se emplmaron y subimos la cuenta en 1
			    		iCount+=1


    print("Output count for unique objects : ", output_count)

    #declaracion del tipo de letra para imprimir el numero de sillas
    font = cv2.FONT_HERSHEY_DUPLEX
    
    #si la cantidad de objectos diferentes es igual a 2
    if(len(output_count) == 2):
    	print(output_count["chair"] - iCount)
    	#si el calculo del total de sillas menos las empalmdas es myor a 0 
    	if(output_count["chair"] - iCount >= 0): 
    		#agregamos la cuenta de sillas vacias a la imagen
    		cv2.putText(frame,"Sillas desocupadas "+ str(output_count["chair"] - iCount) ,(10,25), font, .7 ,(0,240,0),2,cv2.LINE_AA)
    	else:
    		#si es menor a 0 agregamos numero de sillas = 0 a la imagen
    		cv2.putText(frame,"Sillas desocupadas "+ str(0) ,(10,25), font, .7 ,(0,240,0),2,cv2.LINE_AA)

        #desplegamos el frame actual
    	cv2.imshow('frame2',frame)
    	cv2.waitKey(1)
    	out.write(frame)

    	#mientras la tecla 'p' este oprimida pausamos en ese frame el video
    	while(0xFF == ord('p')):
    		cv2.putText(frame,"Pausa" ,(250,250), font, 2 ,(0,0,0),2,cv2.LINE_AA)
    		pass
    else:
    	#si la cantidad es diferente de 2
    	#checamos si existe la llave "chair" en el diccionario
    	if("chair" in output_count):
    	#agregamos la cantdidad de sillas al frame
    		cv2.putText(frame,"Sillas desocupadas "+ str(output_count["chair"] - iCount) ,(10,25), font, .7 ,(0,240,0),2,cv2.LINE_AA)
    	else:
    		#si no agragamos sillas desocupadad 0 al frame
    		cv2.putText(frame,"Sillas desocupadas "+ str(0) ,(10,25), font, .7 ,(0,240,0),2,cv2.LINE_AA)
    	
    	#mostramos el frame
    	cv2.imshow('frame2',frame)
    	cv2.waitKey(1)
    	out.write(frame)

    	#mientras la tecla 'p' este oprimida pausamos en ese frame el video
    	while(0xFF == ord('p')):
    		cv2.putText(frame,"Pausa" ,(250,250), font, 2 ,(0,0,0),2,cv2.LINE_AA)
    		pass

    #nos asegguramos que elvalor de cueta sea 0
    iCount = 0
    print("------------END OF A FRAME --------------")
    if(0xFF == ord('q')):
    	sys.exit()
    

execution_path = os.getcwd()


#le decimos a opencv que usaremos la camara de cierto index
camera = cv2.VideoCapture(1) 

#iniciamos el detector
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

#selecionamos cuales objectos queremos detectar
custom_objects = detector.CustomObjects(person=True, chair=True)


#variables para desplegar el video en tiempo real
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output-count2.avi',fourcc, 29.0, (640,480))

#funcion de la libreria imageai para detectar los objectos
video_path = detector.detectCustomObjectsFromVideo( save_detected_video = False, return_detected_frame=True, custom_objects=custom_objects, camera_input=camera,
                                output_file_path=os.path.join(execution_path, "camera_detected_91")
                                , frames_per_second=29, log_progress=True, per_frame_function = forFrame)
print(video_path)




