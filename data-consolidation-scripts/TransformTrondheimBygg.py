import pandas as pd

# read_file = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/42 - Forbruksanalyse-Bodø Kommune - Tverlandet Bo og Servicesenter - 10.10.2021 9.37.18.xls')
# read_file.to_csv (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/42o.csv', index = None, header=True)

bt_school = "Skole"
bt_daycare = "Barnehage"
bt_health = "Helse"
bt_other = "Annet"
bt_admin = "Administrasjon"


def strip_prefix(s, p):
   if s.startswith(p):
      return s[len(p):]
   else:
      return s


def find_building_type(row):
    name = row.Bygg
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
    else:
        return bt_other

municipality_num = 5001

bygg_og_maalere = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/VIS Målere.xlsx', sheet_name="Sheet1", header=None)
# bygg_og_maalere = dfs["Bygg og Målere"]

building_prefix = "Trondheim Kommune - "

mm_point_dict = {}
mm_points_at_location = {}
mm_points_at_location_list = []
mm_column_names = ["ID", "Type", "Unit", "MeterLevel"]

MM_OBJECT_TYPE_IND = 3  - 2
MM_BUILDING_NAME_IND = 4 - 2

MM_ID_IND = 6 - 2
MM_NAME_IND = 4 - 2
MM_TYPE_IND = 5 - 2
MM_UNIT_IND = 7 - 2
MM_LEVEL_IND = 8 - 2

for row in bygg_og_maalere.itertuples():
    if isinstance(row[MM_OBJECT_TYPE_IND], str):
        if "Bygg" in row[MM_OBJECT_TYPE_IND]:
            # The row starts a new building
            cr_building = strip_prefix(row[MM_BUILDING_NAME_IND], building_prefix)

            # Give warning if building is not in the list building file
            #if not cr_building in bygg.index:
            #    print("NOT FOUND: " + cr_building)

            # Init entry for building with empty array of measurement points
            mm_points_at_location[cr_building] = []

        elif "VIS-Måler" in row[MM_OBJECT_TYPE_IND]:
            new_entry = {"MunicipalityCode": municipality_num, "Building": cr_building, "Name": row[MM_NAME_IND], "ID": row[MM_ID_IND]}
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
mm_point_df.set_index("ID", inplace=True)
mm_point_df.to_csv(r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/out_mm_points.csv', sep = ";")

print(mm_point_df)

mm_points_at_location_df = pd.DataFrame(mm_points_at_location_list)
mm_points_at_location_df.set_index("Building", inplace=True)
mm_points_at_location_df.to_csv(r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/out_building_mm_points.csv', sep = ";")
print(mm_points_at_location_df)


# first = bygg_og_maalere.iloc[1]
# print(first)


# read_file.to_csv (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/EsaveExport_Trondheim Kommune_Trondheim_10121314.xls', index = None, header=True)
