# Sofle RGB - Zonekeyboards

Teclado mecánico split Sofle RGB comprado a Zonekeyboards (Chile), con keycaps personalizados de grabado láser diseñados por Roger. Layout en inglés, switches hotswap, firmware QMK.

## Estructura del repositorio

```
sofle-rgb-keycaps/
├── firmware/
│   └── v1/
│       ├── keymap.md                        # Distribución completa de teclas por capa
│       ├── build.md                         # Versión QMK, comando de compilación, cambios de API
│       └── sofle_rev1_zonekeyboards_en.hex  # Hex compilado (copiar desde Linux)
├── sofle_keycaps/      # 56 SVGs de los keycaps (L1-L28, R1-R28)
├── generate_keycaps.py # Script que generó los SVGs
├── SofleV2.pdf         # Manual del teclado
└── CLAUDE.md           # Contexto del proyecto para Claude Code
```

El firmware compilado y activo vive en `~/qmk_firmware/` (Linux).

---

## Hardware

- **Modelo**: Sofle RGB rev1
- **Microcontrolador**: ATmega32U4
- **Bootloader**: Caterina (compatible con avrdude)
- **Identificación USB en bootloader**: `Arduino LLC Arduino Micro (2341:0037:0001)`
- **Conexión entre mitades**: Cable TRRS (jack 3.5mm)
- **Botones de reset**: Sobre los conectores jack 3.5mm en cada PCB
- **Encoders**: Dos perillas (knobs), una por mitad

---

## Setup en Linux (lo que fue necesario instalar)

Sistema: Debian 12 (bookworm)

```bash
# Compilador AVR
sudo apt-get install gcc-avr avr-libc

# Herramienta de flash
sudo apt-get install avrdude

# QMK CLI (sin sudo, usuario local)
pip3 install --user --break-system-packages qmk

# Setup inicial de QMK (clona el repo oficial con submodules)
~/.local/bin/qmk setup -y
# Esto crea ~/qmk_firmware con QMK 0.32.3

# udev rules para que Linux reconozca el teclado en modo bootloader
sudo cp ~/qmk_firmware/util/udev/50-qmk.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules

# Desactivar ModemManager (interfiere con bootloader Caterina)
sudo systemctl stop ModemManager
```

### Por qué no se usó el repo de Zonekeyboards directamente

El repo de Zonekeyboards (`admfgonzalez/qmk_firmware_0.18.17`) es un fork de QMK 0.18.17 que no incluye los submodules (lib/lufa, lib/chibios, etc.) en el push. Su Makefile tampoco es compatible con el QMK CLI moderno (usa comandos como `generate-layouts` que ya no existen).

Solución: usar el QMK oficial 0.32.3 (`~/qmk_firmware`) y copiar el keymap de Zonekeyboards ahí, corrigiendo las incompatibilidades de API.

---

## Firmware

- **Base usada para compilar**: QMK 0.32.3 (oficial, `~/qmk_firmware`)
- **Keymap**: `~/qmk_firmware/keyboards/sofle/keymaps/zonekeyboards_en/`
- **Hex generado**: `~/qmk_firmware/sofle_rev1_zonekeyboards_en.hex`
- **Tamaño**: 27264 / 28672 bytes (95%, 1408 bytes libres)

### Cambios de API aplicados al keymap (0.18.17 → 0.32.3)

| Antes | Después |
|-------|---------|
| `qk_tap_dance_action_t` | `tap_dance_action_t` |
| `KC_LCTRL` | `KC_LCTL` |
| `KC_RCTRL` | `KC_RCTL` |
| `KC_PGDOWN` | `KC_PGDN` |
| `KC__VOLUP` | `KC_VOLU` |
| `KC__VOLDOWN` | `KC_VOLD` |
| `KC__MUTE` | `KC_MUTE` |
| `RGB_TOG` | `UG_TOGG` |
| `RGB_HUI/HUD` | `UG_HUEU/HUED` |
| `RGB_SAI/SAD` | `UG_SATU/SATD` |
| `RGB_VAI/VAD` | `UG_VALU/VALD` |
| `RGB_SPI/SPD` | `UG_SPDU/SPDD` |
| `RGB_MOD` | `UG_NEXT` |
| `RESET` | `QK_BOOT` |
| `OLED_DRIVER = SSD1306` | `OLED_DRIVER = ssd1306` |
| `tap_code(KC_PGDN)` | `tap_code16(KC_PGDN)` |

