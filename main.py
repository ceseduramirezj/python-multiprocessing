""" A diferencia de los hilos, los procesos son totalmente independientes entre sí, por lo tanto
no comparten memoria ni recursos, un proceso no afecta en nada a otro. Esto es una ventaja
para operaciones que requieren de mucho rendimiento (se consume mucha CPU). Por otro lado, los
hilos son adecuados para tareas que requieren de mucha E/S (entrada/salida), como por ejemplo
esperar la respuesta de un servidor, leer un archivo, etc. """

from multiprocessing import Process

