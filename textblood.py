import TextBlob
import Translator
import spotipy

translator = Translator()
print("Analizando sentimiento de poesía...")
texto = ['Me gusta las flores', 
             "Mirar el mar en el cielo", 
             "Amaba y me encantaban los pajaros",
             "No odiaba el alma del paisaje",
            "Disfrutaba cada paso del dia"]
comentarios = []
contar = 0
for cont in range(len(texto)):
    traduccion = translator.translate(texto[contar], src='es', dest='en')
    comentarios.append(traduccion.text + "")
    contar = contar +1


positive_feedbacks = []
negative_feedbacks = []
for feedback in comentarios:
  feedback_polarity = TextBlob(feedback).sentiment.polarity
  if feedback_polarity>0:
    positive_feedbacks.append(feedback)
    continue
  negative_feedbacks.append(feedback)

punt = input("Inserta tu puntuacion: ")
#print("Evalúa lo que estás leyendo")
a = 1
b = 1
c = 1
d = 1
e = 1
#ev = (a+b+c+d+e)

new_punt = int(punt) 

if (new_punt <= 2 ): 

 
    print("Sentimiento negativo.") 
    print(negative_feedbacks)
else :
    
    print("Sentimiento positivo.")
    print(positive_feedbacks)
print("La poesia analizada tiene un sentimiento:")
    
    
    
    #spotify:track:6rqhFgbbKwnb9MLmUQDhG6

