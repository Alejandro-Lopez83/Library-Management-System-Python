# 📚 Library Management System Python

[![English](https://img.shields.io/badge/lang-English-blue.svg)](#english) [![Español](https://img.shields.io/badge/lang-Espa%C3%B1ol-red.svg)](#español)

A simple Python application to manage a library's book collection and borrowing operations.

<a name="english"></a>
## 🚀 Features

- Add new books to the library inventory
- Borrow books using ISBN identification
- Return previously borrowed books
- Display the complete book catalog with availability status
- Search for specific books by ISBN
- ISBN validation to ensure data integrity

## 💻 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```

3. Run the application:
   ```bash
   python library_system.py
   ```

## 🖥️ Usage

The application provides a simple menu-driven interface:

```
*************** LIBRARY SYSTEM MENU ***************
1 - Add book
2 - Borrow book
3 - Return book
4 - Show all books
5 - Search by ISBN
6 - Exit
```

### Adding a Book

When adding a book, you'll need to provide:
- Title
- Author
- ISBN (must be 13 digits according to international standards)

### ISBN Validation

The system implements ISBN-13 validation according to international standards:
- Removes hyphens and spaces automatically
- Ensures exactly 13 numeric digits are present
- Prevents duplicate ISBNs in the library

## 🧩 Code Structure

- `Book` class: Manages all book-related operations
- `display_menu()`: Handles the user interface
- `main()`: Orchestrates the program's flow

## 📋 Requirements

- Python 3.6 or higher

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<a name="español"></a>
# 📚 Sistema de Gestión de Biblioteca

[![English](https://img.shields.io/badge/lang-English-blue.svg)](#english) [![Español](https://img.shields.io/badge/lang-Espa%C3%B1ol-red.svg)](#español)

Una aplicación simple en Python para gestionar una colección de libros de biblioteca y sus operaciones de préstamo.

## 🚀 Características

- Añadir nuevos libros al inventario de la biblioteca
- Prestar libros usando identificación ISBN
- Devolver libros previamente prestados
- Mostrar el catálogo completo de libros con estado de disponibilidad
- Buscar libros específicos por ISBN
- Validación de ISBN para garantizar la integridad de los datos

## 💻 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/sistema-gestion-biblioteca.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd sistema-gestion-biblioteca
   ```

3. Ejecuta la aplicación:
   ```bash
   python sistema_biblioteca.py
   ```

## 🖥️ Uso

La aplicación proporciona una interfaz sencilla basada en menú:

```
*************** MENÚ SISTEMA LIBROS ***************
1 - Agregar libro
2 - Prestar libro
3 - Devolver libro
4 - Mostrar libros
5 - Buscar por ISBN
6 - Salir
```

### Añadir un Libro

Al añadir un libro, necesitarás proporcionar:
- Título
- Autor
- ISBN (debe tener 13 dígitos según los estándares internacionales)

### Validación de ISBN

El sistema implementa validación de ISBN-13 según los estándares internacionales:
- Elimina automáticamente guiones y espacios
- Asegura que estén presentes exactamente 13 dígitos numéricos
- Evita ISBN duplicados en la biblioteca

## 🧩 Estructura del Código

- Clase `Book`: Gestiona todas las operaciones relacionadas con los libros
- `display_menu()`: Maneja la interfaz de usuario
- `main()`: Orquesta el flujo del programa

## 📋 Requisitos

- Python 3.6 o superior

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
