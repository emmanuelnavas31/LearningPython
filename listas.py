def listas():
    numeros = [1, 0, 6, 7, 9]
    print("Lista = ", numeros, type(numeros))

    task = ['tarea1', 'tarea2', 'tearea3']
    print("tareas ", task)

    types = [1, True, 'Hola']
    print(f"Types = {types}")

    print("numeros: ", numeros[2])
    print("Task: ", task[2])

    task[0] = 'Aprender'
    print("Task: ", task)
    print(f"Existe un true dentro de types= {True in types}")
    print(f"Existe un hola dentro de types= {'Hola' in types}")

    """
        Metodos de las listas
        CRUD
        C: Create
        R: Read
        U: Update
        D: Delete
        
    """
    numbers = [1,2,3,4,5]
    print(f"Numbers = {numbers}")
    numbers[-1] = 10
    print(f"Numbers = {numbers}")
    numbers.append(6)
    print(f"Numbers = {numbers}")
    numbers.insert(0, 'hola') # Posicion, elemento
    print(f"Numbers = {numbers}")
    numbers.insert(3, 'mundo')
    print(f"Numbers = {numbers}")

    # unificacion de listas

    task2 = ['todo1', 'todo2', 'todo3']
    newlist = task + task2
    print("newlist ", newlist)
    #Saber que posicion esta un elemento
    index = newlist.index('todo1')
    newlist[index] = 'Harold'
    print("newlist ", newlist)

    # Eliminacion de lementos de las listas

    newlist.remove('tarea2')
    print("newlist ", newlist)

    # Eliminando el ultimo elemento de la lista
    newlist.pop()
    print("newlist ", newlist)

    newlist.pop(0)
    print("newlist ", newlist)

    # Giremos un array
    newlist.reverse()
    print("newlist ", newlist)

    # metodo de ordenamiento
    numbers = [1,2,5,9,2,4,2]
    numbers.sort()
    print("Sort ", numbers)

    letras = ['m','e','s','g','t','a','b']
    letras.sort()
    print("Sort ", letras)

    

if __name__ == '__main__':
    listas()
