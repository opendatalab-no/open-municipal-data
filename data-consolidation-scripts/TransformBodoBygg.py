import pandas as pd

# read_file = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/42 - Forbruksanalyse-Bodø Kommune - Tverlandet Bo og Servicesenter - 10.10.2021 9.37.18.xls')
# read_file.to_csv (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/42o.csv', index = None, header=True)

bt_school = "Skole"
bt_daycare = "Barnehage"
bt_health = "Helsebygg"
bt_admin = "Administrasjonsbygg"
bt_hall = "Idrettsbygg"
bt_church = "Kirkelig bygg"
bt_emergency = "Beredskapsbygg"
bt_leasure = "Bydels- og fritidsbygg"
bt_culture = "Kulturbygg"
bt_heat_central = "Varmesentral"
bt_other = "Annet bygg"

lt_building = "Bygning"


def strip_prefix(s, p):
   if s.startswith(p):
      return s[len(p):]
   else:
      return s


def find_building_type(row):
    name = row.Bygg.lower()
    if "skole" in name:
        return bt_school
    elif "hage" in name:
        return bt_daycare
    elif "velferd" in name:
        return bt_health
    elif "helse" in name:
        return bt_health
    elif "syk" in name:
        return bt_health
    elif "admin" in name:
        return bt_admin
    elif "rådhus" in name:
        return bt_admin
    elif "hall" in name:
        return bt_hall
    elif "basseng" in name:
        return bt_hall
    elif "brann" in name:
        return  bt_emergency
    elif "fritid" in name:
        return bt_leasure
    elif "bydelshus" in name:
        return bt_leasure
    elif "kultur" in name:
        return bt_culture
    else:
        return bt_other

bygg_og_gps = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/00 - Bygg og GPS.xlsx', sheet_name="Bygg og GPS", header=1)
# dfs = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/00 - Bygg og GPS.xlsx', sheet_name=None)
# bygg_og_gps = dfs["Bygg og GPS"]
first = bygg_og_gps.iloc[1]
print(first)

column_names = ["location",  "municipality_code", "location_type", "building_type", "address", "latitude", "longitude"]
# bygg = pd.DataFrame(columns=column_names)
bygg_list = []

municipality_num = 1804

for row in bygg_og_gps.itertuples():
    new_entry = []
    new_entry = [row.Bygg, municipality_num, lt_building, find_building_type(row), row.Adresse, row.North, row.East]
    # print(row.Bygg)
    bygg_list.append(new_entry)
    # print(new_entry)

bygg = pd.DataFrame(bygg_list, columns=column_names)
bygg.set_index("location", inplace=True)
print(bygg)

bygg.to_csv(r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/out_bygg.csv', sep = ";")

bygg_og_maalere = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/00 - Bygg og GPS.xlsx', sheet_name="Bygg og Målere", header=None)
# bygg_og_maalere = dfs["Bygg og Målere"]

building_prefix = "Bodø Kommune - "

mm_point_dict = {}
mm_points_at_location = {}
mm_points_at_location_list = []
mm_column_names = ["meter_id", "meter_type", "unit", "meter_level"]

b_mm_column_names = ["location", "municipality_code", "meter_id", "meter_name"]

MM_OBJECT_TYPE_IND = 3
MM_BUILDING_NAME_IND = 4

MM_ID_IND = 6
MM_NAME_IND = 4
MM_TYPE_IND = 5
MM_UNIT_IND = 7
MM_LEVEL_IND = 8

for row in bygg_og_maalere.itertuples():
    if isinstance(row[MM_OBJECT_TYPE_IND], str):
        if row[MM_OBJECT_TYPE_IND].startswith("Bygg"):
            # The row starts a new building
            cr_building = strip_prefix(row[MM_BUILDING_NAME_IND], building_prefix)

            # Give warning if building is not in the list building file
            if not cr_building in bygg.index:
                print("NOT FOUND: " + cr_building)

            # Init entry for building with empty array of measurement points
            mm_points_at_location[cr_building] = []

        elif row[MM_OBJECT_TYPE_IND].startswith("VIS-Måler"):
            new_entry = {b_mm_column_names[0]: cr_building, b_mm_column_names[1]: municipality_num, b_mm_column_names[2]: row[MM_ID_IND], b_mm_column_names[3]: row[MM_NAME_IND] }
            mm_points_at_location[cr_building].append(new_entry)
            mm_points_at_location_list.append(new_entry)

            if not row[MM_ID_IND] in mm_point_dict:
                # Mot already present,so add to measurement points
                new_entry = [row[MM_ID_IND], row[MM_TYPE_IND], row[MM_UNIT_IND], row[MM_LEVEL_IND]]
                mm_point_dict[row[MM_ID_IND]] = new_entry

        else:
            print("Row skipped: ", row)
    else:
        print("Row skipped: ", row)



mm_point_df = pd.DataFrame(mm_point_dict.values(), columns=mm_column_names)
mm_point_df.set_index("meter_id", inplace=True)
mm_point_df.to_csv(r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/out_mm_points.csv', sep = ";")

print(mm_point_df)

mm_points_at_location_df = pd.DataFrame(mm_points_at_location_list)
mm_points_at_location_df.set_index("location", inplace=True)
mm_points_at_location_df.to_csv(r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/out_building_mm_points.csv', sep = ";")
print(mm_points_at_location_df)


# first = bygg_og_maalere.iloc[1]
# print(first)


# read_file.to_csv (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/EsaveExport_Trondheim Kommune_Trondheim_10121314.xls', index = None, header=True)
