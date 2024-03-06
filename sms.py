# -*- coding: utf-8 -*-
import os
from twilio.rest import Client

def enviar_sms(numero, mensaje, sid, token, copilot_sid):
    client = Client(sid, token)

    try:
        mensaje_enviado = client.messages.create(
            body=mensaje,
            messaging_service_sid=copilot_sid,
            to=numero
        )

        print(f"SMS enviado correctamente al número {numero}. SID del mensaje: {mensaje_enviado.sid}")
        return True
    except Exception as e:
        print(f"Error al enviar SMS: {str(e)}")
        # Imprimir información adicional de Twilio si está disponible
        if hasattr(e, 'code'):
            print(f"Código de Error de Twilio: {e.code}")
        if hasattr(e, 'msg'):
            print(f"Mensaje de Error de Twilio: {e.msg}")
        return False

def main():
    # Obtener credenciales desde variables de entorno
    sid = os.environ.get("TWILIO_ACCOUNT_SID")
    token = os.environ.get("TWILIO_AUTH_TOKEN")
    copilot_sid = os.environ.get("TWILIO_COPILOT_SID")

    # Obtener información del usuario
    numero_destino = input("Ingresa el número de teléfono de destino (incluyendo el código de país): ")
    mensaje = input("Ingresa el mensaje que deseas enviar: ")

    # Enviar SMS al número de destino utilizando Twilio Copilot
    if enviar_sms(numero_destino, mensaje, sid, token, copilot_sid):
        print("\nSMS enviado correctamente. Espera unos momentos para recibirlo.")
    else:
        print("\nNo se pudo enviar el SMS.")

if __name__ == "__main__":
    main()
