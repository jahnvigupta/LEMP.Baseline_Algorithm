
var dataset = ee.Image('NASA/JPL/global_forest_canopy_height_2005');
var forestCanopyHeight = dataset.select('1');
var forestCanopyHeightVis = {
  min: 0.0,
  max: 30.0,
  region: ee.Geometry.Rectangle([92.125, 8.749749999999999, 101.25025, 28.625]),
  palette: [
    'ffffff', 'fcd163', '99b718', '66a000', '3e8601', '207401', '056201',
    '004c00', '011301'
  ],
};

Map.setCenter(92.125, 8.7497, 1);
Map.addLayer(forestCanopyHeight, forestCanopyHeightVis, 'Forest Canopy Height');
var geometry = ee.Geometry.Rectangle([92.125, 8.7497, 101.25025, 28.625]); //these coordinates are for Myanmar, as being used for roads and waterways 

Export.image.toDrive({
  image: forestCanopyHeight,
  description: 'Forest_Canopy_Height',
  folder: "Deforestation Modelling/Forest Canopy Height",
  scale: 30,
  region: geometry,
  maxPixels: 2506973170,
  fileFormat: "GeoTIFF"
});

// var multiPoint = ee.Geometry.MultiPoint([[-121.68, 39.91], [-97.38, 40.34]]);
// Map.addLayer(multiPoint)
