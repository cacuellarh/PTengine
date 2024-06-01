from celery import shared_task
from screen.Services.Notification.SelectorNotification import SelectorNotification
from screen.Services.Auto_validate import Validate
from screen.Services.Notification.SelectorNotification import SelectorNotification
from django.core.serializers import deserialize
from screen.Services.Console_info import Console
from django.conf import settings
from django.core.serializers import serialize
from screen.DB.Repos.Image_repos import Image_repos
import logging

# celery -A bosquejo worker -Q email_queue -l info
base = settings.PATHS["base_url"]
ImageRoutinPath = settings.PATHS["ImageRoutes"]
@shared_task(queue="validate_queue")
def validate(img):
    notify = SelectorNotification()
    notify.select_notification("email")
    html = " "
    validate = Validate()
    for obj in deserialize("json", img):
        ins = obj.object
        Console.important(f"Iniciando scaneo proceso:{ins.id_image}")
        prices = validate.aut_validate(ins)
    
        # Verificar si prices es None antes de acceder a sus elementos
        if prices is not None:
            current = prices.get("current_price")
            db = prices.get("db_price")
                
            Console.info(f"{current}, {db}")
            html = '''
        
            <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notificación de cambio de precio</title>
    <style type="text/css">
        *,
        html,
        body,
        div,
        span,
        applet,
        object,
        iframe,
        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        p,
        blockquote,
        pre,
        a,
        abbr,
        acronym,
        address,
        big,
        cite,
        code,
        del,
        dfn,
        em,
        font,
        img,
        ins,
        kbd,
        q,
        s,
        samp,
        small,
        strike,
        strong,
        sub,
        tt,
        var,
        b,
        u,
        i,
        center,
        dl,
        dt,
        dd,
        ol,
        ul,
        li,
        fieldset,
        form,
        label,
        legend,
        table,
        caption,
        tbody,
        tfoot,
        thead,
        tr,
        th,
        td,
        tr,
        select,
        input {
            appearance:inherit; 
            -moz-appearance:inherit; 
            -webkit-appearance:inherit; 
            background:transparent; 
            border:none; 
            border-radius:0; 
            box-sizing: border-box; 
            margin:0; 
            outline:0; 
            padding:0; 
            text-decoration:none;
            list-style: none;
            font-family: var(--main_font);
            color: inherit;
        }
        :root {
            /* Tamaño objetos */
            font-size: 15px;
            /* ===== Variables de fuentes ===== */
            --main_font: 'Poppins', sans-serif;
        }
        body {
            font-family: var(--main_font);
        }
        .container {
            width: 100%;
            height: 100vh;
            background-color: #f0f0f0;        
        }
        .main {
            width: 50rem;
            margin: 0 auto;
        }

        table {
            background-color: #ffffff;
            border-radius: 5px;
            padding: 2rem;
        }

        table tr {
            text-align: center;
        }

        h1 {
            font-size: 2rem;
            text-align: center;
            margin-bottom: 1rem;
        }
        p {
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }
        img {
            height: 3.5rem;
        }
        td a {
            padding: 0.7rem 1.2rem;
            background-color: #3C0753;
            color: #fff !important;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s ease;
        }
        td a:hover {
            background-color: #720455;
        }
        .info {
            padding: 2rem;
        }
        .info p,
        .info a {
            color: gray;
            margin-bottom: 1rem;
            font-size: 1rem;
        }
        .info p:last-child {
            margin-top: 1rem;
        }
        .info a {
            text-decoration: underline;
        }
        .unsubscribe {
            font-size: 0.7rem;
            padding-top: 1.5rem;
            color: gray;
        }
        .unsubscribe a{ 
            padding: unset;
            background-color: unset;
            color: gray !important;
            border: none;
            border-radius: unset;
            font-size: 0.7rem;
            text-decoration: underline;
        }
        .unsubscribe a:hover {
            background-color: unset !important;
            color: #3C0753;     
        }
        @media screen and (max-width: 1800px) {
            :root {
                font-size: 14px;
            }
        }

        @media screen and (max-width: 1550px) {
            :root {
                font-size: 13px;
            }
        }

        @media screen and (max-width: 1290px) {
            :root {
                font-size: 12px;
            }
        }

        @media screen and (max-width: 1170px) {
            :root {
                font-size: 11px;
            }
        }

        @media screen and (max-width: 1024px) {
            :root {
                font-size: 10px;
            }
        }

        @media screen and (max-width: 990px) {
            :root {
                font-size: 11px;
            }
        }
        @media screen and (max-width: 899px) {
            :root {
                font-size: 10px;
            }
        }
        @media screen and (max-width: 768px) {
            :root {
                font-size: 9px;
            }
        }
        @media screen and (max-width: 699px) {
            :root {
                font-size: 8px;
            }
        }
        @media screen and (max-width: 576px) {
            :root {
                font-size: 14px;
            }
            .main {
                width: 100%;
                margin: 0 !important;
            }
        }
        @media screen and (max-width: 500px) {
            :root { 
                font-size: 13px;
            }
        }
        @media screen and (max-width: 450px) {
            :root {
                font-size: 11px;
            }
        }
        @media screen and (max-width: 375px) {
            :root {
                font-size: 9px;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="main">
            <table>
                <tr>
                    <td><img src="'''+ ImageRoutinPath+ 'logo_dark_purple.png' '''" alt="TrackMyPrice"></td>
                </tr>
                <tr>
                    <td><h1>¡Hemos detectado un cambio en el precio de tu producto "'''+ str(ins.ImageTrackDescription) +'''"!</h1></td>
                </tr>
                <tr>
                    <td><p>Para ver los detalles y consultar el nuevo precio, haz clic en el siguiente botón:</p></td>
                </tr>
                <tr>
                    <td><a href="'''+ str(base)+'''/details_price/''' + str(ins.id_image)+ '''/''' + str(current) +'''" target="_blank">Consultar precio</a></td>
                </tr>
                <tr>
                    <td class="unsubscribe">Puedes desuscribirte dando click <a href="'''+ str(base)+'''/unsubscribe/'''+ str(ins.id_image)+'''">aquí</a></td>
                </tr>
            </table>
            <div class="info">
                <p>Has recibido este email porque estás registrado en TrackMyPrice. Consulta nuestra <a href="https://trackmyprice.co/privacy" target="_blank">política de privacidad</a> para más información.</p>
                <p>&copy; <span id="year"></span> TrackMyPrice.</p>
            </div>
        </div>
    </div>
    <script type="text/javascript">
        document.getElementById('year').innerText = new Date().getFullYear();
    </script> 
</body>
</html>

                '''
        
            notify.conf({"destiny": ins.client_fk.email,
                        "body": html,
                        "affair" : f"Notificacion cambio de precio producto {ins.ImageTrackDescription}"
                        })
            notify.send_notification()
        Console.warning("No se obtuvo un precio correcto")
            
