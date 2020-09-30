import rasterio
import matplotlib.pyplot as plt
from osgeo import gdal
import rasterio.plot

def visualiseRasterDataFromFile(path, title, xlabel, ylabel):
  """
      It visualises a raster layer.

  Input:
      path: path of the raster layer to be visualised
      title: titl of the plot
      xlabel: xlabel of the plot
      ylabel: ylabel of the plot
      
  Output: 
      No Output
      
  """
  src = rasterio.open(path)
  oview=9
  thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))
  plt.imshow(thumbnail)
  plt.colorbar()
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

def GetExtent(path):
    """
      It gives the latitude and longitude of four corners of the layer.

    Input:
        path: path of the layer for which coordinates need to be found.
        
    Output: 
        ext: List containing coordinates of all corners
        
    """
    ds=gdal.Open(path)
    gt=ds.GetGeoTransform()
    cols = ds.RasterXSize
    rows = ds.RasterYSize
    ext=[]
    xarr=[0,cols]
    yarr=[0,rows]

    for px in xarr:
        for py in yarr:
            x=gt[0]+(px*gt[1])+(py*gt[2])
            y=gt[3]+(px*gt[4])+(py*gt[5])
            ext.append([x,y])
        yarr.reverse()
    return ext

def poly_to_prox(file_name, input_filepath, raster_filepath, output_filepath):
  """
      It converts a given polygon layer to proximty distance.

  Input:
      file_name: Name of the file for which proximity distance is to be calculated.
      input_filepath: Path of the file for which proximity distance is to be calculated.
      raster_filepath: Path where polygon layer converted to raster layer is stored.
      output_filepath: Path where proximity distance layer is stored.
      
  Output: 
      No Output
      
  """
  #creating raster layer of polygon
  gdal_rasterize -l file_name -a osm_id -ts 36501.0 79501.0 -a_nodata 0.0 -te 92.125 8.74975 101.25025 28.625 -ot Byte -of GTiff input_filepath raster_filepath
  #Creating proximity layer of raster layer
  gdal_proximity.py -srcband 1 -distunits PIXEL -nodata 0.0 -ot Int16 -of GTiff  raster_filepath output_filepath


def extractWindowedDataAndSaveData(input_path, output_path, col_off, row_off, width, height):
  """
      It extracts a window from a raster with given parameters.

    Input:
        input_path: path of the layer for which window needs to be extracted.
        output_path: path of the raster file where window is stored.
        col_off: column off of window in raster layer.
        row_off: row off of window in raster layer.
        width: width of window.
        height: height of window.
        
    Output: 
        No Output
        
    """
  window_ = rasterio.windows.Window(col_off=col_off, row_off=row_off, width=width, height=height)
  file = rasterio.open(input_path)
  out_profile = file.profile.copy()
  out_profile['width']=window_.width
  out_profile['height']=window_.height
  dst = rasterio.open(output_path, 'w', **out_profile)
  dst.write(file.read(window=window_))
  print("Completed extraction of window to new file")