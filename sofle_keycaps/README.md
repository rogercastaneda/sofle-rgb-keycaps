# Sofle RGB Keycap SVG Files

Archivos SVG para las keycaps del teclado Sofle RGB.

## Especificaciones

- **Tamaño**: 100x100px (viewport)
- **Fuente**: Sans-serif
- **Color**: Negro (#000000)
- **Fondo**: Transparente

## Tipos de Teclas

### Teclas con 2 Caracteres (Dual)
Ejemplo: `1!`, `2@`, `3#`
- Carácter superior (shift): 24px, posición Y=30
- Carácter inferior (normal): 28px, posición Y=70

### Teclas con 1 Carácter
Ejemplo: `Q`, `W`, `E`
- Tamaño: 32px
- Centrado horizontal y vertical

### Teclas con Palabras (Modificadoras)
Ejemplo: `Tab`, `Shift`, `Enter`
- Tamaño: 16-18px (según longitud)
- Centrado horizontal y vertical

## Layout del Teclado

### Lado Izquierdo (L1-L28)
```
Fila 1: L1(`~)  L2(1!)  L3(2@)  L4(3#)  L5(4$)  L6(5%)
Fila 2: L7(Tab) L8(Q)   L9(W)   L10(E)  L11(R)  L12(T)
Fila 3: L13(Caps) L14(A) L15(S) L16(D)  L17(F)  L18(G)
Fila 4: L19(Shift) L20(Z) L21(X) L22(C) L23(V)  L24(B)
Fila 5: L25(Cmd) L26(Alt) L27(Lower) L28(Esc)
```

### Lado Derecho (R1-R28)
```
Fila 1: R6(6^)  R5(7&)  R4(8*)  R3(9()  R2(0))  R1(Back)
Fila 2: R12(Y)  R11(U)  R10(I)  R9(O)   R8(P)   R7(]})
Fila 3: R18(H)  R17(J)  R16(K)  R15(L)  R14(;:) R13('")
Fila 4: R24(N)  R23(M)  R22(,)  R21(.>) R20(/?) R19(Shift)
Fila 5: R28(Space) R27(Upper) R26(Alt) R25(Enter)
```

## Archivos Generados

Total: 56 archivos SVG

**Lado Izquierdo**: L1.svg - L28.svg
**Lado Derecho**: R1.svg - R28.svg

## Uso

Estos archivos SVG están diseñados para ser grabados en keycaps de teclado mecánico. Son escalables y mantienen la legibilidad en diferentes tamaños.

## Caracteres Especiales Escapados

Los siguientes caracteres están correctamente escapados para XML/SVG:
- `&` → `&amp;`
- `<` → `&lt;`
- `>` → `&gt;`
- `"` → `&quot;`
- `'` → `&#39;`
