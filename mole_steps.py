#!/usr/bin/env python3
"""
mole_steps.py — Limpieza de Mac con Mole, paso a paso.
Uso: python3 mole_steps.py
"""

import subprocess
import sys

# ── Colores ANSI ──────────────────────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
CYAN   = "\033[36m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
GRAY   = "\033[90m"

# ── Definición de pasos ───────────────────────────────────────────────────────
STEPS = [
    {
        "name":      "Instalación via Homebrew",
        "desc":      "Instala Mole si no lo tienes aún",
        "cmd":       "brew install mole",
        "skippable": True,
        "skip_hint": "Skipea si ya tienes `mo` instalado",
    },
    {
        "name":      "Simulacro (dry-run)",
        "desc":      "Muestra qué se va a borrar sin tocar nada",
        "cmd":       "mo clean --dry-run",
        "skippable": True,
        "skip_hint": "Skipea solo si ya revisaste antes",
    },
    {
        "name":      "Limpieza general",
        "desc":      "Borra cachés, logs y archivos temporales",
        "cmd":       "mo clean",
        "skippable": False,
        "skip_hint": "",
    },
    {
        "name":      "Limpieza de proyectos",
        "desc":      "Borra node_modules / build / target sin uso reciente",
        "cmd":       "mo purge",
        "skippable": True,
        "skip_hint": "Skipea si no tienes proyectos que limpiar",
    },
    {
        "name":      "Optimización del sistema",
        "desc":      "Libera RAM y refresca servicios del sistema",
        "cmd":       "mo optimize",
        "skippable": True,
        "skip_hint": "Skipea si acabas de reiniciar",
    },
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def header():
    print(f"\n{BOLD}{CYAN}╔══════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║   🐹  Mole — Limpieza de Mac     ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════╝{RESET}\n")

def ask_skip(hint: str) -> bool:
    """Devuelve True si el usuario quiere skipear."""
    if hint:
        print(f"  {GRAY}💡 {hint}{RESET}")
    
    # Prompt más visual
    prompt = f"  {BOLD}{YELLOW}s{RESET}: Skip {DIM}|{RESET} {BOLD}{GREEN}Enter{RESET}: Continuar {CYAN}»{RESET} "
    
    try:
        resp = input(prompt).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{RED}Interrumpido.{RESET}")
        sys.exit(1)
    
    print() # Línea en blanco después del input
    return resp == "s"

def run_cmd(cmd: str) -> bool:
    """Ejecuta el comando y devuelve True si fue exitoso."""
    print(f"  {DIM}$ {cmd}{RESET}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0

def step_label(i: int, total: int, name: str) -> str:
    return f"{BOLD}[{i}/{total}] {name}{RESET}"

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    header()
    total   = len(STEPS)
    skipped = []
    failed  = []

    for i, step in enumerate(STEPS, 1):
        print(step_label(i, total, step["name"]))
        print(f"  {GRAY}{step['desc']}{RESET}")

        if step["skippable"]:
            if ask_skip(step["skip_hint"]):
                print(f"  {YELLOW}⏩ Skipped.{RESET}\n")
                skipped.append(step["name"])
                continue
        else:
            print() # Espacio si no hay skip prompt

        ok = run_cmd(step["cmd"])
        if ok:
            print(f"\n  {GREEN}✓ Listo{RESET}\n")
        else:
            print(f"\n  {RED}✗ Falló — revisa el output de arriba{RESET}")
            try:
                cont = input(f"  {YELLOW}¿Continuar de todas formas? (s/n): {RESET}").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print(f"\n{RED}Interrumpido.{RESET}")
                sys.exit(1)
            if cont != "s":
                print(f"\n{RED}Abortado en el paso {i}.{RESET}")
                sys.exit(1)
            failed.append(step["name"])
            print()

    # ── Resumen ───────────────────────────────────────────────────────────────
    print(f"{BOLD}{GREEN}══════════════════════════════════{RESET}")
    print(f"{BOLD}{GREEN}  ✅  Proceso terminado{RESET}")
    print(f"{BOLD}{GREEN}══════════════════════════════════{RESET}")
    if skipped:
        print(f"\n{YELLOW}  Skipeados:{RESET}")
        for s in skipped:
            print(f"    {GRAY}• {s}{RESET}")
    if failed:
        print(f"\n{RED}  Con errores:{RESET}")
        for f in failed:
            print(f"    {RED}• {f}{RESET}")
    print()

if __name__ == "__main__":
    main()
