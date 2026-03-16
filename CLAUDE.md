# Proyecto: Teclado Sofle RGB - Zonekeyboards

## Contexto general
Teclado mecánico split Sofle RGB comprado a Zonekeyboards (Chile).
Keycaps personalizados con grabado láser, diseñados por Roger con layout en inglés.
Switches hotswap (intercambiables). Firmware: QMK.

## Estado del proyecto
Resuelto. El firmware fue compilado y flasheado exitosamente desde Linux (Debian 12).
El teclado funciona correctamente con el keymap documentado en `TEST_KEYMAP.md`.

## Archivos del proyecto
- `sofle_keycaps/` — 56 archivos SVG de los keycaps (L1-L28, R1-R28)
- `firmware/v1/keymap.md` — Distribución completa de teclas por capa
- `firmware/v1/build.md` — Versión QMK, comando de compilación, cambios de API
- `firmware/v1/sofle_rev1_zonekeyboards_en.hex` — Hex compilado (pendiente copiar desde Linux)
- `generate_keycaps.py` — Script que generó los SVGs
- `SofleV2.pdf` — Manual del teclado
- `~/qmk_firmware/` — QMK 0.32.3 con el keymap activo (en Linux)

## Hardware
- Modelo: Sofle RGB rev1
- Microcontrolador: ATmega32U4
- Bootloader: Caterina
- Identificación USB en bootloader: `Arduino LLC Arduino Micro (2341:0037:0001)`
- Botones de reset: sobre los conectores jack 3.5mm en cada PCB
- USB: siempre a la mitad izquierda (MASTER_LEFT)

## Firmware activo
- Base: QMK 0.32.3 oficial (`~/qmk_firmware` en Linux)
- Keymap: `~/qmk_firmware/keyboards/sofle/keymaps/zonekeyboards_en/`
- Compilar: `PATH="$HOME/.local/bin:$PATH" make -C ~/qmk_firmware sofle/rev1:zonekeyboards_en`
- Hex generado: `~/qmk_firmware/sofle_rev1_zonekeyboards_en.hex`

El keymap original de Zonekeyboards (QMK 0.18.17) fue portado a QMK 0.32.3.
Los cambios de API aplicados están documentados en el README.

## Keymap — capa base

```
Izquierdo                                Derecho
──────────────────────────────────────────────────────────────
L1(Esc)   L2(1!)  L3(2@) L4(3#) L5(4$) L6(5%)   R6(6^) R5(7&) R4(8*) R3(9()  R2(0)) R1(←Bksp)
L7(Tab)   L8(Q)   L9(W)  L10(E) L11(R) L12(T)   R12(Y) R11(U) R10(I) R9(O)   R8(P)  R7(}])
L13(Shift)L14(A)  L15(S) L16(D) L17(F) L18(G)   R18(H) R17(J) R16(K) R15(L)  R14(;:)R13({[)
L19(Ctrl) L20(Z)  L21(X) L22(C) L23(V) L24(B)   R24(N) R23(M) R22(,) R21(.>) R20(-_)R19('")
L25(Alt)  L26(`~) L27(Lower) L28(Cmd) L29(Space) R29(Enter) R28(Upper) R27(\|) R26(/?) R25(=+)
```

- L13 (Shift): tap dance — 1 toque = Shift, doble = Caps Lock
- Lower + Upper simultáneo = capa Adjust (RGB + QK_BOOT)

## Diseño de keycaps

### Colores
- Blanco: letras alfabéticas (A-Z)
- Rojo: números y fila numérica (`` `~ 1! 2@ 3# 4$ 5% 6^ 7& 8* 9( 0) ``)
- Azul: modificadores y comandos (Tab, Caps/Shift, Ctrl, Alt, Cmd, Esc, Enter, Space, ←, Lower, Upper, `]}`, `'"`, `;:`, `,`, `.>`, `/?`)

### Nomenclatura SVG
- L1-L28: lado izquierdo
- R1-R28: lado derecho
- R1: ícono de flecha ← (Flowbite), no texto

## Notas importantes
- VIA y Vial no son compatibles con este firmware
- El botón de reset no borra el keymap; solo entra en modo bootloader ~8 segundos
- Para flashear: detener ModemManager (`sudo systemctl stop ModemManager`) antes de avrdude
- El repo de Zonekeyboards no tiene submodules; no compilar desde ahí
