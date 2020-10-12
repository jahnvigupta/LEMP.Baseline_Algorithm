var dataset = ee.ImageCollection('MODIS/006/MOD13A1')
                  .filter(ee.Filter.date('2018-01-01', '2018-05-01'));
var ndvi = dataset.select('NDVI');
var ndviVis = {
  min: 0.0,
  max: 9000.0,
  palette: [
    'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
    '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
    '012E01', '011D01', '011301'
  ],
};
Map.setCenter(6.746, 46.529, 2);
Map.addLayer(ndvi, ndviVis, 'NDVI');

var geometry = ee.Geometry.Rectangle([92.125, 8.7497, 101.25025, 28.625]); //these coordinates are for Myanmar, as being used for roads and waterways 

Export.image.toDrive({
  image: ndvi,
  description: 'NDVI',
  folder: "Deforestation Modelling/NDVI",
  scale: 30,
  region: geometry,
  maxPixels: 2506973170,
  fileFormat: "GeoTIFF"
});
