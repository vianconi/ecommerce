# Flask E-commerce API

Este es un backend RESTful construido con Flask que proporciona funcionalidades básicas para un sistema de e-commerce, incluyendo autenticación de usuarios, gestión de productos y operaciones con carrito de compras.

## Características

- Registro e inicio de sesión de usuarios con Flask-Login
- CRUD de productos (crear, leer, actualizar, eliminar)
- Gestión de carrito de compras (agregar, eliminar, ver, checkout)
- API protegida con autenticación de usuario
- Soporte para CORS

## Tecnologías usadas

- Python 3
- Flask
- Flask-Login
- Flask-CORS
- Flask-SQLAlchemy

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/flask-ecommerce-api.git
cd flask-ecommerce-api
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno necesarias:

Crea un archivo `config.py` en la raíz del proyecto con el contenido:

```python
SECRET_KEY = 'tu_clave_secreta'
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

5. Inicializa la base de datos:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

## Ejecución

```bash
python app.py
```

El servidor se ejecutará en `http://127.0.0.1:5000/`

## Endpoints principales

### Autenticación
- `POST /login` - Inicia sesión
- `POST /logout` - Cierra sesión (requiere login)

### Productos
- `GET /api/products` - Listar productos
- `GET /api/products/<product_id>` - Ver producto
- `POST /api/products/add` - Agregar producto (requiere login)
- `PUT /api/products/update/<product_id>` - Actualizar producto (requiere login)
- `DELETE /api/products/delete/<product_id>` - Eliminar producto (requiere login)

### Carrito
- `GET /api/cart` - Ver carrito (requiere login)
- `POST /api/cart/add/<product_id>` - Agregar al carrito (requiere login)
- `DELETE /api/cart/remove/<product_id>` - Eliminar del carrito (requiere login)
- `POST /api/cart/checkout` - Vaciar carrito (requiere login)

## Notas
- No incluye hashing de contraseñas, es solo para fines educativos.
- Se puede adaptar fácilmente para producción con ajustes de seguridad y base de datos.

## Licencia

MIT License
