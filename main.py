#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import cgi
import urllib
import hashlib
import json
import re

from google.appengine.api import images
from google.appengine.ext import ndb


class usuario(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    image = ndb.BlobProperty()

class Image(webapp2.RequestHandler):
    def get(self):
        greeting_key = ndb.Key(urlsafe=self.request.get('img_id'))
        greeting = greeting_key.get()
        if greeting.image:
            #img = images.Image(greeting.image)
            #img.resize(width=80, height=100)
            #img.im_feeling_lucky()
            #thumbnail = img.execute_transforms(output_encoding=images.JPEG)

            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(greeting.image)
        else:
            self.response.out.write('No image')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>EjerciciosDSSW - Victor Ramirez</h1><br/><br/>'
                            '<a href="/tarea1">Tarea 1</a><br/>'
                            '<a href="/registro">Tarea 2</a><br/>'
                            '<a href="/verusuarios">Tarea 3</a><br/>'
                            '<a href="/registro">Tarea 4</a><br/>'
                            '<a href="/datos">Tarea 5</a><br/>'
                            )
		
class Tarea1Handler(webapp2.RequestHandler):
	def get(self):
		self.response.write('<H1>Tarea 1</H1><br/><br/>'
                                    '<a href="/saludo?lang=SP">Saludo</a><br/>'
                                    '<a href="/saludo?lang=EN">Greeting</a><br/>'
                                    '<a href="/saludo?lang=EU">Agurra</a><br/>'
                                    )

class Tarea3Handler(webapp2.RequestHandler):
	def get(self):
                usuarios = usuario.query()
                self.response.write('''<style>
                                            table {
                                                    border-collapse: collapse;
                                                    font
                                                }

                                                table, th, td {
                                                    border: 1px solid black;
                                                    padding: 3px;
                                                }
                                                th {
                                                    background-color: gray;
                                                    color: white;
                                                }
                                        </style>
                                        
                                        <H1>Usuarios Registrados</H1><a href="/registro">Registrarse</a><br/><br/><br/>
                                        <table>
                                            <tr>
                                                <th>Usuario</th>
                                                <th>Correo</th>
                                                <th>Fecha de registro</th>
                                                <th>Imagen</th>
                                            </tr>''')
                for acct in usuarios.fetch():
                    self.response.write('''
                                            <tr>
                                                <td>''' + acct.nombre + '''</td>
                                                <td>''' + acct.email + '''</td>
                                                <td>''' + str(acct.created) + '''</td>
                                                <td>''')
                    if acct.image:
                        self.response.write('<div><img src="/img?img_id=%s"></img></div>' %
                                    acct.key.urlsafe())
                    else:
                        self.response.write('''Sin Imagen''')
                    self.response.write('''</td></tr>''')
                self.response.write('''</table>''')

            
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


ER_USUARIO = re.compile(r"^[a-zA-Z0-9]{3,20}")
ER_CONTRASENA = re.compile(r"^.{6,20}")
ER_CORREO = re.compile(r"^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$")

