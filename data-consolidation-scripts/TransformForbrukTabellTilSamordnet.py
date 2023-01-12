import pandas as pd
from os import walk
import glob

DRAMMEN_INPUT_DIR = r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Drammen/Edited'
BODO_INPUT_DIR = r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/Edited'
STAVANGER_INPUT_DIR = r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Stavanger/Edited'
TRONDHEIM_INPUT_DIR = r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/Edited'

INPUT_DIR = STAVANGER_INPUT_DIR

OUTPUT_FILE = INPUT_DIR + "/out/out.csv"

COLUMN_NAMES = ["timestamp", "meter_id", "value"]

def fix_timestamp(intime):
    segments = intime.split(" ")
    time_segments = segments[1].split(":")
    hour_and_mins = time_segments[0] + ":00"
    if "." in segments[0]:
        datesegments = segments[0].split(".")
        return datesegments[2] + "-" + datesegments[1] + "-" + datesegments[0] + " " + hour_and_mins

    return segments[0] + " "  + hour_and_mins


    # timesegments = intime.split(" ")
    # tmp = timesegments[0] + " " + timesegments[1]
    # tmp = fix_timestamp_hour_and_zero_min(tmp)
    # return tmp #timesegments[0] + " " + timesegments[1]

def transform_from_to(input_dir, output_file_name):
    out_list = []
#    input_file_names = next(walk(input_dir), (None, None, []))[2]  # [] if no file

    input_file_names = glob.glob(input_dir+'/*.csv')

    for filename in input_file_names:
        # in_df = pd.read_csv(input_dir + "/" + filename, sep=';')
        in_df = pd.read_csv(filename, sep=';')

        # Go through each row of data in the table
        for row in in_df.itertuples():
            if len(row) >= 2:
                # Extract timestamp, and for each value find the corresponding meter and add an entry to the list
                timestamp = fix_timestamp(row[1])

                for i in range(len(row)-2):
                    meter = in_df.columns[i+1]
                    value = row[i+2]

                    new_entry = {COLUMN_NAMES[0]: timestamp, COLUMN_NAMES[1]: meter, COLUMN_NAMES[2]: value}
                    out_list.append(new_entry)

    out_df = pd.DataFrame(out_list)
    out_df.set_index([COLUMN_NAMES[0],COLUMN_NAMES[1]], inplace=True)
    out_df.to_csv(output_file_name, sep = ";")

transform_from_to(INPUT_DIR, OUTPUT_FILE)
# print(fix_timestamp("2010-02-01 01:00:13"))
# print(fix_timestamp("2010-02-01 01:00"))
# print(fix_timestamp("01.02.2015 01:00"))
# print(fix_timestamp("01.02.2015 01:00:13"))
#print(fix_timestamp("01.02.2021 00:00 - 01:00"))

# read_file = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/EsaveExport_Trondheim Kommune_Trondheim_10121314.xls')
# read_file.to_csv (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/EsaveExport_Trondheim Kommune_Trondheim_10121314.csv', index = None, header=True)
