import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

puntaje = 0

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Se genera una lista que contenga 3 de las preguntas,respuestas posibles y respuesta correcta de manera que no haya preguntas repetidas
questions_to_ask = random.sample(
    list(zip(questions, answers, correct_answers_index)), k=3
)

# El usuario deberá contestar 3 preguntas
for question, options, answer in questions_to_ask:
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
        except ValueError:
            print("Respuesta no válida. Debe ingresar un número entero.")
            sys.exit(1)
        if user_answer < 0 or user_answer > 3:
            print(f"Respuesta no válida. Debe ingresar un numero entre 1 y 4")
            sys.exit(1)
        # Se verifica si la respuesta es correcta
        if user_answer == answer:
            print("¡Correcto!")
            puntaje += 1
            break
        else:
            print("Incorrecto.")
            puntaje -= 0.5

            # Si es el segundo intento, se muestra la respuesta correcta
            if intento == 1:
                print("La respuesta correcta es:")
                print(options[answer])

    # Se imprime un espacio en blanco al final de la pregunta
    print()

# Imprimir puntaje
if puntaje < 0:
    puntaje = 0
print(f"El puntaje final es {puntaje}")
