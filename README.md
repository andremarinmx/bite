# Bite App #

![Bite App Logo](logo.png)

Aplicación web progresiva para la venta de comida en Ciudad Juárez.

---

## Configuración del proyecto ##

### Clonar el repositorio ###

`$ git clone https://github.com/oscarmiranda3615/biteapp.git`

### Crear una entorno virtual dentro del repositorio (solo se realiza una vez) ###

`$ virtualenv venv`

*Es necesario que se llame __venv__, pues así está escrito en los archivos a excluir en cambios realizados*

### Activar el entorno virtual (cada vez que se va a trabajar en el repositorio) ###

Desde cmd:

`$ venv\Scripts\activate.bat`

Desde PowerShell:

`$ .\venv\Scripts\activate.ps1`

### Instalar las dependencias del proyecto ###

`$ pip install -r requirements.txt`

---

## Estructura base del proyecto ##

```
biteapp (Raíz del proyecto)
└---models (Código backend con acceso a la BD)
|	└	*.py
└---static
|	└---css (Estilos de la app)
|	|	└	*.css
|	└---icons (Íconos de la app [Logo])
|	|	└	*.png
|	└---img (Imágenes dentro de la app)
|	|	└	*.svg
|	└---js (Comportamiento del frontend)
|	|	└	*.js
|	|	favicon.png (Ícono usado en la web)
|	|	manifest.json (Configuración de la app)
|	|	service-worker.js (Convierte el sitio en app)
└---templates (Vistas de la app)
|	|	*.html
|	└---layouts (Disposición de la vista)
|		└	*.html
|	.gitignore (Archivos a excluir del repositorio)
|	.pylintrc (Configuración del linter)
|	api.py (Puntos de acceso asíncrono)
|	app.py (Inicio de la app)
|	db.py (Configuración de la BD)
|	login.py (Manejar el inicio de sesión)
└	requirements.txt (Dependencias del proyecto)
```

---

## Extensiones recomendadas para Visual Studio Code ##

### Color Highlight (Sergii Naumov) ###

> Previsualizar colores en archivos CSS.

[Ver en Marketplace](https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight)

### Jinja (wholroyd) ###

> Soporte de sintaxis y autocompletado de plantillas.

[Ver en Marketplace](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja)

### Live Share (Microsoft) ###

> Colaboración en tiempo real sobre el proyecto.

[Ver en Marketplace](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

---

## Acerca de ##

Proyecto realizado por:

- [Óscar Miranda](https://github.com/oscarmiranda3615)
- [André Marín](https://github.com/andre7070)
