print("TEST GATUNO: ¿Qué gato eres? (Responde con A, B, C o D)")
a = 0
b = 0
c = 0
d = 0
print("1. ¿Qué haces cuando suena la alarma?\n")
print("A. La apagas y sigues durmiendo")
print("B. Revisas el celular/PC")
print("C. La pospones")
print("D. Te despiertas de inmediato")

respuesta = input("Respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

print("\n2. ¿Cuál es tu plan perfecto de fin de semana?\n")
print("A. Dormir hasta tarde y quedarme en casa")
print("B. Jugar videojuegos")
print("C. Salir sin rumbo")
print("D. Ver a mis amigos o ir a una fiesta")
respuesta = input("Respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

print("\n3. ¿Cuál es tu mayor red flag?")
print("A. Me desaparezco por días")
print("B. Adivino cosas que no debería saber")
print("C. Digo las cosas sin pensarlo")
print("D. Me río en malas situaciones")
respuesta = input("Respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

print("\n4. ¿Cómo prefieres comunicarte?")
print("A. Por mensajes")
print("B. Con memes, reels o stickers")
print("C. Cara a cara")
print("D. Llamadas o mensajes de voz largos")
respuesta = input("Tu respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

print("\n5. ¿Qué actividad describe mejor tu día a día?")
print("A. Dormir, comer, repetir")
print("B. Estudiar, hacer trabajos")
print("C. Juzgar a la gente en redes")
print("D. Salir a pasear")
respuesta = input("Tu respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

print("\n6. ¿Qué harías si alguien te escribe 'tenemos que hablar'?")
print("A. Duermo una siesta y finjo que no lo vi.")
print("B. Busco los chats antiguos para tener pruebas.")
print("C. Contesto: “¿qué paso ahora?”")
print("D. Le mando 4 notas de voz, un sticker y digo “qué serio”.")
respuesta = input("Tu respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

print("\n7. ¿Qué haces en un grupo de WhatsApp?")
print("A. Leo todo y nunca respondo.")
print("B. Reacciono con un emoji y hago captura por si acaso.")
print("C. Contesto una vez y silencio el grupo.")
print("D. Contesto todo.")
respuesta = input("Tu respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

print("\n8. ¿Qué emoji usarías para describirte?")
print("A. 🫠")
print("B. 🤓")
print("C. 🙄")
print("D. 😛")
respuesta = input("Tu respuesta: ")
if respuesta == "A" or respuesta == "a":
    a += 1
elif respuesta == "B" or respuesta == "b":
    b += 1
elif respuesta == "C" or respuesta == "c":
    c += 1
elif respuesta == "D" or respuesta == "d":
    d += 1

gato_dormilon = """
GATITO DORMILÓN - 80% siestas 20% pensamientos funcionales

∩――――∩
||    /'　 /|
||   (  ´ ｰ`) ZZzz
|ﾉ^⌒⌒づ`￣  ＼
(　ノ　　⌒ ヽ ＼
＼　　||￣￣￣￣￣||
　 ＼,ﾉ||  

Tu verdadera pasión es el descanso. Eres paz con patitas, por lo que evitas los dramas. 
Eres algo reservado y selectivo con tus amigos, pero muy fiel.
"""

gato_hacker = """
GATITO HACKER — 1010101% sospechoso.

     /\_/|     
    (= ᵥ ᵥ =)
    /  >💻< ¨
   /  /     \ 
  (/       \_)

Eres un verdadero gato LICC! Eres observador, analítico y un poco misterioso.
Eres experto en leer ambientes y chats grupales que no contestarás. 

"""

gato_hater = """
GATO hater — 100% quejas.

   /ᐠ — ᐟ\ 
 (  >д<) 💢       
  ૮ …….. Ⳋ ˎˊ˗
  
Eres el gato que aparece, mira con desaprobación y se va sin decir nada.  
No te agrada casi nadie, y no haces esfuerzo por ocultarlo, pero eres honesto, muy leal y logras agradarle a la gente.
"""

gato_fiesta = """
GATO FIESTA - 120% volumen, 0% autocontrol.

     /\_ /\    
    ( ･ ω ･)つ
   / >🎈  
  //     \

Eres alguien muy extrovertido y sensible al aburrimiento. 
Una junta no es lo mismo sin tu presencia, y siempre traes luz contigo.
"""

if a == b == c == d:
    print("ERES... ¿un perro?")
    print("""
        .-"-.
       /|6 6|\       "WOOF... Digo, MIAU"
      {/(0)\}
       / ^ \
      (/ /^\ \)-'
       ""' '""

Eres un perro infiltrado! Intentaste encajar pero algo no cuadró, tu emoción y alegría demuestran tu verdadera identidad.

""")
else:
    print("\nResultado:")
    if a >= b and a >= c and a >= d:
        print(gato_dormilon)
    elif b >= a and b >= c and b >= d:
        print(gato_hacker)
    elif c >= a and c >= b and c >= d:
        print(gato_hater)
    else:
        print(gato_fiesta)