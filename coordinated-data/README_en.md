# Coordinated energy datasets for municipalities

(Norwegian)[README_no.md]

The datasets in this directory are coordinated based on data sources from the municipalities.

There are four types of data sets that belong together.
- Location: Describes a location (usually a building) that has energy data.
- MeasurementPoint: Describes a measurement point with a unique id, what it is and the unit measurements are performed in.
- LocationMeasurementPoint: Connects a measurement point with a location and assigns a local namee for the measurement point. Some measurement points are used by multiple locations, e.g. for temperature measurements from official measurement stations from met.no.
- Measurements: Timestamped measurements from measurement points.

A description of each dataset with their attributes are given below.

## Location
| Attribute | Description  |
| --------- | ------------ |
| location | Name of the location, e.g. name of a school or daycare |
| municipality_code | The municipality code for the location. The codes are defined in the data set [Standard for kommuneinndeling](https://www.ssb.no/klass/klassifikasjoner/131/koder) at SSB. |
| location_type | Type of locatinn. Valid values are : Bygning (Building), Rom (Room), Annet (Other) |
| building_type | Type of building. Legal values : Skole (School), Barnehage (Daycare), Helsebygg (Health), Administrasjonsbygg (Admin), Idrettsbygg (Sports), Kirkelig bygg (Religious), Beredskapsbygg (Emergency response), Bydels- og fritidsbygg (Community), Kulturbygg (Culture), Varmesentral (Heat central), Annet bygg (Other) |
| address | Adress for the location / building |
| latitude | Latitude for the location in decimal degrees |
| longitude | Longitude for the lcoation in decimal degrees |
 
## MeasurementPoint
| Attribute | Description  |
| --------- | ------------ |
| meter_id | Unique id for the measurement point. Examples: EID_972418013_00290, Eklima_82290_TAM |
| meter_type | Description of what type of measurement point this is. Examples are Fastkraft, Temperatur, Graddager, Varmepumpe |
| unit | The unit for the measurement, e.g. kWh, °C |
| meter_level | Usually one of the following values: Consumption meter, Other meter |
 
## LocationMeasurementPoint
| Attribute | Description  |
| --------- | ------------ |
| location | Name of the lcoation (see Location) |
| municipality_code | The municipality code of the location |
| meter_id | Unique id for the measurement point (see MeasurementPoint) |
| meter_name | Local name for the measurement point (unique only within the location). Examples: Temp middel, Fastkraft, Fastkraft 67756 |
 
## Measurements
| Attribute | Description  |
| --------- | ------------ |
| timestamp | Timestamp with date and time, e.g. 2010-01-04 06:00:00 |
| meter_id | Unique id for the measurement point (se MeasurementPoint) |
| value | A single measurement from the meter. Usually a floating point value, with comma as separator, e.g. 4,20 |
 
