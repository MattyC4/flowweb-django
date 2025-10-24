# FlowWeb (Django)

Sistema web para gestión de APR (AquaMetrics/FlowWeb). Incluye autenticación por **correo o nombre de usuario**, dashboards por **rol**, y módulo inicial de **reportes por RUT**.

## Requisitos
- Python 3.11+ (recomendado)
- Node.js 18+ y npm
- Git
- (Opcional) PowerShell en Windows

## Estructura sugerida
flowweb/
├─ config/ # settings, urls, asgi/wsgi
├─ apps/
│ ├─ users/ # login por email/username, roles, redirecciones
│ ├─ medidores/
│ ├─ consumos/
│ ├─ boletas/
│ └─ reportes/ # consulta por RUT (historial de consumo)
├─ templates/
│ ├─ users/ ... # cada app con su base_<app>.html
│ └─ ...
├─ static/ # estáticos de dev (no versionar colectados)
├─ manage.py
├─ package.json # Tailwind / build front si aplica
├─ tailwind.config.js # (si usas Tailwind)
├─ postcss.config.js
├─ requirements.txt
├─ .env.example # ejemplo de variables
└─ .gitignore

r
Copiar código

> Convención de bases HTML: cada app tiene su `base_<app>.html` (p.ej. `base_users.html`, `base_reportes.html`) con header, footer y botón “Volver al dashboard” según rol.

## Configuración (Windows / PowerShell)
1) **Clonar e instalar dependencias Python**
```powershell
git clone https://github.com/MattyC4/flowweb-django.git
cd flowweb-django
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
Variables de entorno

powershell
Copiar código
copy .env.example .env
# Edita SECRET_KEY y otros valores reales
Migraciones y superusuario

powershell
Copiar código
python manage.py migrate
python manage.py createsuperuser
Correr el servidor

powershell
Copiar código
python manage.py runserver
Frontend (opcional si usas Tailwind/MUI/etc.)

powershell
Copiar código
npm install
npm run dev   # o el script definido en package.json
Autenticación y Roles
Login por correo o nombre de usuario (app users).

Tras iniciar sesión, se redirige a dashboard según rol:

admin: acceso completo.

secretaria: sin acceso a creación de tarifas ni registro de cuentas nuevas.

operario: registrar consumos y medidores, ver historiales.

Validaciones de acceso por rol evitando saltos vía URL.

Reportes (App reportes)
Consulta por RUT (historial consumo mensual, medidor asignado y otros datos).

Página accesible desde el índice.

Variables clave (ver .env.example)
SECRET_KEY, DEBUG, ALLOWED_HOSTS

DB_* para base de datos (por defecto SQLite; puedes pasar a Postgres/MySQL)

EMAIL_* si envías correos

(Futuro) Integraciones SII / Cloud (AWS, Firebase) → no poner secretos en el repo, solo en .env.

Comandos útiles
powershell
Copiar código
# Activar entorno
.\.venv\Scripts\activate

# Instalar nuevas dependencias
pip install <paquete>
pip freeze > requirements.txt

# Colectar estáticos (prod)
python manage.py collectstatic

# Formato/estilo (si usas black/isort)
black .
isort .
Git workflow recomendado
Rama principal protegida: main

Trabajo diario:

bash
Copiar código
git checkout -b feature/<breve-descripcion>
# ...cambios...
git add .
git commit -m "feat(users): login por email o username"
git push -u origin feature/<breve-descripcion>
# abre Pull Request hacia main
Troubleshooting
No puedo hacer push (non-fast-forward)
Usa:

bash
Copiar código
git pull --rebase origin main --allow-unrelated-histories
git push
Node modules en el repo
Asegúrate que node_modules/ está en .gitignore y ejecuta:

bash
Copiar código
git rm -r --cached node_modules
git commit -m "chore: stop tracking node_modules"
git push
db.sqlite3 bloqueada
Cierra runserver/extensiones que la usen. No se versiona; ya está en .gitignore.
