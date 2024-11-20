import secrets
import smtplib
from email.mime.text import MIMEText

def recuperacion_contrasena(correo, codigo):
    
    remitente = "m4rcosw8@gmail.com"
    asunto = "Recuperación de Contraseña"
    cuerpo = f"Tu código de recuperación es: {codigo}"

    mensaje = MIMEText(cuerpo)
    mensaje["Subject"] = asunto
    mensaje["From"] = remitente
    mensaje["To"] = correo

    # Configuración del servidor SMTP
    servidor_smtp = "smtp.gmail.com"
    puerto = 587
    contraseña = "bbps mcev xmal jqzo"

    with smtplib.SMTP(servidor_smtp, puerto) as server:
        server.starttls()
        server.login(remitente, contraseña)
        server.sendmail(remitente, correo, mensaje.as_string())
        
# recuperacion_contrasena('kingplayjr@gmail.com')