from .boole import integracion_boole
from .rect import integracion_rect
from .rect_cen import integracion_rect_cen
from .trap import integracion_trap
from .simpson_1_3 import integracion_simpson_1_3
from .simpson_3_8 import integracion_simpson_3_8

__all__ = [
    'integracion_boole',
    'integracion_rect',
    'integracion_rect_cen',
    'integracion_trap',
    'integracion_simpson_1_3',
    'integracion_simpson_3_8'   
]

