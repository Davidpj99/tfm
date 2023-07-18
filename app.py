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
 Se le presentan dos alternativas. ¿Qué escenario
 preferiría tener?: 

a) Tener la seguridad de recuperar los 50.000€ como
 mínimo, pudiendo conseguir más dinero. 

b) Tener un 50% de posibilidades de obtener 70.000€ y
 un 50 por ciento de posibilidades de convertirse en 35.000€.''',
['a', 'b'],
)

# Pregunta 6
pregunta_6 = st.radio(
'''7. Elija uno de estos dos resultados: 

a) Una ganancia asegurada de 475€. 

b) Un 25% de posibilidad de ganar 2.000€ y un 75% de no
 ganar nada.''',
['a', 'b'],
)

# Pregunta 7
pregunta_7 = st.radio(
'''8. Su asesor financiero le presenta un plan para reequilibrar
 su cartera. Este reequilibrio requiere de una serie de cambios 
 potenciales, que incluso pueden implicar el desencadenamiento 
 de hechos desagradables para el cliente, pero son necesarios 
 para reajustar su cartera.
 ¿Qué acontecimiento es más probable?: 

a) Usted toma acción sobre la recomendación inmediatamente. 

b) Usted dice que "lo pensará" para hacer una revisión honesta y 
 volver a su asesor en una semana, pero en realidad se pondrá en
 contacto con su asesor en ese momento.

c) Dice que "lo pensará" y que se comunicará con su asesor en una
 semana. Probablemente no contactará con su asesor hasta dentro de
 tres meses porque tiende a angustiarse por hacer cambios 
 sustanciales en su cartera.''',
['a', 'b', 'c'],
)

# Pregunta 8
pregunta_8 = st.radio(
'''9. Su cartera de inversiones contiene bonos corporativos de
 cierta calidad. El bono le ha estado proporcionando ingresos constantes
 y está contento. Su asesor financiero analiza sus tenencias de bonos 
 y le recomienda que reemplace el bono corporativo por un bono municipal 
 de calidad comparable, estimando que obtendrá una mejor rentabilidad 
 después de impuestos y tasas sobre ganancias de capital. 
 Usted no se encuentra familiarizado con este bono municipal.
 ¿Cuál sería su reacción ante esta recomendación?: 

a) Vendería el corporativo y compraría el bono municipal. 

b) Mantendría las cosas como están.''',
['a', 'b'],
)

# Pregunta 9
pregunta_9 = st.radio(
'''10. Suponga que ha heredado una inversión totalmente líquida de
 una mina de oro sudafricana de su excéntrico tío Jim. Usted
 discute el activo con su asesor financiero, y concluye que su 
 cartera ya contiene suficiente oro y materias primas. Además, 
 añade que su herencia no es un activo diversificado y recomienda
 venderlo. ¿Qué sería más probable?:

a) Vendería, según lo recomendado por mi asesor financiero.

b) Mantendría el interés de la mina de oro, puesto que es una herencia
 y no me agradan los cambios.''',
['a', 'b'],
)

# Pregunta 10
pregunta_10 = st.radio(
'''11. Compra una acción a 50€. Sube a 60€ en unos pocos meses, y
 luego baja a 40€ tras unos meses después. No está seguro de lo que
 sucederá a continuación. ¿Cómo respondería a este escenario?:

a) Vendo por el miedo a que pueda caer más.

b) Mantengo posición con la esperanza de que suba hasta los 50€
 para salir de esa inversión.''',
['a', 'b'],
)

# Pregunta 11
pregunta_11 = st.radio(
'''12. En una escala del 1 al 3, siendo 3 - "totalmente de acuerdo",
 ¿cuánto está de acuerdo con lo siguiente?: Al pensar en vender
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

a) Todavía hay tiempo para que nieve, por lo que su
 pronóstico probablemente sea correcto.

b) Todavía puede haber tiempo para que nieve, pero puede
 que se haya equivocado en su pronóstico.

c) Su experiencia le dice que su pronóstico probablemente fue
 incorrecto porque la mayoría del invierno ha pasado; por lo tanto,
 es poco probable que nieve.''',
['a', 'b', 'c'],
)

# Pregunta 13
pregunta_13 = st.radio(
'''14. Cuando escucha noticias que implican un potencial negativo 
 para el precio de una inversión que posee,
 ¿cuál sería su reacción ante dicha información?:
 
a) Tiende a ignorar la información porque ya ha realizado la inversión,
 ya ha determinado que la empresa tendrá éxito.
 
b) Reevaluará su razonamiento para comprar acciones, pero
 probablemente mantendrá su pensamiento inicial, ya que
 opina que la empresa tendrá éxito.

c) Reevaluará su razonamiento para comprar acciones y
 decidirá, basado en una consideración objetiva de todos
 los hechos, qué hacer a continuación.''',
['a', 'b', 'c'],
)

# Pregunta 14
pregunta_14 = st.radio(
'''15. Suponga que realiza una inversión basada en su propia
 investigación. Un asesor le presenta información que
 contradice su creencia sobre dicha inversión. ¿Cómo respondería?:
 
a) No le hace caso. Se fía más de su investigación.
 
b) Pide que le dé argumentos para entender por
 qué su información contradice su creencia, aunque
 generalmente se decantará por su pensamiento.

