import random
import respuestas

class respuestas_bot:

    def mensajes_respuesta(self, mensaje):
        self.mensaje = mensaje
        
        respuesta_probable = {}

        def respuesta(respuesta_bot, lista_palabras, respuesta_simple = False, palabras_requeridas = []):
            nonlocal respuesta_probable
            respuesta_probable[respuesta_bot] = self.probabilidad_mensaje(self.mensaje, lista_palabras, respuesta_simple, palabras_requeridas)

        respuesta(respuestas.saludos[random.randrange(3)], self.palabras_clave('saludos'), respuesta_simple = True)
        respuesta(respuestas.sentir[random.randrange(4)], self.palabras_clave('sentir'), palabras_requeridas=['como'])
        respuesta(respuestas.bien[random.randrange(3)], self.palabras_clave('bien'), respuesta_simple= True)
        respuesta(respuestas.transporte[random.randrange(5)], self.palabras_clave('transporte'), respuesta_simple= True)
        respuesta(respuestas.pensum[random.randrange(3)], self.palabras_clave('pensum'), respuesta_simple= True)

        respuesta(respuestas.admision[random.randrange(2)], self.palabras_clave('admision'), respuesta_simple= True)
        respuesta(respuestas.economia[random.randrange(3)], self.palabras_clave('economia'), respuesta_simple= True)
        respuesta(respuestas.becas[random.randrange(4)], self.palabras_clave('becas'), respuesta_simple= True)
        respuesta(respuestas.certificaciones[random.randrange(3)], self.palabras_clave('certificaciones'), respuesta_simple= True)
        respuesta(respuestas.deportes[random.randrange(2)], self.palabras_clave('deportes'), respuesta_simple= True)
        respuesta(respuestas.residencia[random.randrange(3)], self.palabras_clave('residencia'), respuesta_simple= True)
        respuesta(respuestas.despedida[random.randrange(3)], self.palabras_clave('despedida'), respuesta_simple= True)

        match = max(respuesta_probable, key=respuesta_probable.get)

        return self.desconocido() if respuesta_probable[match] < 1 else match

    def probabilidad_mensaje(self, mensaje_usuario, palabras_reconocidas, respuesta_simple=False, palabras_requerida=[]):
        self.mensaje_usuario = mensaje_usuario
        self.palabras_reconocidas = palabras_reconocidas 
        self.respuesta_simple = respuesta_simple
        self.palabra_requerida = palabras_requerida
        
        certeza = 0
        hay_palabras_requeridas = True

        for palabra in self.mensaje_usuario:
            if palabra in self.palabras_reconocidas:
                certeza +=1

        porcentaje = float(certeza) / float (len(self.palabras_reconocidas))

        for palabra in self.palabra_requerida:
            if palabra not in self.mensaje_usuario:
                hay_palabras_requeridas = False
                break
        if hay_palabras_requeridas or self.respuesta_simple:
            return int(porcentaje * 100)
        else:
            return 0

    def desconocido(self):
        
        respuesta = ['No comprendo lo que quieres decir', 'No te entiendo muy bien', 'Lo siento, pero no te entiendo'][random.randrange(3)]
        return respuesta

    def palabras_clave(self, asunto):

        palabras = []

        with open(f"./comparaciones/{asunto}.txt", "r", encoding="utf_8") as file:
            for palabra in file:
                palabras.append(palabra.replace('\n', ''))

        return palabras