class EmailHandler(webapp2.RequestHandler):
    def get(self):
                email = self.request.get("email")
                if not ER_CORREO.match(email):
                    self.response.out.write('''<div style="background-color: white;"><b>Email incorrecto</b></div> @@@@@ $('#email').val('')''')
                else:
                    usuarios = usuario.query(usuario.email == email)
                    if usuarios.count() == 0 :
                        self.response.out.write('''<div style="background-color: white; color: green;"><b>Email correcto</b></div> @@@@@''')
                    else:
                        self.response.out.write('''<div style="background-color: white; color: blue;"><b>Email ya utilizado</b></div> @@@@@ $('#email').val('')''')

		
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
            imagen = "Imagen"
            tuimagen = "Selecciona una imagen"
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
                imagen = "Image"
                tuimagen = "Choose an image"
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
                  //e.preventDefault(); //prevent the default action
                }
            });

        function validateEmail(email) {
          var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
          return regex.test(email);
        }


        window.onload = function() {
            $("#email").change(function() {
                validarEmail($(this).val())
            });
        };


        function validarEmail(f){    
        $.ajax("/valemail?email="+f, 
        { "type": "get",   // usualmente post o get
           "success": function(result) {
                // respuesta en un span
                var vecResult = result.split('@@@@@');
                $("#error_email").html(vecResult[0]);
                eval(vecResult[1]);
                },
            "beforeSend": function() {
                $("#error_email").html("Consultando...");
            },
           "error": function(result) {
            console.error("Se ha producido un error: ", result);},
            "async": true,})
        };


    </script>
  </head>
 
  <body>
  <h5><a href="/verusuarios">Usuarios Registrados</a></h5>
  <h6><a href="/registro">Espa&ntilde;ol</a> | <a href="/registro?lang=EN">English</a></h6>
  <h1>DSSW-''' + tarea + ''' 2</h1>
    <h2>''' + rellene + ''':</h2>
    <form method="post" enctype="multipart/form-data" target="my_iframe">
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
        <tr>
          <td class="label">
            ''' + imagen + '''
          </td>
          <td>
            <input type="file" name="imagen" id="imagen" value="" >
          </td>
          <td class="error">
            <span id="error_imagen"></span>
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
            avatar = self.request.get('imagen')
            avatarName = self.request.POST.multi['imagen']
            hola = "Hola "
            datos = "Tus datos son correctos"
            nombreVacio = "El nombre debe tener entre 3 y 20 caracteres (entre d&iacute;gitos y/o letras)"
            noCoinciden = "Las contrase&ntilde;as no coinciden"
            passCorto = "La contrase&ntilde;a debe tener una longitud m&iacute;nima de 6 caracteres."
            correoIncorrecto = "El correo no tiene el formato correcto"
            usuarioRegistrado = "Este usuario no esta disponible, cambie el nombre de usuario o correo."
            if lang == 'EN':
                hola = "Hello "
                datos = "Your information is correct."
                noCoinciden = "Password Mismatch"
                nombreVacio = "Username must have between 3 and 20 characters (digits and/or letters)."
                passCorto = "Password must have at least 6 characters"
                correoIncorrecto = "Incorrect email format"
                usuarioRegistrado = "User not available, change username or email."
            if not ER_USUARIO.match(username):
                mensaje += '<span class="error" id="error_email">' + nombreVacio + '</span><br/>'
            if not ER_CONTRASENA.match(password):
                mensaje += '<span class="error" id="error_email">' + passCorto + '</span><br/>'
            if password <> verify :
                mensaje += '<span class="error" id="error_email">' + noCoinciden + '</span><br/>'
            if not ER_CORREO.match(email):
                mensaje += '<span class="error" id="error_email">' + correoIncorrecto + '</span><br/>'

            if mensaje == "" :
                usuarios = usuario.query(ndb.OR(usuario.nombre == username, usuario.email == email))
                if usuarios.count() > 0 :
                    mensaje= '<span class="error" id="error_email">' + usuarioRegistrado + '</span><br/>'
                    self.response.write('''<link type="text/css" rel="stylesheet" href="http://siconeso.appspot.com/stylesheets/main.css" />
                                    <style>
                                        .error {color: red}
                                    </style>
                                    ''' + mensaje )
                else:
                    datosLog = usuario()
                    datosLog.nombre = username
                    datosLog.password = hashlib.md5(password).hexdigest()
                    datosLog.email = email
                    if avatarName != "":
                        avatar = images.resize(avatar, 80, 100)
                        datosLog.image = avatar
                    #if (img_format == 'jpeg' or 'jpg' or 'gif' or 'png' or 'bmp' or 'tiff' or 'ico' or 'webp'):
                    
                    datosLog.put()
                    self.response.write('''<link type="text/css" rel="stylesheet" href="http://siconeso.appspot.com/stylesheets/main.css" />
                                <span class="label">''' + hola + self.request.get("username") + '''</span><br/>
                                <span class="label">''' + datos + '''</span><br/>''')
            else:
                self.response.write('''<link type="text/css" rel="stylesheet" href="http://siconeso.appspot.com/stylesheets/main.css" />
                                    <style>
                                        .error {color: red}
                                    </style>
                                    ''' + mensaje )

