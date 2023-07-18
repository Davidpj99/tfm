import streamlit as st
import pandas as pd

# Pregunta 0
pregunta_0 = st.radio(
'''1. Supongamos que el perfil de riesgo del cliente
 es: 

a) Conservador. 

B) Moderado. 

C) Agresivo.''',
['a', 'b', 'c'],
)

# Pregunta 1
pregunta_1 = st.text_input('Nombre:',)

# Pregunta 2
pregunta_2 = st.number_input('Indique su edad:', step=1)

# Pregunta 3
pregunta_3 = st.number_input('Indique capital invertido:', step=1)

# Pregunta 4
pregunta_4 = st.radio(
'''5. Imagine que hace una inversión que cae un
 25% en los primeros seis meses y no está seguro
 de sí se recuperará. ¿Qué haría normalmente (NO lo
 que cree que haría). ¿Qué haría en realidad?: 

a) Vender en cuanto recupere lo perdido. 

b) Aunque recupere lo perdido, mantendré la posición
 arriesgándome a otra caída.''',
['a', 'b'],
)
    
# Pregunta 5
pregunta_5 = st.radio(
'''6. Suponga que hace un plan para invertir 50.000€.
 Eres presentado con dos alternativas. ¿Qué escenario
 preferirías tener?: 

a) Tener la seguridad de que recuperaré mis 50.000€ como
 mínimo, incluso si no lo hago hacer más dinero. 

b) Tener un 50% de posibilidades de obtener 70.000€ y
 un 50 por ciento de posibilidades de obteniendo 35.000€.''',
['a', 'b'],
)

# Pregunta 6
pregunta_6 = st.radio(
'''7. Elige uno de estos dos resultados: 

a) Una ganancia asegurada de 475€. 

b) Un 25% de posibilidad de ganar 2.000€ y un 75% de no
 ganar nada.''',
['a', 'b'],
)

# Pregunta 7
pregunta_7 = st.radio(
'''8. Su asesor financiero le presenta un plan para reequilibrar
 su cartera. Este reequilibrio requeriría que hiciera una serie
 de cambios sustanciales en su cartera, que incluso pueden implicar
 el desencadenamiento de hechos imponibles que no son agradables, pero son
 bastante necesarios para obtener su cartera donde debe estar.
 ¿Cuál de los siguientes es más probable?: 

a) Usted toma acción sobre la recomendación inmediatamente. 

b) Usted dice que "lo pensará" para hacer una revisión honesta y 
 volver a su asesor en una semana, y en realidad se pondrá en
 contacto con su asesor en ese momento.

c) Dices que 'lo pensarás' y te comunicarás con tu asesor en una
 semana y probablemente contactará con su asesor y puede
 que no por tres o seis meses porque tiende a angustiarse por hacer
 cambios sustanciales como este ejemplo.''',
['a', 'b', 'c'],
)

# Pregunta 8
pregunta_8 = st.radio(
'''9. Su cartera de inversiones contiene bonos corporativos de
 cierta calidad. El bono le ha estado proporcionando ingresos
 y usted está feliz con eso. Su asesor financiero analiza sus
 tenencias de bonos y recomienda que reemplace el bono corporativo
 con un bono municipal de calidad comparable, estimando que obtendrá
 una mejor rentabilidad después de impuestos y tasas sobre ganancias de
 capital. No estás familiarizado con este bono municipal.
 ¿Cuál es su respuesta más probable?: 

a) Venderé el corporativo y compraré el bono municipal. 

b) Mantendré las cosas como están.''',
['a', 'b'],
)

# Pregunta 9
pregunta_9 = st.radio(
'''10. Suponga que ha heredado una inversión totalmente líquida en
 un mina de oro sudafricana de tu excéntrico tío Jim. Usted
 discute el activo con su asesor financiero, y ella concluye
 que su cartera ya contiene suficiente oro y mercancías. Más
 importante, su herencia no es un activo diversificado. Su
 asesor recomienda venderlo. ¿Qué es mas probable que haga?:

a) Venderé, según lo recomendado por mi asesor financiero.

b) Mantendré el interés de la mina de oro, porque no me gusta vender o modificar cosas que la gente pasa y me deja.''',
['a', 'b'],
)

