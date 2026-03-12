# Sofle RGB - Zonekeyboards

Teclado mecánico split Sofle RGB comprado a Zonekeyboards (Chile), con keycaps personalizados de grabado láser diseñados por Roger. Layout en inglés, switches hotswap, firmware QMK.

## Estructura del repositorio

```
keyboard/
├── sofle_keycaps/          # 56 SVGs de los keycaps (L1-L28, R1-R28)
├── sofle_rev1_zonekeyboards.hex  # Firmware enviado por Zonekeyboards
├── ESQUEMA_COLORES_SOFLE_CLEAN.md  # Esquema de colores (Google Docs-compatible)
├── EMAIL_ZONEKEYBOARDS.txt  # Historial de comunicación con proveedor
├── PROMPT_LINUX.md         # Instrucciones para configurar desde Linux
├── generate_keycaps.py     # Script que generó los SVGs
├── SofleV2.pdf             # Manual del teclado
└── CLAUDE.md               # Contexto completo del proyecto para Claude Code
```

## Hardware

- **Modelo**: Sofle RGB rev1
- **Microcontrolador**: ATmega32U4
- **Bootloader**: Caterina (compatible con avrdude)
- **Identificación USB en bootloader**: `Arduino LLC Arduino Micro (2341:0037:0001)`
- **Conexión entre mitades**: Cable TRRS (jack 3.5mm)
- **Botones de reset**: Sobre los conectores jack 3.5mm en cada PCB

## Firmware

- **Base**: QMK firmware
- **Repo Zonekeyboards**: https://github.com/admfgonzalez/qmk_firmware_0.18.17
- **Keymap usado**: `keyboards/sofle/keymaps/zonekeyboards_en/keymap.c`
- **Archivo flasheado**: `sofle_rev1_zonekeyboards.hex`
- **Herramienta de flash**: QMK Toolbox 0.3.3 / avrdude 8.1

### Cómo flashear

1. Conectar ambas mitades vía TRRS y USB
2. Presionar el botón de reset de la mitad derecha (sobre el jack 3.5mm), luego el de la izquierda
3. Abrir QMK Toolbox, seleccionar el `.hex` y hacer flash

### Capa Adjust (para RESET por software)

Activar con **Lower + Upper** simultáneo. La tecla RESET está en la fila 3, última posición del lado derecho (posición `'"`).

## Diseño de keycaps

### Colores por función

| Color | Teclas |
|-------|--------|
| Blanco | Letras alfabéticas: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M |
| Rojo | Números y fila numérica: `` `~ 1! 2@ 3# 4$ 5% 6^ 7& 8* 9( 0) `` |
| Azul | Modificadores y comandos: Tab, Caps, Shift ×2, Cmd, Alt ×2, Esc, Enter, Space, ←, Lower, Upper, `]}`, `'"`, `;:`, `,`, `.>`, `/?` |

### Nomenclatura

- **L1–L28**: lado izquierdo (de arriba a abajo, izquierda a derecha)
- **R1–R28**: lado derecho
- **R1**: SVG especial con ícono de flecha ← (Flowbite), no texto

### Layout físico

```
Izquierdo                          Derecho
─────────────────────────────────────────────────────
L1(`~)  L2(1!) L3(2@) L4(3#) L5(4$) L6(5%)    R6(6^)  R5(7&) R4(8*) R3(9()  R2(0)) R1(←)
L7(Tab) L8(Q)  L9(W)  L10(E) L11(R) L12(T)    R12(Y)  R11(U) R10(I) R9(O)   R8(P)  R7(]})
L13(Caps) L14(A) L15(S) L16(D) L17(F) L18(G)  R18(H)  R17(J) R16(K) R15(L)  R14(;:) R13('")
L19(Shift) L20(Z) L21(X) L22(C) L23(V) L24(B) R24(N)  R23(M) R22(,) R21(.>) R20(/?) R19(Shift)
L25(Cmd) L26(Alt) L27(Lower) L28(Esc)          R28(Space) R27(Upper) R26(Alt) R25(Enter)
```

### Mapeo firmware vs etiqueta

| Etiqueta keycap | Posición | Código QMK | Comportamiento real |
|-----------------|----------|------------|---------------------|
| Caps | L13 | `TD_CAPLOCK` | Tap dance: 1 toque = Shift, doble = Caps Lock |
| Shift (izq) | L19 | `KC_LCTRL` | Ctrl izquierdo |
| Shift (der) | R19 | `KC_RSFT` | Shift derecho |

> El keycap dice "Shift" pero en el firmware L19 es Ctrl. Esto fue una decisión de Zonekeyboards, no un error de diseño del layout.

## Problema sin resolver (Mac)

### Síntoma

En **Mac**, la tecla L19 (etiquetada "Shift", firmware `KC_LCTRL`) actúa como Shift en lugar de Ctrl.

En **Linux**, la misma tecla funciona correctamente como Ctrl.

### Lo que se descartó

- Remapeo en System Preferences > Modifier Keys del Sofle: verificado correcto (Control → Control)
- El problema no es del SO: Linux funciona bien con el mismo hardware y firmware

### Hipótesis activa

El `.hex` enviado por Zonekeyboards podría no corresponder exactamente al firmware que tenían instalado de fábrica, o el flash no afectó ambas mitades de la misma forma.

### Estado

Email enviado a Zonekeyboards. Pendiente respuesta.

Próximo paso si no responden: recompilar firmware desde el repo de Zonekeyboards en Linux y flashear manualmente. Ver `PROMPT_LINUX.md` para instrucciones detalladas.

## Especificaciones técnicas de los SVGs

- **Viewport**: 100×100px
- **Fuente**: sans-serif
- **Color texto**: `#000000` (negro)
- **Fondo**: transparente
- Caracteres especiales correctamente escapados para XML/SVG (`&amp;`, `&lt;`, `&gt;`, `&quot;`, `&#39;`)

### Tamaños de texto por tipo de tecla

| Tipo | Tamaño | Posición Y |
|------|--------|------------|
| 1 carácter | 32px | centrado (50) |
| Dual (carácter superior, ej: `!`) | 24px | 30 |
| Dual (carácter inferior, ej: `1`) | 28px | 70 |
| Palabra modificadora (ej: `Tab`) | 16–18px | centrado (50) |

## Herramientas locales instaladas

- QMK Toolbox 0.3.3
- avrdude 8.1
- avr-gcc (via brew)
- qmk CLI (versión minimal)
- Repo QMK clonado en `~/qmk_firmware`
