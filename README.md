# Twilio SMS Sender Script

Este script de Python utiliza la API de Twilio para enviar mensajes SMS a través de Twilio Copilot.

## Requisitos

- Python 3.x
- [Cuenta de Twilio](https://www.twilio.com/) (para obtener las credenciales y el SID de Copilot)
- Cuenta de Twilio Copilot con un servicio de mensajería configurado

## Instalación

1. **Clona este repositorio o descarga el archivo `sms.py`.**

    ```bash
    git clone https://github.com/tu_usuario/SMS.git
    ```

2. **Instala las dependencias ejecutando el siguiente comando:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configura las variables de entorno:**

    - `TWILIO_ACCOUNT_SID`: SID de tu cuenta Twilio.
    - `TWILIO_AUTH_TOKEN`: Token de autenticación Twilio.
    - `TWILIO_COPILOT_SID`: SID de tu servicio Twilio Copilot.

    Puedes configurar estas variables de entorno en tu sistema o crear un archivo `.env` en la raíz del proyecto y cargarlo antes de ejecutar el script.

4. **Ejecuta el script:**

    ```bash
    python sms_sender.py
    ```

## Configuración de Twilio Copilot

Asegúrate de tener un servicio de mensajería configurado en tu cuenta de Twilio Copilot antes de ejecutar el script. Obtén el SID del servicio y configúralo en las variables de entorno.

## Uso

1. **Ejecuta el script:**

    ```bash
    python sms_sender.py
    ```

2. **Ingresa el número de teléfono de destino (incluyendo el código de país).**
3. **Ingresa el mensaje que deseas enviar.**
4. **El script intentará enviar el SMS y te proporcionará el SID del mensaje si es exitoso.**

## Contribuciones

Si encuentras problemas o deseas contribuir, ¡siéntete libre de abrir un problema o enviar un pull request!

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
