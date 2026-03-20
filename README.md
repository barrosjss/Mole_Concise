# 🐹 Mole — Limpieza de Mac

Guía paso a paso para limpiar y optimizar tu Mac con [Mole](https://github.com/nicholasgasior/mole).

---

## Archivos del proyecto

| Archivo         | Descripción                                            |
| --------------- | ------------------------------------------------------ |
| `mole_steps.py` | Script interactivo que ejecuta la limpieza paso a paso |
| `index.html`    | Documentación visual                                   |

---

## Requisitos

- **macOS**
- **Python 3** — ya viene instalado en Mac. Verifica con:
  ```bash
  python3 --version
  ```
- **Homebrew** — para instalar Mole. Si no lo tienes:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

---

## Cómo ejecutar el script

### 1. Clona o descarga el repositorio

```bash
git clone https://github.com/barrosjss/Mole_Concise.git
cd Mole_Concise
```

### 2. Ejecuta el script

```bash
python3 mole_steps.py
```

El script te guiará por **5 pasos** en orden:

| Paso | Comando              | Skippable                          |
| ---- | -------------------- | ---------------------------------- |
| 1    | `brew install mole`  | ✅ Si ya tienes `mo`               |
| 2    | `mo clean --dry-run` | ✅ Si ya revisaste antes           |
| 3    | `mo clean`           | ❌ Paso principal                  |
| 4    | `mo purge`           | ✅ Si no hay proyectos que limpiar |
| 5    | `mo optimize`        | ✅ Si acabas de reiniciar          |

> Para **skipear** un paso, escribe `s` y presiona Enter.  
> Para **continuar**, solo presiona Enter.

---

## Cómo ver la documentación web

```bash
# Abre en tu navegador
open index.html
```

---

## Referencia rápida de comandos Mole

| Tarea                           | Comando        |
| ------------------------------- | -------------- |
| Menú interactivo                | `mo`           |
| Limpieza general                | `mo clean`     |
| Borrar instaladores (.dmg/.pkg) | `mo installer` |
| Analizar espacio                | `mo analyze`   |
| Ver salud del sistema           | `mo status`    |
