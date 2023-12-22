# Adjust Elevation Data and find the slope

import numpy as np
import pandas as pd
import os
import geopy.distance
import pickle



df_ski_diff = pd.read_csv('trail_status/trail_status.csv')
df_ski_diff = df_ski_diff.rename(columns={'Unnamed: 0': 'Trail_ID'})
df_ski_diff = df_ski_diff.set_index("Trail_ID")


top_path = 'ski_resort_piste_coords'
# resorts = os.listdir(top_path)[1:]
resorts = ['Stowe Mountain Resort', 'Telluride Ski Area', 'Taos Ski Valley', 'Killington']

df_ski_trails = pd.DataFrame(columns = ['ID', 'Resort', 'Trail', 'Input Lon', 'Input Lat', 'Elev(ft)', 'Elev(m)', 'Length(ft)', 'Lowest Elev(ft)', 'Slope', 'Average Slope', 'Max Slope', 'Grade', 'Gladed', 'Moguled', 'Diff'])


for resort in resorts:
    resort_path = top_path + '/' + resort
    trails_csv = os.listdir(resort_path)
    if '.DS_Store' in trails_csv:
        index = trails_csv.index('.DS_Store')
        del trails_csv[index]
    for trail in trails_csv:
        final_path = resort_path + '/' + trail
        df_temp = pd.read_csv(final_path)
        df_temp.insert(1, 'Resort', resort)
        df_temp.insert(2, 'Trail', trail.replace('.csv', ''))
        df_temp['Length(ft)'] = 0
        df_temp['Lowest Elev(ft)'] = np.min(df_temp["Elev(ft)"])
        df_temp['Slope'] = 0
        length = 0
        for ell in range(len(df_temp)-1):
            df_temp['Length(ft)'][ell+1] = geopy.distance.distance([df_temp['Input Lat'][ell], df_temp['Input Lon'][ell]], [df_temp['Input Lat'][ell+1], df_temp['Input Lon'][ell+1]]).ft
            df_temp['Slope'][ell+1] = (df_temp['Elev(ft)'][ell]-df_temp['Elev(ft)'][ell+1])/(df_temp["Length(ft)"][ell+1]) 

        df_temp['Average Slope'] = np.average(df_temp['Slope'])
        df_temp['Max Slope'] = np.max(df_temp['Slope'])
        trail_id = df_temp["Trail"][0].split('_')
        df_temp['Grade'] = df_ski_diff["difficulty"][int(trail_id[0])]
        df_temp['Gladed'] = np.where(df_ski_diff["gladed"][int(trail_id[0])] == 'TRUE', 1, 0)
        df_temp['Moguled'] = np.where(df_ski_diff["grooming"][int(trail_id[0])] == 'mogul', 1, 0)

        # Diff = AveSlope + MaxSlope + 5(gladed) + 3(Moguls)
        df_temp['Diff'] = df_temp['Average Slope'] + df_temp['Max Slope'] + 10*df_temp['Gladed'] + 6*df_temp['Moguled']
        df_ski_trails = pd.concat([df_ski_trails, df_temp])
        




df_ski_trails.to_csv('ski_trails_data.csv', columns = ["Lowest Elev(ft)", "Diff"])


print("stop")



    