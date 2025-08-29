from collections.abc import Iterable
from matplotlib_venn import venn2
import matplotlib.pyplot as plt


def practica_punto_1():
    # Cree un conjunto frutas con al menos 5 frutas.
    frutas = set({"Banana", "Kiwi", "Manzana", "Mora", "Maracuya"})

    # Agregue una fruta nueva.
    frutas.add("Sandia")

    # Elimine una fruta existente.
    frutas.discard("Kiwi")

    # Intente agregar un elemento repetido y muestre el conjunto final.
    frutas.add("Banana")
    print("Conjunto final de frutas:", frutas)


def practica_punto_2():
    # Cree 2 conjuntos
    estudiantes_matematicas = {"Ana", "Luis", "Carlos", "María"}
    estudiantes_fisica = {"Carlos", "María", "Sofía", "Pedro"}
    
    # Muestra los estudiantes que están en ambas clases.
    print("En ambas clases:", estudiantes_fisica.intersection(estudiantes_matematicas))
    
    # Muestra los estudiantes que están en matemáticas pero no en física.
    print("Solo en matemáticas:", estudiantes_matematicas.difference(estudiantes_fisica))

    # Muestra la unión de estudiantes.
    print("Unión de estudiantes:", estudiantes_matematicas.union(estudiantes_fisica))

    # Muestra los estudiantes que están solo en una de las dos clases.
    print("Solo en una clase:", estudiantes_fisica.symmetric_difference(estudiantes_matematicas))

    # ---------------------------
    # Diagramas de Venn 
    # ---------------------------
    venn = venn2(
        [estudiantes_matematicas, estudiantes_fisica],
        set_labels=("Matemáticas", "Física")
    )

    venn.get_label_by_id('10').set_text("\n".join(estudiantes_matematicas - estudiantes_fisica))  # Solo en Matemáticas
    venn.get_label_by_id('01').set_text("\n".join(estudiantes_fisica - estudiantes_matematicas))  # Solo en Física
    venn.get_label_by_id('11').set_text("\n".join(estudiantes_matematicas & estudiantes_fisica))  # En ambas

    plt.title("Diagrama de Venn: Estudiantes en Matemáticas y Física")
    plt.show()


def practica_punto_3():
    lista = [1, 2, 2, 3, 4, 4, 5]
    print("Lista sin duplicados:", eliminar_duplicados(lista))


def eliminar_duplicados(*s: Iterable[any]) -> list[any]:
    # Recibe una lista con elementos repetidos y devuelve una lista sin duplicados.
    return list(set().union(*s))


def practica_punto_4():
    # Pide al usuario que ingrese un párrafo de texto. Convierte el texto a minúsculas.
    parrafo = input("Ingrese su párrafo de texto: ").lower()
    
    # Elimina los signos de puntuación.
    puntuaciones = ".,();"
    parrafo = parrafo.translate(str.maketrans("", "", puntuaciones))

    # Guarda en un conjunto todas las palabras únicas
    words = set(parrafo.split())

    # Muestra el número de palabras únicas
    print("Cantidad de palabras únicas:", len(words))

    # Muestra la lista ordenada de palabras únicas
    print("Palabras ordenadas:", sorted(words))


if __name__ == "__main__":
    practica_punto_1()
    practica_punto_2()
    practica_punto_3()
    practica_punto_4()
