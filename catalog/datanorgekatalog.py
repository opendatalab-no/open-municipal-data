import os
from datacatalogtordf import Catalog, Dataset, Distribution, Agent, Resource
from concepttordf import Contact

# Values
municipalities = [
    ("Bodø", "bodo", "972418013"), 
    ("Drammen", "drammen", "921234554"), 
    ("Stavanger", "stavanger", "964965226"), 
    ("Trondheim", "trondheim", "942110464")]
datahotelDatasets = [("location-measurement-points", "Location measurement points"), ("locations", "Locations"), ("measurement-points", "Measurement points"), ("measurements", "Measurements")]

# Create catalog object
catalog = Catalog()
catalogIdentifier = "https://example.com/kommunedata/energi"
catalog.identifier = catalogIdentifier
catalog.dct_identifier = catalogIdentifier
catalog.title = {
    "nb": "Energimålingar i kommunale bygg",
    "en": "Energy usage datasets from municipality buildings"
}
catalog.description = {
    "nb": "Datasett frå kommunar, på samme format. Frå SamÅpne-prosjektet. Lansert til Open data challenge 2022.",
    "en": "Datasets from municipalities in the same format. From the SamÅpne-project. Launched for Open data challenge 2022."
}
agent = Agent()
agent.identifier = "https://data.brreg.no/enhetsregisteret/enhet/991825827"
agent.name = {
    "nb": "Digitaliseringsdirektoratet",
    "en": "The Norwegian Digitalisation Agency"
}
catalog.publisher = agent 

# Create datasets:
for (municipalityName, municipalityShortname, orgnr) in municipalities:
    dataset = Dataset()
    dctIdentifier = "https://example.com/kommunedata/energi/" + municipalityShortname
    dataset.identifier = dctIdentifier
    dataset.dct_identifier = dctIdentifier
    agent = Agent()
    agent.identifier = "https://data.brreg.no/enhetsregisteret/api/enheter/" + orgnr
    agent.name = {
        "nb": municipalityName + " kommune",
        "en": municipalityName + " municipality"
    }
    dataset.publisher = agent
    contact = Contact()
    contact.email = "erlend.stav@sintef.no"
    contact.name = {"nb": "Erlend Stav"}
    contact.url = "https://www.sintef.no/alle-ansatte/ansatt/erlend.stav/"
    dataset.contactpoint = contact
    dataset.title = {
        "nb": "Energimålinger kommunale bygg",
        "en": "Energy usage in municipal buildings"}
    dataset.description = {
        "nb": """
Datasettene i denne katalogen er samordnet basert på kiledata fra kommunene.

Det er fire typer datasett som hører sammen.
- Location: Beskriver en lokasjon (vanligvis et bygg) som det finnes energidata for.
- MeasurementPoint: Beskriver et målepunkt med en unik id, hva målepunktet er og enhet det måles i.
- LocationMeasurementPoint: Knytter et målepunkt til en lokasjon og gir et lokalt navn for målepunktet. Enkelte målepunkt brukes av mange lokasjoner, f.eks. temperaturmålere fra offisielle målestasjoner fra meteorilogisk institutt (met.no)
- Measurements: Tidsstemplede målinger fra målepunkt
  
Beskrivelse av hvert av datasettene med deres felter følger under.

## Location
| Feltnavn | Beskrivelse  |
| -------- | ------------ |
| location | Navn på lokasjonen, f.eks. navn på skole eller barnehage |
| municipality_code | Kommunekoden for lokasjonen. Kodene er definert i datasettet [Standard for kommuneinndeling](https://www.ssb.no/klass/klassifikasjoner/131/koder) hos SSB. |
| location_type | Type lokasjon. Lovlige verdier: Bygning, Rom, Annet |
| building_type | Type bygning. Lovlige verdier: Skole, Barnehage, Helsebygg, Administrasjonsbygg, Idrettsbygg, Kirkelig bygg, Beredskapsbygg, Bydels- og fritidsbygg, Kulturbygg, Varmesentral, Annet bygg |
| address | Adresse til lokasjonen / bygget |
| latitude | Breddegrad for lokasjonen i desimalgrader |
| longitude | Lengdegrad for lokasjonen i desimalgrader |
<br>  
<br>  

## MeasurementPoint
| Feltnavn | Beskrivelse  |
| -------- | ------------ |
| meter_id | Unik id for målepunktet. Eksempler: EID_972418013_00290, Eklima_82290_TAM |
| meter_type | Beskriver hva slags type målepunkt det er. Eksempler er Fastkraft, Temperatur, Graddager, Varmepumpe |
| unit | Enhet som måleren måler, f.eks. kWh, °C |
| meter_level | Vanligvis en av følgende to verdier: Forbruksmåler, Annen måler |
  
  

## LocationMeasurementPoint
| Feltnavn | Beskrivelse  |
| -------- | ------------ |
| location | Navn på lokasjonen (se Location) |
| municipality_code | Kommunekoden for lokasjonen |
| meter_id | Unik id for målepunktet (se MeasurementPoint) |
| meter_name | Lokalt navn for målepunktet (unikt bare innenfor lokasjonen). Eksempler: Temp middel, Fastkraft, Fastkraft 67756 |
  
  
## Measurements
| Feltnavn | Beskrivelse  |
| -------- | ------------ |
| timestamp | Tidsstempel med dato og klokkeslett, f.eks. 2010-01-04 06:00:00 |
| meter_id | Unik id for målepunkt (se MeasurementPoint) |
| value | Måleravlesning. Vanligvis flyttall med komma som separator, f.eks. 4,20 |

        """
        }
    dataset.access_rights = "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
    dataset.theme = [
        "http://publications.europa.eu/resource/authority/data-theme/ENER", 
        "http://publications.europa.eu/resource/authority/data-theme/GOVE"
        ]
    dataset.keyword = {"nb": "energimåling"}

    # Create distributions
    for (datasetId, datasetName) in datahotelDatasets:
        dist = Distribution()
        datasetHotelId = municipalityShortname + "/energy/" + datasetId
        accessUrl = "https://hotell.difi.no/?dataset=" + datasetHotelId
        dist.identifier = accessUrl
        dist.access_URL = accessUrl
        dist.download_URL = "https://hotell.difi.no/download/" + datasetHotelId
        dist.title = {
            "nb": datasetName,
            "en": datasetName
        }
        dist.description = {
            "nb": "API i formatene JSON, XML, CSV og YAML. Komplett nedlasting som CSV",
            "en": "API supporting JSON, XML, CSV and YAML. Complete download as CSV"
        }
        dist.formats = [
            "https://www.iana.org/assignments/media-types/text/csv", 
            "https://www.iana.org/assignments/media-types/application/xml",
            "https://www.iana.org/assignments/media-types/application/yaml",
            "https://www.iana.org/assignments/media-types/application/json"
        ]
        dist.license = "https://data.norge.no/nlod/no/2.0"
        dataset.distributions.append(dist)

    # Add dataset to catalog:
    catalog.datasets.append(dataset)

# get rdf representation in turtle (default)
rdf = catalog.to_rdf()
# print(rdf.decode())

# change working directory to same as script
# https://stackoverflow.com/a/1432949
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print(os.getcwd())

# write to file
f = open("kommuneenergi.ttl", "w")
f.write(rdf.decode())
f.close()