# Pregunta 10
pregunta_10 = st.radio(
'''11. Compra una acción a 50€. Sube a 60€ en unos pocos meses, y
 luego baja a 40€ por unos meses después. No está seguro de lo que
 sucederá a continuación. ¿Cómo responderías a este escenario?:

a) Vendo por el miedo a que pueda caer más.

b) Mantengo posición con la esperanza de que suba hasta los 50€
 para salir de esa inversión.''',
['a', 'b'],
)

# Pregunta 11
pregunta_11 = st.radio(
'''12. En una escala del 1 al 3, siendo 3 - "totalmente de acuerdo",
 ¿cuánto está de acuerdo con lo siguiente: Al pensar en vender
 una inversión, el precio que pagué es un factor importante que
 considero antes de tomar cualquier decisión: 
 
a) 1.

b) 2.

c) 3.''',
['a', 'b', 'c'],
)

# Pregunta 12
pregunta_12 = st.radio(
'''13. Suponga que vive en Baltimore, Maryland, y hace el siguiente
 pronóstico: "Creo que habrá un invierno con nieve este año".
 Además, suponga que, a mediados de febrero, se da cuenta de
 que no ha caído nieve. ¿Cuál es su reacción natural a esta
 información?: 

a) Todavía hay tiempo para que caiga mucha nieve, por lo que mi
 pronóstico probablemente sea correcto.

b) Todavía puede haber tiempo para un poco de nieve, pero puede
 que me haya equivocado en mi pronóstico.

c) Mi experiencia me dice que mi pronóstico probablemente fue
 incorrecto la mayoría del invierno ha pasado; por lo tanto,
 la cantidad acumulada de nieve no es probable que sea significativa.''',
['a', 'b', 'c'],
)

# Pregunta 13
pregunta_13 = st.radio(
'''14. Cuando escucha noticias que implica un potencial negativo 
 para el precio de una inversión que posee,
 ¿cuál es su natural reacción a esta información?:
 
a) Tiendo a ignorar la información porque ya he hecho elinversión,
 ya he determinado que la empresa tendrá éxito.
 
b) Reevaluaré mis razones para comprar las acciones, pero
 probablemente apegarme a él porque normalmente me atengo
 a mi determinación original de que una empresa tendrá éxito.

c) Reevaluaré mi razonamiento para comprar las acciones y
 decidiré, basado en una consideración objetiva de todos
 los hechos, qué hacer a continuación.''',
['a', 'b', 'c'],
)

# Pregunta 14
pregunta_14 = st.radio(
'''15. Supongamos que realizas una inversión basada en tu propia
 investigación. Un asesor te presenta información que
 contradice tu creencia sobre esta inversión. ¿Cómo responderías?:
 
a) No le hago caso. Me fío más de mi investigación.
 
b) Pido que me dé sus argumentos para entender por
 qué su información contradice mi creencia, aunque
 generalmente me decantaré por hacer caso a mi investigación.

c) Estudio sus argumentos y me considero capaz de decantarme
 objetivamente por una de las dos opciones, sin que mi propia
 investigación me condicione.''',
['a', 'b', 'c'],
)

#Guardar respuestas
Resultados = {
    "Respuestas" : [pregunta_0, pregunta_1, pregunta_2, pregunta_3,
                    pregunta_4, pregunta_5, pregunta_6, pregunta_7,
                    pregunta_8, pregunta_9, pregunta_10, pregunta_11,
                    pregunta_12, pregunta_13, pregunta_14]
}

#Definición Sesgos
Loss_aversion = Resultados["Respuestas"][4:7].count("a")/3

if (Loss_aversion > 0.5):
    Sesgo_1 = "Loss_Aversion"
else:
    Sesgo_1 = "Racional"

task_7 = Resultados["Respuestas"][7]

if (task_7 == "a"):
    six = 0
elif (task_7 == "b"):
    six = 1
else:
    six = 3

Status_Quo = Resultados["Respuestas"][8:10].count("b") * 4 + six

