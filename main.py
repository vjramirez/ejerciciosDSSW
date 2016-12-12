#!/usr/bin/env python
# -*- coding: cp1252 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>EjerciciosDSSW - Victor Ramirez</h1><br/><br/>'
                            '<a href="/tarea1">Tarea 1</a><br/>'
                            '<a href="/registro">Tarea 2</a><br/>'
                            )
		
class Tarea1Handler(webapp2.RequestHandler):
	def get(self):
		self.response.write('<H1>Tarea 1</H1><br/><br/>'
                                    '<a href="/saludo?lang=SP">Saludo</a><br/>'
                                    '<a href="/saludo?lang=EN">Greeting</a><br/>'
                                    '<a href="/saludo?lang=EU">Agurra</a><br/>'
                                    )
class Tarea1SaludoHandler(webapp2.RequestHandler):
	def get(self):
                lang = self.request.get("lang")
                self.response.write('''
                                    <html>
                                        <head>
                                            <style type="text/css">
                                                H1 {border-width: 1; border: solid;}
                                                body {text-align: center}
                                            </style>
                                        </head>
                                        <body>
                                    ''')
                if lang == 'SP':
                    self.response.write('<H1>Hola Mundo</H1><br/>')
                elif lang == 'EN':
                    self.response.write('<H1>Hello World</H1><br/>')
                elif lang == 'EU':
                    self.response.write('<H1>Kaixo Mundoa</H1><br/>')
        
                self.response.write('''
                                            <img src="https://media.giphy.com/media/3o6gb3qeuP96u4m5cQ/giphy-tumblr.gif" /><br/>
                                            <H1></H1>
                                        </body>
                                    </html>
                                    ''')

ER_USUARIO = re.compile(r"^[a-zA-z0-9]{3,20}")
ER_CONTRASENA = re.compile(r"^.{6,20}")
ER_CORREO = re.compile(r"^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$")
		
