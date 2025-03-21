import random

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
    ("=", "==", "!=", "==="),4
]

correct_answers_index = [1, 2, 0, 3, 1]

Puntaje = 0 

questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)


for question, answer, correct_answer_index in questions_to_ask:  
        
    print(question)
    for i, options_answers in enumerate(answer):
        print(f"{i + 1}. {options_answers}")
    for intento in range(2):
        try:
            user_answer = int((input("Respuesta: "))) - 1
            if user_answer <= 4:
                if user_answer == correct_answer_index:
                    print("¡Correcto!")
                    Puntaje += 1 
                    break
            else: 
                print("Respuesta no valida")    
        except ValueError or TypeError:
            print("Respuesta no valida") 
    else:
        print("Incorrecto. La respuesta correcta es:")
        print(answers[answers.index(answer)][correct_answer_index])
        Puntaje -= 0.5 

    print()

print("Tu puntaje final fue:", f"{Puntaje}")