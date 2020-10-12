var dataset = ee.ImageCollection('MODIS/006/MOD13A1')
                  .filter(ee.Filter.date('2018-01-01', '2018-05-01'));
var evi = dataset.select('EVI');

var geometry = ee.Geometry.Rectangle([92.125, 8.7497, 101.25025, 28.625]); //these coordinates are for Myanmar, as being used for roads and waterways 

Export.image.toDrive({
  image: evi.mean(),
  description: 'EVI',
  folder: "Deforestation Modelling/EVI",
  scale: 30,
  region: geometry,
  maxPixels: 2506973170,
  fileFormat: "GeoTIFF"
});