c) Estudia sus argumentos y considera capaz de decantarse
 objetivamente por una de las dos opciones, sin que su propia
 investigación le condicione.''',
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

Loss_aversion_exp = '''- Evitar sobreexposición mediática para no enfocarse en el corto plazo.'''
Status_Quo_exp = '''- Realizar una reunión/llamada con el cliente cada 15 días
 para informarle de cómo está el mercado y cuáles son las oportunidades y tendencias
 que emergen.
 
 - Maximizar la diversificación de la cartera del cliente, para que no siienta que 
 "todos los huevos están en la misma cesta".'''
Efecto_Ancla_exp = '''- Utilizar la volatilidad a corto plazo para realizar rebalanceos
 sistemáticos mensualmente mientras se mantienen los objetivos a largo plazo.

- Realizar simulaciones de distintos escenarios (recesión, expansión, estanflación) para
 observar cómo se comportaría la cartera y que el cliente decida con qué nivel de riesgo
 se encuentra cómodo.'''
Conservadurismo_exp = ''''''
Loss_Conserv = '''- Establecer guías y reglas objetivas para comprar, vender o rebalancer la cartera,
 especialmente si las condiciones de mercado son más duras y requieren un enfoque sistemático.'''
Status_Conser = '''- Realizar un rebalanceo mensual y modificar la cartera si el gestor lo ve necesario.'''
Racional_exp = ''''''

solucion = ""

if (Sesgo_1 == "Loss_Aversion"):
    solucion += Loss_aversion_exp + "\n\n"

if (Sesgo_1 == "Loss_Aversion" or Sesgo_4 == "Conservadurismo"):
    solucion += Loss_Conserv + "\n\n"

if (Sesgo_2 == "Status_Quo"):
    solucion += Status_Quo_exp + "\n\n"

if (Sesgo_2 == "Status_Conserv" or Sesgo_4 == "Conservadurismo"):
    solucion += Status_Conser + "\n\n"

if (Sesgo_3 == "Efecto_Ancla"):
    solucion += Efecto_Ancla_exp + "\n\n"

if (Sesgo_4 == "Conservadurismo"):
    solucion += Conservadurismo_exp + "\n\n"

if (Sesgo_1 == "Racional" or Sesgo_2 == "Racional" or Sesgo_3 == "Racional" or Sesgo_4 == "Racional"):
    solucion += Racional_exp + "\n\n"


# Explicación de sesgos

Loss_aversion_cal = '''- El sesgo de Loss Aversion aparece cuando un cliente
 prefiere evitar las pérdidas a tener ganancias. Este sesgo implica que los
 inversores mantengan una inversión demasiado tiempo y, en ocasiones, desatar
 ventas precipitadas.'''
Status_Quo_cal = '''- Status Quo es un sesgo emocional que predispone a las
 personas a elegir una opción que ratifique lo conocido en lugar de opciones
 alternativas que podrían generar cambios. Este sesgo implica que los inversores
 cojan cariño a ciertas posiciones, manteniendo inversiones que no son adecuadas 
 en el momento. También aparece cuando los inversores no quieren hacer frente a 
 costes por cambiar la posición.'''
Efecto_Ancla_cal = '''- El Efecto Ancla es un sesgo cognitivo que aparece cuando
 las personas tienden a basar sus decisiones o valoraciones en una referencia
 inicial, llamada "ancla", incluso si esa referencia no es relavante o precisa.
 Por ejemplo: Un reloj cuesta 200€ y lo ponen de oferta al 50%. Puede que el
 reloj en dicho momento su valor real sea de 50€, pero al percibir una oferta
 del 50% pensamos que es un gran precio y por lo tanto, lo compramos.'''
Conservadurismo_cal = '''- El Conservadurismo aparece cuando las personas se
 aferran a sus puntos de vista anteriores o pronósticos con el objetivo de
 conocer nueva información. Este sesgo implica que un inversor pueda ser inflexible
 a la hora de presentar nueva información sobre sus inversiones, ocasionando una
 reacción tardía ante nueva información.'''
Racional_cal = '''- Un comportamiento Racional aparece cuando nuestros pensamientos
 se corresponden con la realidad, es decir, están basados en hechos o datos fiables
 y por lo tanto podemos realizar inversionas más objetivas.'''

Explicacion = ""

if (Sesgo_1 == "Loss_Aversion"):
    Explicacion += Loss_aversion_cal + "\n\n"

if (Sesgo_2 == "Status_Quo"):
    Explicacion += Status_Quo_cal + "\n\n"

if (Sesgo_3 == "Efecto_Ancla"):
    Explicacion += Efecto_Ancla_cal + "\n\n"

if (Sesgo_4 == "Conservadurismo"):
    Explicacion += Conservadurismo_cal + "\n\n"

if (Sesgo_1 == "Racional" or Sesgo_2 == "Racional" or Sesgo_3 == "Racional" or Sesgo_4 == "Racional"):
    Explicacion += Racional_cal + "\n\n"


#Botón para el cálculo

if st.button ("Enviar encuesta y obtener resultados"):
    if pregunta_1 == "":
        st.write (f"Primero debe de poner su nombre. Este campo es obligatorio.")
    else:
        st.write (f"{pregunta_1}, estamos encantados de darle la bienvenida" +
            " a la gestora. Con este cuestionario hemos analizado sus" +
            " sesgos cognitivos y emocionales y nuestro algoritmo ha" +
            " determinado qué haremos para evitar que estos sesgos" +
            " puedan afectar negativamente a su inversión. Por ello," +
            " desde la gestora recomendamos:\n\n"
            f" {solucion}\n\n Estas recomendaciones se realizan en función del sesgo" +
            " que usted, como inversor, ha obtenido como resultado de esta" +
            " encuesta. Los sesgos observados a lo largo de la encuesta han" +
            " sido los siguientes:\n\n"
            f"{Explicacion}")
    
    


    

    


