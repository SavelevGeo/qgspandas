import pandas as pd
from qgis.core import QgsVectorLayer
from qgis.utils import iface

if __name__ == 'df_from_active_layer': # if being imported
    layer: QgsVectorLayer = iface.activeLayer()
    assert isinstance(
        layer, QgsVectorLayer), 'A vector layer needs to be selected'
    print(f'{layer} is selected')