class Tarea2Handler(webapp2.RequestHandler):
	def get(self):
            lang = self.request.get("lang")
            tarea = "Tarea"
            rellene = "Rellene los campos por favor"
            usuario = "Nombre de usuario"
            tunombre = "Tu nombre"
            contrasena = "Contrase&ntilde;a"
            tucontrasena = "Tu contrase&ntilde;a"
            repecontrasena = "Repetir contrase&ntilde;a"
            repelacontrasena = "Repite la contrase&ntilde;a"
            email = "Correo Electr&oacute;nico"
            tuemail = "Tu correo electr&oacute;nico"
            enviar = "Enviar"
            nombError = "Nombre Incorrecto"
            passError = "Contrase\u00F1a Incorrecta"
            passmiss = "Contrase\u00F1a No Coincide"
            emailError = "Email Incorrecto"
            if lang == 'EN':
                tarea = "Task"
                rellene = "Please, complete the information below"
                usuario = "Username"
                tunombre = "Your name"
                contrasena = "Password"
                tucontrasena = "Your password"
                repecontrasena = "Repeat password"
                repelacontrasena = "Repeat the password"
                email = "Email"
                tuemail = "Your Email"
                enviar = "Submit"
                nombError = "Wrong Name"
                passError = "Wrong Password"
                passmiss = "Password Mismatch"
                emailError = "Wrong Email"
	    self.response.write('''
<html>
  <head>
    <link type="text/css" rel="stylesheet" href="http://siconeso.appspot.com/stylesheets/main.css" />
    <title>Introduzca sus datos:</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
      h6 {float: right;
          margin-top: 0px;}
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script>
    $(document)
        .on('click', 'form input[type=submit]', function(e) {
            $('span').text("");
            var isValid = true;
            if ($('#username').val()==''){
                $('#error_username').text("''' + nombError + '''!");
                isValid = false;
            }
            if ($('#password').val()==''){
                $('#error_password').text("''' + passError + '''!");
                isValid = false;
            }
            if ($('#verify').val()==''){
                $('#error_verify').text("''' + passError + '''!");
                isValid = false;
            }
            if ($('#password').val()!='' && $('#verify').val()!='' && $('#password').val() != $('#verify').val()){
                $('#error_verify').text("''' + passmiss + '''!");
                isValid = false;
            }
            if( !validateEmail($('#email').val())) {
                $('#error_email').text("''' + emailError + '''!");
                isValid = false;
            }
            if(!isValid) {
              e.preventDefault(); //prevent the default action
            }
        });

        function validateEmail(email) {
          var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
          return regex.test(email);
        }
    </script>
  </head>
 
  <body>
  <h6><a href="/registro">Espa&ntilde;ol</a> | <a href="/registro?lang=EN">English</a></h6>
  <h1>DSSW-''' + tarea + ''' 2</h1>
    <h2>''' + rellene + ''':</h2>
    <form method="post" target="my_iframe">
      <table>
        <tr>
          <td class="label">
            ''' + usuario + '''
          </td>
          <td>
            <input type="text" name="username" id="username" value="" placeholder="''' + tunombre + ''' ...">
          </td>
          <td class="error">
            <span id="error_username"></span>
          </td>
        </tr>
 
        <tr>
          <td class="label">
            ''' + contrasena + '''
          </td>
          <td>
            <input type="password" name="password" id="password" value="" placeholder="''' + tucontrasena + ''' ..." autocomplete="off">
          </td>
          <td class="error">
            <span id="error_password"></span>
          </td>
             
          </td>
        </tr>
 
        <tr>
          <td class="label">
            ''' + repecontrasena + '''
          </td>
          <td>
            <input type="password" name="verify" id="verify" value="" placeholder="''' + repelacontrasena + ''' ...">
          </td>
          <td class="error">
            <span id="error_verify"></span>
          </td>
        </tr>
 
        <tr>
          <td class="label">
            ''' + email + '''
          </td>
          <td>
            <input type="text" name="email" id="email" value=""  placeholder="''' + tuemail + ''' ...">
          </td>
          <td class="error">
            <span id="error_email"></span>
          </td>
        </tr>
      </table>
 
      <input type="submit" value="''' + enviar + '''">
    </form>
    <iframe name="my_iframe"  width="100%" height="300" frameBorder="0" ></iframe>
  </body>
 
</html>
''')
        def post(self):
            mensaje = ""
            username = self.request.get("username")
            password = self.request.get("password")
            verify = self.request.get("verify")
            email = self.request.get("email")
            lang = self.request.get("lang")
            hola = "Hola "
            datos = "Tus datos son correctos"
            nombreVacio = "El nombre debe tener entre 3 y 20 caracteres (entre d&iacute;gitos y/o letras)"
            noCoinciden = "Las contrase&ntilde;as no coinciden"
            passCorto = "La contrase&ntilde;a debe tener una longitud m&iacute;nima de 6 caracteres."
            correoIncorrecto = "El correo no tiene el formato correcto"
            if lang == 'EN':
                hola = "Hello "
                datos = "Your information is correct."
                noCoinciden = "Password Mismatch"
                nombreVacio = "Username must have between 3 and 20 characters (digits and/or letters)."
                passCorto = "Password must have at least 6 characters"
                correoIncorrecto = "Incorrect email format"
            if not ER_USUARIO.match(username):
                mensaje += '<span class="error" id="error_email">' + nombreVacio + '</span><br/>'
            if not ER_CONTRASENA.match(password):
                mensaje += '<span class="error" id="error_email">' + passCorto + '</span><br/>'
            if password <> verify :
                mensaje += '<span class="error" id="error_email">' + noCoinciden + '</span><br/>'
            if not ER_CORREO.match(email):
                mensaje += '<span class="error" id="error_email">' + correoIncorrecto + '</span><br/>'

            if mensaje == "" :
                self.response.write('''<link type="text/css" rel="stylesheet" href="http://siconeso.appspot.com/stylesheets/main.css" />
                                <span class="label">''' + hola + self.request.get("username") + '''</span><br/>
                                <span class="label">''' + datos + '''</span><br/>''')
            else:
                self.response.write('''<link type="text/css" rel="stylesheet" href="http://siconeso.appspot.com/stylesheets/main.css" />
                                    <style>
                                        .error {color: red}
                                    </style>
                                    ''' + mensaje )

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/tarea1', Tarea1Handler),
	('/registro', Tarea2Handler),
	('/saludo', Tarea1SaludoHandler),
], debug=True)
