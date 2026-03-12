# Proyecto: Teclado Sofle RGB - Zonekeyboards

## Contexto general
Teclado mecánico split Sofle RGB comprado a Zonekeyboards (Chile).
Keycaps personalizados con grabado láser, diseñados por Roger con layout en inglés.
Switches hotswap (intercambiables).
Firmware: QMK

## Archivos del proyecto
- `sofle_keycaps/` — 56 archivos SVG de los keycaps (L1-L28, R1-R28)
- `sofle_rev1_zonekeyboards.hex` — Firmware enviado por Zonekeyboards
- `ESQUEMA_COLORES_SOFLE_CLEAN.md` — Esquema de colores de keycaps (sin ASCII art, para Google Docs)
- `EMAIL_ZONEKEYBOARDS.txt` — Email enviado a Zonekeyboards pidiendo ayuda
- `~/qmk_firmware/` — Repo QMK de Zonekeyboards clonado localmente

## Layout de keycaps diseñado

### Colores
- Blanco: letras alfabéticas (Q W E R T Y U I O P A S D F G H J K L Z X C V B N M)
- Rojo: números y fila numérica (`~ 1! 2@ 3# 4$ 5% 6^ 7& 8* 9( 0))
- Azul: comandos y modificadores (Tab, Caps, Shift x2, Cmd, Alt x2, Esc, Enter, Space, ← Back, Lower, Upper, ]}, '", ;:, ,, .>, /?)

### Nomenclatura
- L1-L28: lado izquierdo
- R1-R28: lado derecho
- R1 usa un SVG con flecha ← de Flowbite en lugar de texto

## Problema actual (sin resolver)

### Síntoma
La tecla etiquetada "Shift" (L19, fila inferior izquierda) no funciona como Ctrl en Mac.
La tecla etiquetada "Caps" (L13) actúa como Shift (tap dance: un toque = Shift, doble = Caps Lock).

### Comportamiento por sistema operativo
- **Linux**: Ctrl funciona correctamente en la posición L19
- **Mac**: L19 actúa como Shift, no como Ctrl

### Lo que se hizo
1. Se flasheó `sofle_rev1_zonekeyboards.hex` usando QMK Toolbox 0.3.3
2. Para entrar en bootloader se presionaron botones pequeños sobre los conectores jack 3.5mm (primero derecho, luego izquierdo) — se asume que son botones de reset, no mencionados en el PDF oficial
3. Flash exitoso: avrdude escribió y verificó 26680 bytes (Caterina/ATmega32U4)
4. El problema persiste en Mac después del flash

### Análisis del firmware
Repo de Zonekeyboards: https://github.com/admfgonzalez/qmk_firmware_0.18.17
Keymap usado: `keyboards/sofle/keymaps/zonekeyboards_en/keymap.c`

En el keymap, L19 tiene `KC_LCTRL` (línea 117/121).
Sin embargo en Mac esa tecla actúa como Shift, no como Ctrl.

Hipótesis: el `.hex` enviado por Zonekeyboards podría no corresponder al firmware
que tenían instalado originalmente, o el flash no afectó ambos splits correctamente.

### Estado actual
Email enviado a Zonekeyboards con 3 preguntas:
1. ¿El .hex enviado es el mismo que usaron originalmente?
2. ¿El orden de los botones de reset importa?
3. ¿Hay algún paso adicional post-flash?

**Esperando respuesta.**

## Configuración Mac verificada
- Modifier Keys del Sofle en Mac: todo correcto (Control → Control, sin remapeos)
- El problema no es de configuración del sistema operativo

## Herramientas instaladas
- QMK Toolbox 0.3.3
- avrdude 8.1
- avr-gcc (via brew)
- qmk CLI (versión minimal, solo config/clone/console/env/setup)
- Repo QMK clonado en ~/qmk_firmware

## Repo QMK Zonekeyboards
- URL: https://github.com/admfgonzalez/qmk_firmware_0.18.17
- Keymaps disponibles: zonekeyboards, zonekeyboards_en, zonekeyboards_NB, zonekeyboards_win_cl, etc.
- RESET en capa Adjust: fila 3, última tecla lado derecho (posición `'"`)
- Adjust se activa con: Lower + Upper simultáneo

## Notas adicionales
- Los botones de reset están sobre los conectores jack 3.5mm de cada mitad
- El PDF que viene en la caja (QR) no menciona estos botones
- VIA (usevia.app) y Vial no detectan el teclado con el firmware actual
- El teclado se identifica como "Arduino LLC Arduino Micro (2341:0037:0001)" en bootloader
- Bootloader: Caterina (ATmega32U4)