También se comentó `RGBLED_SPLIT` y se protegió `RGBLED_NUM` con `#ifndef RGBLIGHT_LED_COUNT` en `config.h` para evitar redefiniciones con el nuevo sistema de info.json.

---

## Compilar el firmware

```bash
PATH="$HOME/.local/bin:$PATH" make -C ~/qmk_firmware sofle/rev1:zonekeyboards_en
```

El hex queda en `~/qmk_firmware/sofle_rev1_zonekeyboards_en.hex`.

---

## Flashear el teclado

Se flashea cada mitad por separado. El cable TRRS puede estar conectado o no durante el flash.

```bash
# Detener ModemManager antes de flashear (interfiere con Caterina)
sudo systemctl stop ModemManager

# Comando de flash (mismo para ambas mitades)
avrdude -p atmega32u4 -c avr109 -P /dev/ttyACM0 -b 57600 -D \
  -U flash:w:$HOME/qmk_firmware/sofle_rev1_zonekeyboards_en.hex:i
```

### Proceso paso a paso

1. Conectar USB a la mitad a flashear
2. Escribir el comando de avrdude en la terminal (sin ejecutar aún)
3. Presionar el botón de reset de esa mitad (sobre el jack 3.5mm)
4. Ejecutar el comando inmediatamente — hay ~8 segundos antes de que salga del modo bootloader
5. Esperar confirmación: `avrdude done. Thank you.`
6. Repetir para la otra mitad

> Si el puerto no es `/dev/ttyACM0`, verificarlo con `ls /dev/ttyACM*` justo después del reset.

---

## Uso normal del teclado

- **USB**: siempre conectado a la **mitad izquierda** (es el master, definido por `MASTER_LEFT` en config.h)
- **TRRS**: conecta ambas mitades, necesario para que funcionen las dos
- **OLED izquierdo**: muestra capa activa
- **OLED derecho**: muestra logo — solo se activa cuando el TRRS está conectado al master (izquierda)

---

## Keymap actual

Ver `firmware/v1/keymap.md` para la distribución completa de teclas por capa.

### Resumen rápido

```
Izquierdo                              Derecho
──────────────────────────────────────────────────────────
L1(Esc)  L2(1!) L3(2@) L4(3#) L5(4$) L6(5%)    R6(6^) R5(7&) R4(8*) R3(9() R2(0)) R1(←Bksp)
L7(Tab)  L8(Q)  L9(W)  L10(E) L11(R) L12(T)    R12(Y) R11(U) R10(I) R9(O)  R8(P)  R7(}])
L13(Shft)L14(A) L15(S) L16(D) L17(F) L18(G)    R18(H) R17(J) R16(K) R15(L) R14(;:)R13({[)
L19(Ctrl)L20(Z) L21(X) L22(C) L23(V) L24(B)    R24(N) R23(M) R22(,) R21(.>)R20(-_)R19('")
L25(Alt) L26(`~)L27(Lwr)L28(Cmd)L29(Spc)       R29(Ent)R28(Upr)R27(\|)R26(/?)R25(=+)
```

### Capas

- **Lower** (mantener L27): F-keys izquierda, símbolos, numpad derecho, controles de media
- **Upper** (mantener R28): F-keys izquierda, flechas y navegación derecha
- **Adjust** (Lower + Upper simultáneo): controles RGB, QK_BOOT para reset por software

### Encoders (perillas)

| Encoder | Capa base | Lower / Upper |
|---------|-----------|---------------|
| Izquierdo (giro) | Volumen +/- | Volumen +/- |
| Derecho (giro) | Page Up / Page Down | Flecha Arriba / Abajo |

---

## Botón de reset

El botón de reset **no borra el keymap**. Solo pone el microcontrolador en modo bootloader para recibir un nuevo firmware. Si no se flashea nada en los ~8 segundos siguientes, el teclado vuelve a funcionar normal con el firmware que ya tenía.

---

## Herramientas instaladas (Linux)

| Herramienta | Versión | Instalación |
|-------------|---------|-------------|
| gcc-avr | 5.4.0 | `sudo apt-get install gcc-avr avr-libc` |
| avrdude | 7.1 | `sudo apt-get install avrdude` |
| qmk CLI | 1.2.0 | `pip3 install --user --break-system-packages qmk` |
| QMK firmware | 0.32.3 | `~/.local/bin/qmk setup -y` → `~/qmk_firmware` |
