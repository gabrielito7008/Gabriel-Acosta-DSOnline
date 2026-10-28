ALTAS_TEXTO = """Alba  Requena ;  ALBA.REQUENA@bridge.example ; Data  Science

sergio molina ; sergio.molina@bridge.example ; IA Engineering
Nuria Bel ; nuria.bel.bridge.example ; Data Science
CARLA VIDAL ; carla.vidal @Bridge.Example ; Ciberseguridad
Iván  Tejero ; ivan.tejero@BRIDGE.example ; Data  Science

Marta Sanchís ; MARTA.SANCHIS@BRIDGE.EXAMPLE ; IA Engineering
SERGIO  MOLINA ;  Sergio.Molina@bridge.example  ; IA Engineering
Adrián Gascó ; adrian.gasco@bridge.example ; Ciberseguridad
  Noa Ferrán;noa.ferran@bridge.example;Data Science
Óscar Ibáñez ; oscar.ibanez@bridge.example ; IA Engineering
elena  cortés ; ELENA.CORTES@bridge.example ; Data Science"""

altas_limpias = []
descartes = []
vistos = []

for linea in ALTAS_TEXTO.split("\n"):
    if not linea.strip():
        continue
    
    partes = linea.split(";")
    if len(partes) != 3:
        continue
        
    nombre_raw, correo_raw, programa_raw = partes
    
    nombre = " ".join(nombre_raw.split()).title()
    correo = "".join(correo_raw.split()).lower()
    programa = " ".join(programa_raw.split())
    
    if "@" not in correo or not correo.endswith("@bridge.example"):
        descartes.append([linea, "email_invalido"])
        continue
        
    if correo in vistos:
        descartes.append([linea, "duplicado"])
        continue
        
    vistos.append(correo)
    altas_limpias.append([nombre, correo, programa])

artefacto = {
    "artefacto": "altas_limpias",
    "fuente": "formulario de inscripción",
    "columnas": ["nombre", "email", "programa"],
    "altas": altas_limpias,
    "descartes": descartes,
}

print("Altas válidas:", len(altas_limpias))
print("Descartes:", len(descartes))