class Tarea5Handler(webapp2.RequestHandler):
    def get(self):
                lang = self.request.get("lang")
                self.response.write('''
                                    <!DOCTYPE html>
                                    <html>
                                        <head>
                                            <title>DSSW-Tarea 5</title>
                                            <meta name="viewport" content="initial-scale=1.0">
                                            <meta charset="utf-8">
                                            <script src="https://apis.google.com/js/platform.js" async defer></script>
                                            <meta name="google-signin-client_id" content="960747220119-kvks81kdt3s1cl2hhs0372h7q9onjpqg.apps.googleusercontent.com">
                                            <style>
                                              /* Always set the map height explicitly to define the size of the div
                                               * element that contains the map. */
                                              #map {
                                                height: 500px;
                                                width: 800px;
                                              }
                                              /* Optional: Makes the sample page fill the window. */
                                              html, body {
                                                height: 100%;
                                                margin: 0;
                                                padding: 0;
                                              }
                                            </style>
                                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                                            <script>

                                                function statusChangeCallback(response) {

                                                    if (response.status === 'connected') {
                                                      // Logged into your app and Facebook.
                                                      testAPI();
                                                    } 
                                                    else {
                                                      // The person is not logged into Facebook, so we're not sure if
                                                      // they are logged into this app or not.
                                                      //document.getElementById('log').innerHTML = 'Please log ' +
                                                      //  'into Facebook.';
                                                    }
                                                  }
                                                function logout() {
                                                    FB.logout(function(response) {
                                                       // Person is now logged out
                                                       $("#logout").hide();
                                                        $("#logout").html("");
                                                        $("#login").show();
                                                    });
                                                }

                                                function checkLoginState() {
                                                    FB.getLoginStatus(function(response) {
                                                      statusChangeCallback(response);
                                                    });
                                                  }

                                                var profile;
                                                window.onload = function() {
                                                    $("#consultar").click(function() {
                                                        if ($("#dir").val() != ""){
                                                            $("#dir").css("background-color","white");
                                                            buscarDir($("#dir").val())
                                                        }
                                                        else {
                                                            $("#dir").css("background-color","red");
                                                        }
                                                        
                                                    });
                                                    $("body").show();
                                                };

                                                function buscarDir(f){
                                                    f = f.replace(/á/g,"a").replace(/é/g,"e").replace(/í/g,"i").replace(/ó/g,"o").replace(/ú/g,"u");
                                                    $.ajax("/datos?dir="+f, 
                                                    { "type": "post",   // usualmente post o get
                                                       "success": function(result) {
                                                            // respuesta en un span
                                                            $("#loading").hide();
                                                            var vecResult = result.split('@@@@@');
                                                            $("#my_div").html(vecResult[0]);
                                                            eval(vecResult[1]);
                                                            },
                                                        "beforeSend": function() {
                                                            $("#loading").show();
                                                            $("#my_div").html("");
                                                            $("#map").html("");
                                                        },
                                                       "error": function(result) {
                                                        console.error("Se ha producido un error: ", result);},
                                                        "async": true,})
                                                };

                                                function onSignIn(googleUser) {
                                                // Si el login es correcto ...
                                                  var profile = googleUser.getBasicProfile();
                                                  $("#login").hide();
                                                  $("#logout").html("<div style='float:right;'><img src='"+ profile.getImageUrl() + "'></div><div style='float:right; padding:10px;'><b>"+ profile.getName() +
                                                                    "</b><br/>" + profile.getEmail() + "<br/>" +
                                                                    "<a href='#' onclick='signOut();'>Salir</a></div>");
                                                  /*alert('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
                                                  alert('Name: ' + profile.getName());
                                                  alert('Image URL: ' + profile.getImageUrl());
                                                  alert('Email: ' + profile.getEmail());*/
                                                  $("#logout").show();
                                                }

                                                function signOut() {
                                                    var auth2 = gapi.auth2.getAuthInstance();
                                                    auth2.signOut().then(function () {
                                                        $("#logout").hide();
                                                        $("#logout").html("");
                                                        $("#login").show();
                                                    });
                                                }


                                            </script>
                                          </head>
                                          <body style="display:none;">
                                            <div id="fb-root"></div>
                                            <script>
                                                window.fbAsyncInit = function() {
                                                    FB.init({
                                                      appId      : '279232835812962',
                                                      xfbml      : true,
                                                      version    : 'v2.8'
                                                    });

                                                    FB.getLoginStatus(function(response) {
                                                        statusChangeCallback(response);
                                                    });
                                                  };

                                                (function(d, s, id) {
                                                    $("#fbutton").html("Acceder");
                                                  var js, fjs = d.getElementsByTagName(s)[0];
                                                  if (d.getElementById(id)) return;
                                                  js = d.createElement(s); js.id = id;
                                                  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.8";
                                                  fjs.parentNode.insertBefore(js, fjs);
                                                }(document, 'script', 'facebook-jssdk'));


                                                function testAPI() {
                                                    var urlImg = "";
                                                    FB.api('/me/picture', function(response) {
                                                        urlImg = response.data.url;
                                                    });
                                                    FB.api('/me', { fields: 'name, email' }, function(response) {
                                                        $("#login").hide();
                                                        //$("#logout").html('Thanks for logging in, ' + response.name + '!' + '<br/><button onclick="javascript:logout();">Logout from Facebook</button>');
                                                        $("#logout").html("<div style='float:right;'><img src='" + urlImg + "'></div><div style='float:right; padding:10px;'><b>"+ response.name +
                                                                    "</b><br/>"+ response.email +"<br/>" +
                                                                    "<button onclick='javascript:logout();'>Salir de Facebook</button></div>");
                                                        $("#logout").show();

                                                    });
                                                  }

                                            </script>


                                            <div id="login" style="float:right; margin:10px;">
                                                <div style="float:right;"
                                                    class="g-signin2"
                                                    data-onsuccess="onSignIn"
                                                    data-onfailure="onSignInFailure">
                                                </div>
                                                <fb:login-button id="fbutton" style="float:right; margin-right:10px; margin-top:5px;" size="large" scope="public_profile,email" onlogin="checkLoginState();">Acceder</fb:login-button>
                                            </div>
                                            <div id="logout" style="float:right; width:350px; height:100px;">
                                            </div>
                                    
                                            
                                            <h1>DSSW-Tarea 5: Servicios Web</h1>
                                            <h4>Escriba una dirección, barrio, ciudad, provincia o país para consultar su ubicación en un mapa.</h4>
                                            <input type="text" name="dir" id="dir" />
                                            <input type="button" value="Consultar" id="consultar" />
                                            <div id="loading" width="100%" height="300" style="display:none">
                                                <img src='http://img.ffffound.com/static-data/assets/6/77443320c6509d6b500e288695ee953502ecbd6d_m.gif' />
                                            </div>
                                            <div id="my_div" width="100%" height="300" ></div>
                                            <div id="map" ></div>
                                            <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBwbeY6D6EAdwNgPo0cvHqrJzRzcIzv4MI"></script>


                                            
                                        <body>
                                    </html>
                                    ''')
    def post(self):
                serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
                address=self.request.get('dir')
                url = serviceurl + urllib.urlencode({'address': address})
                uh = urllib.urlopen(url)
                data = uh.read()
                #js = json.loads(unicode(str(data).decode('utf-8')))
                js = json.loads(str(data))
                matriz = js['results']
                if len(matriz)>0:
                    direccion = matriz[0]['formatted_address']
                    self.response.write('''<br/>Resultado: ''' + direccion + '''</br> ''')
                    self.response.write('''Latitud: ''' + str(matriz[0]['geometry']['location']['lat']) + '''</br> ''')
                    self.response.write('''Longitud: ''' + str(matriz[0]['geometry']['location']['lng']) + '''</br> ''')
                    self.response.write('''@@@@@
                                                var myLatLng = {lat: ''' + str(matriz[0]['geometry']['location']['lat']) + ''', lng: ''' + str(matriz[0]['geometry']['location']['lng']) +'''};
                                                var map = new google.maps.Map(document.getElementById('map'), {
                                                  zoom: 14,
                                                  center: myLatLng
                                                });
                                                var marker = new google.maps.Marker({
                                                  position: myLatLng,
                                                  map: map,
                                                  title: ' ''' + direccion + ''' '
                                                });

                                                var contentString = '<div id="content">'+
                                                                    '<div id="siteNotice">'+
                                                                    '</div>'+
                                                                    '<h1 id="firstHeading" class="firstHeading">''' + direccion + '''</h1>'+
                                                                    '<div id="bodyContent">'+
                                                                    '<p>Latitud: ''' + str(matriz[0]['geometry']['location']['lat']) + '''</br>'+
                                                                    'Longitud: ''' + str(matriz[0]['geometry']['location']['lng']) + '''</p>'+
                                                                    '</div>'+
                                                                    '</div>';

                                                var infowindow = new google.maps.InfoWindow({
                                                  content: contentString
                                                });


                                                marker.addListener('click', function() {
                                                  infowindow.open(map, marker);
                                                });


    ''')

                else:
                    self.response.write('''<br/>No hay resultados.''')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/tarea1', Tarea1Handler),
	('/registro', Tarea2Handler),
	('/saludo', Tarea1SaludoHandler),
    ('/verusuarios', Tarea3Handler),
    ('/img', Image),
    ('/valemail', EmailHandler),
    ('/datos', Tarea5Handler),
], debug=True)
