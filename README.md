**🚀 TP1 - API REST con FastAPI: ABM de Usuarios y Productos**  

Trabajo Práctico N° 1 de la materia **Programación IV** — *Tecnicatura Universitaria en Programación (UTN)*.  
El proyecto implementa una **API RESTful** en memoria utilizando **FastAPI** y **Pydantic v2**, completando el ABM (Alta, Baja, Modificación y Filtrado) de la entidad `User` y agregando el CRUD completo de una entidad propia (`Product`).  
  
---  
**📁 Estructura del Proyecto**  
```  
clase-fastapi/  
 ├── main.py                # Punto de entrada y configuración de FastAPI  
 ├── models/  
 │   ├── users.py           # Modelos Pydantic y validaciones de Usuarios  
 │   └── products.py        # Modelos Pydantic y validaciones de Productos  
 ├── routers/  
 │   ├── users.py           # Endpoints CRUD y filtrado de Usuarios  
 │   └── products.py        # Endpoints CRUD y filtrado de Productos  
 ├── requirements.txt       # Dependencias del proyecto  
 ├── setup.cfg              # Reglas de estilo PEP 8 (pycodestyle)  
 └── pyrightconfig.json     # Configuración de chequeo estático de tipos  
   
```  
  
---  
**⚙️ Instalación y Ejecución**  
**1. Clonar el repositorio**  
```  
git clone https://github.com/IvanClar1a/UTN-TP1-PROGRAMACION-IV.git  
 cd UTN-TP1-PROGRAMACION-IV/clase-fastapi  
   
```  
   
**2. Crear y activar el entorno virtual**  
**En Linux / macOS:**  
```  
python3 -m venv .venv  
 source .venv/bin/activate  
   
```  
*Nota (Ubuntu/Debian): si aparece un error al crear el entorno virtual, instalar primero `sudo apt install python3-venv`.*  
**En Windows (PowerShell):**  
```  
python -m venv .venv  
 .venv\Scripts\Activate.ps1  
   
```  
**En Windows (CMD):**  
```  
python -m venv .venv  
 .venv\Scripts\activate.bat  
   
```  
**3. Instalar dependencias**  
```  
pip install -r requirements.txt  
   
```  
**4. Levantar el servidor de desarrollo**  
```  
fastapi dev main.py  
   
```  
*(Alternativa con Uvicorn: `uvicorn main:app --reload`)*  
   
 *(Si el puerto `8000` ya está ocupado, podés levantar en otro puerto con: `fastapi dev main.py --port 8001`)*  
  
---  
**📖 Documentación Interactiva (Swagger UI)**  
Con el servidor corriendo en `http://127.0.0.1:8000`, podés acceder a la documentación interactiva para probar todos los endpoints directamente desde el navegador:  
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs "http://127.0.0.1:8000/docs")  
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc "http://127.0.0.1:8000/redoc")  
**¿Cómo probar un endpoint en Swagger?**  
1. Hacé clic sobre el endpoint que quieras probar (por ejemplo `GET /user` o `POST /product`).  
2. Presioná el botón **"Try it out"**.  
3. Completá los parámetros o el cuerpo JSON (si corresponde) y hacé clic en **"Execute"**.  
  
---  
**🔌 Endpoints Disponibles**  
**👤 Usuarios (**`/user`**)**  
Modelo: `id` (`int > 0`), `name` (`str`), `is_active` (`bool`, por defecto `true`).  
  
|  |  |  |  |  
| - | - | - | - |  
| **Método** |  **Ruta** |  **Descripción** |  **Código OK** |  
| `GET` |  `/user` |  Lista todos los usuarios. Permite filtrar por estado con `?is_active=true` o `?is_active=false`. |  `200` |  
| `GET` |  `/user/{id}` |  Obtiene un usuario específico por su `id`. |  `200` |  
| `POST` |  `/user` |  Crea un nuevo usuario validando que el `id` no esté duplicado. |  `201` |  
| `PUT` |  `/user/{id}` |  Reemplaza por completo los datos de un usuario existente. |  `200` |  
| `PATCH` |  `/user/{id}` |  Modifica parcialmente solo los campos enviados del usuario. |  `200` |  
| `DELETE` |  `/user/{id}` |  Elimina un usuario existente por su `id`. |  `200` |  
  
   
**📦 Productos (**`/product`**)**  
Entidad propia de 5 campos: `id` (`int > 0`), `nombre` (`str`), `categoria` (`str`), `precio` (`float > 0`), `stock` (`int >= 0`).  
  
|  |  |  |  |  
| - | - | - | - |  
| **Método** |  **Ruta** |  **Descripción** |  **Código OK** |  
| `GET` |  `/product` |  Lista todos los productos. Permite búsqueda por categoría con `?categoria=perifericos`. |  `200` |  
| `GET` |  `/product/{id}` |  Obtiene un producto específico por su `id`. |  `200` |  
| `POST` |  `/product` |  Crea un nuevo producto validando tipos, rangos numéricos y unicidad de `id`. |  `201` |  
| `PUT` |  `/product/{id}` |  Reemplaza todos los atributos del producto especificado. |  `200` |  
| `PATCH` |  `/product/{id}` |  Actualiza parcialmente los atributos enviados del producto. |  `200` |  
| `DELETE` |  `/product/{id}` |  Elimina un producto existente por su `id`. |  `200` |  
  
   
  
---  
**🧪 Ejemplos de Payload (JSON)**  
**Crear un producto (`POST /product`):**  
```  
{  
   "id": 3,  
   "nombre": "Mouse Inalambrico",  
   "categoria": "Perifericos",  
   "precio": 45000.0,  
   "stock": 20  
 }  
   
```  
**Actualización parcial (`PATCH /product/3`):**  
```  
{  
   "precio": 42500.0,  
   "stock": 18  
 }  
   
```  
  
---  
**✨ Validaciones y Manejo de Errores**  
- **`404 Not Found`:** Cuando se intenta consultar, modificar o eliminar un `id` inexistente.  
- **`409 Conflict`:** Cuando se intenta crear un usuario o producto con un `id` que ya existe.  
- **`422 Unprocessable Entity`:** Validación automática de Pydantic (tipos incorrectos, textos vacíos o solo espacios, precios `<= 0` o stock negativo).  
