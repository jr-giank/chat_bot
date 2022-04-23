import re
import os
from chatbot import respuestas_bot

class chatbot:

    def respuesta(self, texto_usuario):
        self.texto_usuario = texto_usuario
        
        respuestas = respuestas_bot()

        mensaje_usuario = re.split(r'\s|[/\,-;:¿?_]\s*', self.texto_usuario.lower())
        
        respuesta = respuestas.mensajes_respuesta(mensaje_usuario)

        return respuesta


if __name__ == '__main__':
    
    bot = chatbot()
    os.system('cls')
    
    while True:
        print("Bot:", bot.respuesta(input('Tú: ')))
