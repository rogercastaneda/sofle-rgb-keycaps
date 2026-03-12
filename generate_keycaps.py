#!/usr/bin/env python3
"""
Script para generar archivos SVG para keycaps del teclado Sofle RGB
"""

import os
from pathlib import Path

# Definir el layout del teclado
LEFT_SIDE = {
    "L1": ("`", "~"),
    "L2": ("1", "!"),
    "L3": ("2", "@"),
    "L4": ("3", "#"),
    "L5": ("4", "$"),
    "L6": ("5", "%"),
    "L7": "Tab",
    "L8": "Q",
    "L9": "W",
    "L10": "E",
    "L11": "R",
    "L12": "T",
    "L13": "Caps",
    "L14": "A",
    "L15": "S",
    "L16": "D",
    "L17": "F",
    "L18": "G",
    "L19": "Shift",
    "L20": "Z",
    "L21": "X",
    "L22": "C",
    "L23": "V",
    "L24": "B",
    "L25": "Cmd",
    "L26": "Alt",
    "L27": "Lower",
    "L28": "Esc",
}

RIGHT_SIDE = {
    "R1": "Back",
    "R2": ("0", ")"),
    "R3": ("9", "("),
    "R4": ("8", "*"),
    "R5": ("7", "&"),
    "R6": ("6", "^"),
    "R7": ("]", "}"),
    "R8": "P",
    "R9": "O",
    "R10": "I",
    "R11": "U",
    "R12": "Y",
    "R13": ("'", '"'),
    "R14": (";", ":"),
    "R15": "L",
    "R16": "K",
    "R17": "J",
    "R18": "H",
    "R19": "Shift",
    "R20": ("/", "?"),
    "R21": (".", ">"),
    "R22": ",",
    "R23": "M",
    "R24": "N",
    "R25": "Enter",
    "R26": "Alt",
    "R27": "Upper",
    "R28": "Space",
}

def escape_xml(text):
    """Escapar caracteres especiales para XML/SVG"""
    replacements = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def create_single_char_svg(char):
    """SVG para teclas con un solo carácter (centrado, 32px)"""
    char_escaped = escape_xml(char)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <text x="50" y="50" font-family="sans-serif" font-size="32" fill="#000000" text-anchor="middle" dominant-baseline="central">{char_escaped}</text>
</svg>'''

def create_word_svg(word):
    """SVG para palabras (centrado, 16-18px dependiendo de la longitud)"""
    # Ajustar tamaño de fuente según longitud
    font_size = 16 if len(word) > 5 else 18
    word_escaped = escape_xml(word)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <text x="50" y="50" font-family="sans-serif" font-size="{font_size}" fill="#000000" text-anchor="middle" dominant-baseline="central">{word_escaped}</text>
</svg>'''

def create_dual_char_svg(bottom, top):
    """SVG para teclas con 2 caracteres (normal abajo 28px, shift arriba 24px)"""
    bottom_escaped = escape_xml(bottom)
    top_escaped = escape_xml(top)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <text x="50" y="30" font-family="sans-serif" font-size="24" fill="#000000" text-anchor="middle" dominant-baseline="central">{top_escaped}</text>
  <text x="50" y="70" font-family="sans-serif" font-size="28" fill="#000000" text-anchor="middle" dominant-baseline="central">{bottom_escaped}</text>
</svg>'''

def generate_svg_content(value):
    """Generar contenido SVG según el tipo de tecla"""
    if isinstance(value, tuple):
        # Tecla con 2 caracteres (normal, shift)
        return create_dual_char_svg(value[0], value[1])
    elif len(value) == 1:
        # Tecla con un solo carácter
        return create_single_char_svg(value)
    else:
        # Palabra (tecla modificadora)
        return create_word_svg(value)

def main():
    # Crear directorio de salida
    output_dir = Path("sofle_keycaps")
    output_dir.mkdir(exist_ok=True)

    # Generar archivos para lado izquierdo
    print("Generando archivos para lado izquierdo...")
    for key, value in LEFT_SIDE.items():
        svg_content = generate_svg_content(value)
        output_file = output_dir / f"{key}.svg"
        output_file.write_text(svg_content)
        print(f"  Creado: {output_file}")

    # Generar archivos para lado derecho
    print("\nGenerando archivos para lado derecho...")
    for key, value in RIGHT_SIDE.items():
        svg_content = generate_svg_content(value)
        output_file = output_dir / f"{key}.svg"
        output_file.write_text(svg_content)
        print(f"  Creado: {output_file}")

    print(f"\n✅ Completado! {len(LEFT_SIDE) + len(RIGHT_SIDE)} archivos SVG creados en {output_dir}/")

if __name__ == "__main__":
    main()
