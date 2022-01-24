# Samordnede energidatasett for kommunene

Datasettene i denne katalogen er samordnet basert på kiledata fra kommunene.

Det er fire typer datasett som hører sammen.
- Location: Beskriver en lokasjon (vanligvis et bygg) som det finnes energidata for.
- MeasurementPoint: Beskriver et målepunkt med en unik id, hva målepunktet er og enhet det måles i.
- LocationMeasurementPoint: Knytter et målepunkt til en lokasjon og gir et lokalt navn for målepunktet. Enkelte målepunkt brukes av mange lokasjoner, f.eks. temperaturmålere fra offisielle målestasjoner fra meteorilogisk institutt (met.no)
- Measurements: Tidsstemplede målinger fra målepunkt

Typene datasett inneholder følgende felter:

## Location
| Feltnavn | Beskrivelse  |
| -------- | ------------ |
| location | Navn på lokasjonen, f.eks. navn på skole eller barnehage |
| municipality_code | Kommunekoden for lokasjonen |
| location_type | Type lokasjon. Lovlige verdier: Bygning, Rom, Annet |
| building_type | Type bygning. Lovlige verdier: Skole, Barnehage, Helsebygg, Administrasjonsbygg, Idrettsbygg, Kirkelig bygg, Beredskapsbygg, Bydels- og fritidsbygg, Kulturbygg, Varmesentral, Annet bygg |
| address | Adresse til lokasjonen / bygget |
| latitude | Breddegrad for lokasjonen i desimalgrader |
| longitude | Lengdegrad for lokasjonen i desimalgrader |
 
MeasurementPoint:
meter_id
Unik id for målepunktet. Eksempler: EID_972418013_00290, Eklima_82290_TAM
meter_type
Beskriver hva slags type målepunkt det er. Eksempler er Fastkraft, Temperatur, Graddager, Varmepumpe
unit
Enhet som måleren måler, f.eks. kWh, °C
meter_level
Vanligvis en av følgende to verdier: Forbruksmåler, Annen måler
 
LocationMeasurementPoint:
location
Navn på lokasjonen (se Location)
municipality_code
Kommunekoden for lokasjonen
meter_id
Unik id for målepunktet (se MeasurementPoint)
meter_name
Lokalt navn for målepunktet (unikt bare innenfor lokasjonen).
Eksempler: Temp middel, Fastkraft, Fastkraft 67756
 
Measurements:
timestamp
Tidsstempel med dato og klokkeslett, f.eks. 2010-01-04 06:00:00
meter_id
Unik id for målepunkt (se MeasurementPoint)
value
Måleravlesning. Vanligvis flyttall med komma som separator, f.eks. 4,20
 
