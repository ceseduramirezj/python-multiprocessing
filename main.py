""" A diferencia de los hilos, los procesos son totalmente independientes entre sí, por lo tanto
no comparten memoria ni recursos, un proceso no afecta en nada a otro. Esto es una ventaja
para operaciones que requieren de mucho rendimiento (se consume mucha CPU). Por otro lado, los
hilos son adecuados para tareas que requieren de mucha E/S (entrada/salida), como por ejemplo
esperar la respuesta de un servidor, leer un archivo, etc. """
# Threading = concurrencia
# Multiprocessing = paralelismo
# A mas cores en el ordenador podemos ejecutar mas procesos en paralelo

from multiprocessing import Process, Queue, Pool, cpu_count
from functools import partial
from threading import Thread
import time

def check_number_of_values_in_range(comp_list, lower, upper):
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comp_list:
            number_of_hits += 1
    return number_of_hits

""" def check_value_in_list(x, i, number_of_processes, queue):
    max_number_to_check_to = 10**8
    lower = int(i * max_number_to_check_to / number_of_processes)
    upper = int((i + 1) * max_number_to_check_to / number_of_processes)
    number_of_hits = 0
    for i in range(10**8):
        i in x

    queue.put((lower, upper, number_of_hits)) """

def square(y, addition_component, x):
    return x ** y


num_processes = 4
comparison_list = [1, 2, 3]
lower_and_upper_bounds = [(0, 25*10**6), (25*10**6, 50*10**6), (50*10**6, 75*10*6), (75*10*6, 10**8)]
power_list = [4, 5, 6]
power = 3
addition_component = 2

#queue = Queue()

#start_time = time.time()

#Un pool te da un grupo de Procesos para utilizar
#Al terminar todos los procesos obtenemos un resultado aplicando una funcion a una entrada de dato

# Podemos ver el numero de cores que tiene la maquina
num_cpu_available = max(1, cpu_count() - 1)

print('Number of cpus being used:', num_cpu_available)
#print("num_cpi_available", num_cpu_available)

# Usamos la funcion partial para pasar argumentos a la funcion square, los primeros 2 argumentos
#partial_func = partial(square, power, addition_component)

prepared_list = []
#for i in range(len(comparison_list)):
#    prepared_list.append((comparison_list[i], power_list[i]))

for i in range(len(lower_and_upper_bounds)):
    prepared_list.append((comparison_list, lower_and_upper_bounds[i][0], lower_and_upper_bounds[i][1]))

print('List to use as input:', prepared_list)


with Pool(num_cpu_available) as mp_pool:
    #result = mp_pool.map(partial_func, comparison_list)
    #result = mp_pool.starmap(square, prepared_list)
    result = mp_pool.starmap(check_number_of_values_in_range, prepared_list)


print(result)
""" processes = []

for i in range(num_processes):
    t = Process(target=check_value_in_list, args=(comparison_list, i, num_processes, queue))
    processes.append(t)

for t in processes:
    t.start()

for t in processes:
    t.join()

queue.put('DONE')

while True:
    v = queue.get()
    if v == 'DONE':
        break
    lower, upper, number_of_hits = v
    print('Between', lower, 'and', upper, 'we have', number_of_hits, 'values in the list')

print('Everythin took:', time.time() - start_time, 'seconds') """