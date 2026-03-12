# Prompt para configurar el teclado Sofle RGB en Linux

## Contexto del proyecto

Tengo un teclado mecánico split Sofle RGB comprado a Zonekeyboards (Chile).
Los keycaps son personalizados con grabado láser, diseñados por mí con layout en inglés.
Firmware: QMK. Bootloader: Caterina (ATmega32U4).
El teclado se identifica como "Arduino LLC Arduino Micro (2341:0037:0001)".

## Layout físico de mis keycaps (lo que está grabado en cada tecla)

### Lado izquierdo
- Fila 1: `~ | 1! | 2@ | 3# | 4$ | 5%
- Fila 2: Tab | Q | W | E | R | T
- Fila 3: Caps | A | S | D | F | G
- Fila 4: Shift | Z | X | C | V | B
- Thumb: Cmd | Alt | Lower | Esc

### Lado derecho
- Fila 1: 6^ | 7& | 8* | 9( | 0) | ← (flecha backspace)
- Fila 2: Y | U | I | O | P | ]}
- Fila 3: H | J | K | L | ;: | '"
- Fila 4: N | M | , | .> | /? | Shift
- Thumb: Space | Upper | Alt | Enter

## Lo que quiero que haga cada tecla

### Comportamiento deseado (capa base)
- **Caps (L13)**: Shift (un toque) — no necesito Caps Lock
- **Shift (L19)**: Ctrl izquierdo
- **Shift (R19)**: Shift derecho (este sí debe ser Shift)
- **Cmd (L25)**: Cmd/Win (KC_LGUI)
- **Alt (L26)**: Alt izquierdo
- **Lower (L27)**: activa capa Lower
- **Esc (L28)**: Escape
- **Space (R28)**: Space
- **Upper (R27)**: activa capa Upper/Raise
- **Alt (R26)**: Alt derecho
- **Enter (R25)**: Enter
- **← (R1)**: Backspace
- Todas las letras, números y símbolos: según lo grabado en el keycap

### Resumen de lo que NO quiero cambiar del firmware actual
El firmware actual (zonekeyboards_en) ya tiene correctamente:
- Todas las letras
- Todos los números y símbolos
- Tab, Esc, Enter, Space, Backspace
- Las capas Lower y Raise con F-keys, símbolos, navegación y numpad
- La capa Adjust con controles RGB

Lo único que necesito verificar/corregir es que L19 sea KC_LCTRL y no KC_LSFT.

## Estado actual del firmware

El archivo `sofle_rev1_zonekeyboards.hex` fue flasheado desde Mac.
En **Linux** el Ctrl funciona correctamente en L19.
En **Mac** L19 actúa como Shift en lugar de Ctrl.

Sospecha: el problema podría ser que el .hex flasheado no es el correcto,
o que solo se flasheó un split del teclado.

## Repo QMK disponible

URL: https://github.com/admfgonzalez/qmk_firmware_0.18.17
Keymap de referencia: `keyboards/sofle/keymaps/zonekeyboards_en/keymap.c`

En ese keymap la línea relevante es:
```c
KC_LCTRL, KC_Z, KC_X, KC_C, KC_V, KC_B, KC_MUTE, ...
```

## Tarea a realizar en Linux

1. Instalar las herramientas necesarias para compilar QMK (avr-gcc, avrdude, make)
2. Clonar el repo de Zonekeyboards
3. Verificar que el keymap `zonekeyboards_en` tiene `KC_LCTRL` en L19
4. Compilar el firmware: `make sofle/rev1:zonekeyboards_en`
5. Flashear ambos splits correctamente usando avrdude con bootloader Caterina
6. Verificar que Ctrl+A funciona en Linux y Mac

## Cómo entrar en modo bootloader

El teclado tiene botones de reset pequeños sobre los conectores jack 3.5mm de cada mitad.
Presionar el botón de reset de la mitad que se quiere flashear.
El teclado aparece brevemente como puerto serial (ej: /dev/ttyACM0) al entrar en bootloader.

Comando de flash típico para Caterina:
```bash
avrdude -p atmega32u4 -c avr109 -P /dev/ttyACM0 -b 57600 -D -U flash:w:sofle_rev1_zonekeyboards.hex:i
```

**Importante**: se deben flashear ambos splits por separado, uno a la vez.
Primero el izquierdo (el que tiene el cable USB), luego el derecho.

## Resultado esperado

El teclado debe funcionar igual en Linux y Mac:
- L13 (keycap "Caps") = Shift
- L19 (keycap "Shift") = Ctrl
- R19 (keycap "Shift") = Shift derecho
- Todas las demás teclas según lo grabado en los keycaps