@shared_task(queue="email_queue")

def email_token(email,token_email, productDescription : str):
    notification = SelectorNotification()
    notification.select_notification("email")

    html = '''
            <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notificación de cambio de precio</title>
    <style type="text/css">
        *,
        html,
        body,
        div,
        span,
        applet,
        object,
        iframe,
        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        p,
        blockquote,
        pre,
        a,
        abbr,
        acronym,
        address,
        big,
        cite,
        code,
        del,
        dfn,
        em,
        font,
        img,
        ins,
        kbd,
        q,
        s,
        samp,
        small,
        strike,
        strong,
        sub,
        tt,
        var,
        b,
        u,
        i,
        center,
        dl,
        dt,
        dd,
        ol,
        ul,
        li,
        fieldset,
        form,
        label,
        legend,
        table,
        caption,
        tbody,
        tfoot,
        thead,
        tr,
        th,
        td,
        tr,
        select,
        input {
            appearance:inherit; 
            -moz-appearance:inherit; 
            -webkit-appearance:inherit; 
            background:transparent; 
            border:none; 
            border-radius:0; 
            box-sizing: border-box; 
            margin:0; 
            outline:0; 
            padding:0; 
            text-decoration:none;
            list-style: none;
            font-family: var(--main_font);
            color: inherit;
        }
        :root {
            /* Tamaño objetos */
            font-size: 15px;
            /* ===== Variables de fuentes ===== */
            --main_font: 'Poppins', sans-serif;
        }
        body {
            font-family: var(--main_font);
            background-color: #f0f0f0;        
        }
        .main {
            width: 50rem;
            margin: 0 auto;
        }
        table {
            background-color: #ffffff;
            border-radius: 5px;
            padding: 2rem;
        }

        table tr {
            text-align: center;
        }

        table tr.last_tr {
            text-align: start;
        }

        table tr td img.logo {
            height: 3.5rem;
        }

        table tr td h1 {
            font-size: 2rem;
            text-align: center;
            margin-bottom: 1rem;
        }


        table tr td p {
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }

        table tr td p.last_p {
            margin: 0;
        }

        table tr td p.p_margin {
            margin: 1rem 0;
        } 

        .btn {
            padding: 0.7rem 1.2rem;
            background-color: #3C0753;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s ease;
            margin-bottom: 1rem;
        }

        .btn:hover {
            background-color: #720455;
        }

        .link {
            color: #3C0753;
            text-decoration: underline;
            margin-bottom: 1rem;
        }


        .info {
            padding: 2rem;
        }
        .info p,
        .info a {
            color: gray;
            margin-bottom: 1rem;
            font-size: 1rem;
            margin-bottom: 1rem;
        }

        .info a {
            text-decoration: underline;
        }
        @media screen and (max-width: 1800px) {
            :root {
                font-size: 14px;
            }
        }

        @media screen and (max-width: 1550px) {
            :root {
                font-size: 13px;
            }
        }

        @media screen and (max-width: 1290px) {
            :root {
                font-size: 12px;
            }
        }

        @media screen and (max-width: 1170px) {
            :root {
                font-size: 11px;
            }
        }

        @media screen and (max-width: 1024px) {
            :root {
                font-size: 10px;
            }
        }

        @media screen and (max-width: 990px) {
            :root {
                font-size: 11px;
            }
        }
        @media screen and (max-width: 899px) {
            :root {
                font-size: 10px;
            }
        }
        @media screen and (max-width: 768px) {
            :root {
                font-size: 9px;
            }
        }
        @media screen and (max-width: 699px) {
            :root {
                font-size: 8px;
            }
        }
        @media screen and (max-width: 576px) {
            :root {
                font-size: 14px;
            }
            .main {
                width: 100%;
                margin: 0 !important;
            }
        }
        @media screen and (max-width: 500px) {
            :root { 
                font-size: 13px;
            }
        }
        @media screen and (max-width: 450px) {
            :root {
                font-size: 11px;
            }
        }
        @media screen and (max-width: 375px) {
            :root {
                font-size: 9px;
            }
        }

    </style>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="main">
        <table>
            <tr>
                <td><img class="logo" src="'''+ ImageRoutinPath+ 'logo_dark_purple.png' '''" alt="TrackMyPrice"></td>
            </tr>
            <tr>
                <td><h1>Verifica tu email para comenzar a usar TrackMyPrice</h1></td>
            </tr>
            <tr>
                <td><p>¡Hola! Para comenzar el monitoreo de tu producto "'''+ productDescription +'''" , por favor verifica tu dirección de email.</p></td>
            </tr>
            <tr>
                <td><a class="btn" href="'''+ str(base)+'''/token_confirm/'''+ str(token_email)+'''" target="_blank" style="color:white">Verifica tu producto</a></td>
            </tr>
            <tr>
                <td><p class="p_margin"><strong>¿No puedes ver el botón?  </strong>Copia y pega este enlace en tu navegador:</p></td>
            </tr>
            <tr>
                <td><a class="link">'''+ str(base)+'''/token_confirm/'''+ str(token_email)+'''</a></td>
            </tr>
            <tr class="last_tr">
                <td><p class="last_p">Si tienes preguntas o necesitas asistencia de nuestro equipo de Soporte, por favor <a class="link" href="https://trackmyprice.co/contact">contáctanos</a>.</p></td>
            </tr>
        </table>
        <div class="info">
            <p>Has recibido este email porque estás registrado en TrackMyPrice. Consulta nuestra <a href="https://trackmyprice.co/privacy" target="_blank">política de privacidad</a> para más información.</p>
            <p>&copy; <span id="year"></span> TrackMyPrice.</p>
        </div>
    </div>
    <script type="text/javascript">
        document.getElementById('year').innerText = new Date().getFullYear();
    </script>
</body>
</html>

    '''
    #url = f"http://127.0.0.1:8000/api/token_confirm/{token_email}"
    notification.conf({"destiny": email, "body": html, "affair": f"Confirmación de producto {productDescription}"})
    notification.send_notification()
    Console.warning("Correo enviado")

logger = logging.getLogger(__name__)    
@shared_task()
def execute_auto_task():
    
    try:
        img_repos = Image_repos()
        img_all = img_repos.gel_all()

        for img in img_all:
            if img.notify_validate:
                data = serialize("json", [img])
                Console.info("Tarea publicada")
                validate.delay(data)
    except Exception as e:
        
        logger.exception(f"Error al ejecutar y publicar tareas de validacion: {e}")               