if (Status_Quo/12 > 0.5):
    Sesgo_2 = "Status_Quo"
else:
    Sesgo_2 = "Racional"

task_11 = Resultados["Respuestas"][11]

if (task_11 == "a"):
    ten = 0
elif (task_11 == "b"):
    ten = 1
else:
    ten = 3

Efecto_Ancla = Resultados["Respuestas"][10].count("b") * 4 + ten

if (Efecto_Ancla/8 > 0.5):
    Sesgo_3 = "Efecto_Ancla"
else:
    Sesgo_3 = "Racional"

task_12 = Resultados["Respuestas"][12]
task_13 = Resultados["Respuestas"][13]
task_14 = Resultados["Respuestas"][14]

if (task_12 == "a"):
    eleven = 3
elif (task_12 == "b"):
    eleven = 1
else:
    eleven = 0

if (task_13 == "a"):
    twelve = 3
elif (task_13 == "b"):
    twelve = 1
else:
    twelve = 0

if (task_14 == "a"):
    thirteen = 3
elif (task_14 == "b"):
    thirteen = 1
else:
    thirteen = 0

Tot_Cons = eleven + twelve + thirteen

if (Tot_Cons/12 > 0.5):
    Sesgo_4 = "Conservadurismo"
else:
    Sesgo_4 = "Racional"


# Recomendaciones en función de sesgo

Loss_aversion_exp = "Un aumento del peso en RV..."
Status_Quo_exp = "Una bajada de la RF..."
Efecto_Ancla_exp = "Un aumento en RV..."
Conservadurismo_exp = "Reducción de riesgo..."
Racional_exp = "Mantenemos los pesos de nuestra cartera..."

solucion = ""

if (Sesgo_1 == "Loss_Aversion"):
    solucion += Loss_aversion_exp + "\n"

if (Sesgo_2 == "Status_Quo"):
    solucion += Status_Quo_exp + "\n"

if (Sesgo_3 == "Efecto_Ancla"):
    solucion += Efecto_Ancla_exp + "\n"

if (Sesgo_4 == "Conservadurismo"):
    solucion += Conservadurismo_exp + "\n"

if (Sesgo_1 == "Racional" or Sesgo_2 == "Racional" or Sesgo_3 == "Racional" or Sesgo_4 == "Racional"):
    solucion += Racional_exp + "\n"


# Explicación de sesgos

Loss_aversion_cal = '''El sesgo de Loss_aversion aparece cuando...'''
Status_Quo_cal = '''Status_Quo es un sesgo...'''
Efecto_Ancla_cal = '''El efecto ancla aparece cuando...'''
Conservadurismo_cal = '''El conservadurismo es...'''
Racional_cal = '''Un comportamiento racional es aquel...'''

Explicacion = ""

if (Sesgo_1 == "Loss_Aversion"):
    Explicacion += Loss_aversion_cal + "\n"

if (Sesgo_2 == "Status_Quo"):
    Explicacion += Status_Quo_cal + "\n"

if (Sesgo_3 == "Efecto_Ancla"):
    Explicacion += Efecto_Ancla_cal + "\n"

if (Sesgo_4 == "Conservadurismo"):
    Explicacion += Conservadurismo_cal + "\n"

if (Sesgo_1 == "Racional" or Sesgo_2 == "Racional" or Sesgo_3 == "Racional" or Sesgo_4 == "Racional"):
    Explicacion += Racional_cal + "\n"


#Botón para el cálculo

if st.button ("Enviar encuesta y obtener resultados"):
    st.write (f" Buenas {pregunta_1} después de realizar las preguntas" +
            " y analizar como es su forma de pensar le recomendamos" +
            f" las siguientes actuaciones en su cartera: {solucion}\n\n"
            " Estas recomendaciones se realizan en función del sesgo" +
            " presentado por el inversor cuyo comportamiento implicará" +
            " diferencias a la hora de invertir entre varias personas." +
            " Los sesgos observados a lo largo de la encuesta han sido los siguientes:\n\n"
            f"{Explicacion}")
    
    


    

    


