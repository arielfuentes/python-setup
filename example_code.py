#libraries
import geopandas as gpd
import fiona
from plotnine import *
#kmldata
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
zn_rrl = gpd.read_file('data\\rural_rancagua.kml', driver='KML')
zn_rrl.head()
zn_stgo = gpd.read_file('data\\a stgo.kml', driver='KML')
zn_stgo.head()
(ggplot() + 
  geom_map(zn_rrl) + 
  geom_map(zn_stgo))
