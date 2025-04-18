from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(title="Phase Change Diagram API")

# Datos de ejemplo (simulando la curva de saturación P-v)
# Valores ficticios basados en presión (MPa) -> (v_liquid, v_vapor)
PHASE_CHANGE_DATA = {
    0.1: {"specific_volume_liquid": 0.001043, "specific_volume_vapor": 1.694},
    1: {"specific_volume_liquid": 0.001127, "specific_volume_vapor": 0.1944},
    10: {"specific_volume_liquid": 0.0035, "specific_volume_vapor": 0.0035},  # Punto crítico (ejemplo de la trama)
    20: {"specific_volume_liquid": 0.005, "specific_volume_vapor": 0.002},
}

@app.get("/phase-change-diagram")
def get_phase_change_diagram(
    pressure: float = Query(..., description="Pressure in MPa", gt=0)
):
    """Devuelve los volúmenes específicos en el punto de saturación para una presión dada."""
    closest_pressure = min(PHASE_CHANGE_DATA.keys(), key=lambda x: abs(x - pressure))
    return PHASE_CHANGE_DATA[closest_pressure]