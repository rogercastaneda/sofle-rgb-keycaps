# Firmware v1 — Build Info

## Versión
- QMK: 0.32.3 (oficial)
- Keymap base: `zonekeyboards_en` (portado desde Zonekeyboards QMK 0.18.17)
- Hex: `sofle_rev1_zonekeyboards_en.hex` (compilado en Linux, agregar aquí)

## Compilar

```bash
PATH="$HOME/.local/bin:$PATH" make -C ~/qmk_firmware sofle/rev1:zonekeyboards_en
```

El hex queda en `~/qmk_firmware/sofle_rev1_zonekeyboards_en.hex`.

## Flashear

```bash
sudo systemctl stop ModemManager

avrdude -p atmega32u4 -c avr109 -P /dev/ttyACM0 -b 57600 -D \
  -U flash:w:$HOME/qmk_firmware/sofle_rev1_zonekeyboards_en.hex:i
```

Repetir para cada mitad. Presionar reset (botón sobre el jack 3.5mm) justo antes de ejecutar.

## Cambios de API aplicados (0.18.17 → 0.32.3)

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

También se comentó `RGBLED_SPLIT` y se protegió `RGBLED_NUM` con `#ifndef RGBLIGHT_LED_COUNT` en `config.h`.
