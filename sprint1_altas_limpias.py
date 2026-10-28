# Bridge SA · Operations — altas de la cohorte de marzo
#
# Script de procesamiento y limpieza de altas para el Sprint 1

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
    # Salta las líneas vacías sin considerarlas descartes
    if not linea.strip():
        continue
    
    partes = linea.split(";")
    if len(partes) != 3:
        continue
        
    nombre_raw, correo_raw, programa_raw = partes
    
    # 1. Limpieza previa (primero se limpia, después se decide)
    nombre = " ".join(nombre_raw.split()).title()
    correo = "".join(correo_raw.split()).lower()
    programa = " ".join(programa_raw.split())
    
    # 2. Validación del correo ("email_invalido")
    if "@" not in correo or not correo.endswith("@bridge.example"):
        descartes.append([linea, "email_invalido"])
        continue
        
    # 3. Comprobación de duplicados ("duplicado")
    if correo in vistos:
        descartes.append([linea, "duplicado"])
        continue
        
    # Registro de alta válida
    vistos.append(correo)
    altas_limpias.append([nombre, correo, programa])

artefacto = {
    "artefacto": "altas_limpias",
    "fuente": "formulario de inscripción",
    "columnas": ["nombre", "email", "programa"],
    "altas": altas_limpias,
    "descartes": descartes,
}

print("--- RESULTADOS DEL PROCESAMIENTO ---")
print("Altas válidas:", len(altas_limpias))
print("Descartes:", len(descartes))
print("\n--- ALTAS LIMPIAS ---")
for alta in altas_limpias:
    print(alta)

print("\n--- DESCARTES ---")
for descarte in descartes:
    print(descarte)
