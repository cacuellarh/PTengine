from email import message
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from screen.Services.Console_info import Console
from screen.Interfaces.Inotification import Inotification


class Email(Inotification):
    
    server_smtp = 'smtp.gmail.com'
    port_smtp = 587
    user_smtp = 'noreply.trackmyprice@gmail.com'
    password_smtp = 'xnekzcxhzpidbohm'
    _destiny = ""
    _body = ""
    _affair = ""
    
    def conf(self, params):
        
        self._body = params.get("body", "")
        self._destiny = params.get("destiny", "")
        self._affair = params.get("affair", "")
        
        Console.info(f"Cargando datos de correo {self._body}, {self._destiny},{self._affair}")
    
    def notify(self):
        
        try:
            conexion_smtp = smtplib.SMTP(self.server_smtp, self.port_smtp)
            conexion_smtp.starttls()
            # Iniciar sesión en el servidor SMTP
            conexion_smtp.login(self.user_smtp, self.password_smtp)

            # Construir el mensaje
            message = MIMEMultipart()
            message['From'] = self.user_smtp
            message['To'] = self._destiny
            message['Subject'] = self._affair

            # Agregar el cuerpo del mensaje
            message.attach(MIMEText(''.format(self._body), 'html'))
            # Enviar el mensaje
            errs = conexion_smtp.sendmail(self.user_smtp, self._destiny, message.as_string())


        except Exception as e:
            Console.warning(f"Error al enviar correo de token: {e}")
        finally:
            
            conexion_smtp.quit()    


        
        


    