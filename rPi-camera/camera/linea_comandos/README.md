# Linea de comandos



```bash
man raspistill
```




```bash
raspistill --help
```
https://www.raspberrypi.com/documentation/computers/camera_software.html


usage: raspistill [options]


|Acción|Sintaxis ```[options]```|Descripción|
|---|---|---|
|Nombra el archivo de salida|`--output, -o <filename>`|Especifica el nombre del archivo de salida (`<filename>`). Si no es especificado el archivo no es guardado. Si el nombre es `'-'`, entonces todas las salidas seran enviadas a stdout.|
|Verbose|`--verbose, -v `|Muestra mensajes de debugging/information durante la ejecución del programa|
|Ancho de la imagen|`--width, -w  <size>`|Asigna un ancho de `<size>` a la imagen|
|Alto de la imagen|`--height, -h  <size>`|Fija la altura de la imagen en `<size>`|
|Calidad de la imagen|`--quality, -q  <0 to 100>`|Asigna a la imagen un valor de calidad entre 0 y 100. El valor de  100 es una calidad casi sin comprimir, sin embargo, 75 es en general un buen valor.
|Timeout|`--timeout,-t  <time>`|El programa se ejecutará durante el tiempo `<time>`, entonces tomará la captura (si el valor de `<time>` es especificado). Si este parámetro o es especificado, este será fijado a 5 segundos.|
|Timelapse|`--timelapse, -tl <time-lapse>`|El valor especificado en `<time-lapse>` es el tiempo entre capturas en milisegundos. Usted deberá especificar en formato `%04d` en el nombre del archivo donde usted desea que el frame count number aparezca. </br> </br> `-t 30000 -tl 2000 -o image%04d.jpg`</br></br>Así por ejemplo, el código de abajo producirá una captura cada 2 segundos, sobre un periodo total de 30 segundos, llamando las imágenes image0001.jpg, image0002.jpg y asi sucesivamente hasta la image0015.jpg.|
|Latest|`--latest, -l <filename>`|Asocia el ultimo frame de la imagen al nombre `<filename>`|
|Frame start|`--framestart, -fs`|Almacena el numero del primer frame.|
||`--datetime,    -dt`|Nombre los archivos con la fecha y la hora|
|Timestamp|`--timestamp, -ts`| Usa marcas de tiempo para nombrar los archivos.
|thumb|`--thumb,  -th <x:y:quality>`| Establece parametros en miniatura de acuardo al formato `<x:y:quality>`, el valor por defecto es (64:48:35)|
|encoding|`--encoding, -e <format>`| Define la codificación usada para el archivo de salida definido en `<format>` el cual puede ser jpg, bmp, gif, y png.|
|keypress|`--keypress,    -k `|Modo keypress
|fullpreview|`--fullpreview, -fp`| Modo full screen preview|
|burst|`--burst,    -bm`|Modo de captura en rafaga|
|Demo|`--demo, -d  <ms>`|Ejecuta el modo demo por `<ms>`|

## Ejemplos

1. Tomar una captura por default (con la resolución más alta) después de 2s (el tiempo es especificado en milisegundos). Guarde la imagen como image_ex1.jpg:
   
   ```
   raspistill -t 2000 -o image_ex1.jpg
   ```

2. Tomar una captura con una resolución de 640 x 480. Guarde la imagen como image_ex2.jpg:
   
   ```
   raspistill -t 5000 -o image_ex2.jpg -w 640 -h 480
   ```

3. Tomar una captura reduciendo la calidad considerablemente para reducir el tamaño del archivo. Guarde la imagen como image_ex3.jpg:
   
   ```
   raspistill -t 2000 -o image_ex3.jpg -q 5
   ```

4. Forzar a que la preview aparezca en el sistema coordenado 100,100, con 300 pixeles y 200 pixeles de alto. Guarde la imagen como image_ex4.jpg:
   
   ```
   raspistill -t 2000 -o image_ex4.jpg -p 100,100,300,200
   ```

5. Deshabilite la preview enteramente. Guarde la imagen como image_ex5.jpg:

   ```
   raspistill -t 5000 -o image_ex5.jpg -n
   ```

6. Guarde la imagen como un archivo PNG (lossless compression, pero mas lento que el JPEG). Guarde la imagen como image_ex6.jpg:
   
   ```
   raspistill -t 5000 -o image6.png -e png
   ```

7. Agregue alguna información EXIF JPEG asignando la Artist tag name a Boris, y la altitud del GPS a  123.5m.  Guarde la imagen como image_ex7.jpg.

   ```
   raspistill -t 5000 -o image_ex7.jpg -x IFD0.Artist=Boris -x GPS.GPSAltitude=1235/10
   ```

8. Tome cada 5 segundos una imagen durante 1 minutos  (1min = 60s = 60000 ms), llame las imagenes image_num_001_today.jpg, image_num_001_today.jpg y así sucesivamente con la ultima imagen disponible también bajo el nombre de latest.jpg.
    
   ```
   raspistill -t 60000 -tl 5000 -o image_num_%03d_today.jpg -l latest.jpg
   ```

9. Tome una captura y envíela a stdout.

   ```
   raspistill -t 2000 -o -
   ```

10. Tome una captura y envíela la imagen a un archivo.  Guarde la imagen como my_file.jpg.
    
    ```
    raspistill -t 2000 -o -> my_file.jpg
    ```

11. Corra la cámara por siempre y tome una foto cuando enter sea presionado: Guarde la imagen como my_pics#.jpg donde # es el numero de la fotografía tomada

    ```
    raspistill -t 0 -k -o my_pics%02d.jpg
    ```




