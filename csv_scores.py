# Author   : Atharva Kadam
# Email    : aakadam@umass.edu
# Spire ID : 35090900

import csv
import os

def read_csv(fname):
    dict_encapsulated_list = []

    if not os.path.exists(fname):
        raise FileNotFoundError(f'Error occurred when opening {fname} to read')
    
    try:
        with open(fname, 'r') as f:
            lines = f.readlines()
            
            if not lines:
                return None
            
            for line in lines:
                parts = line.strip().split(',', maxsplit=11)
                
                if len(parts) != 12:
                    continue

                try:
                    name = parts[0].strip()
                    section = parts[1].strip()

                    scores = []
                    for i in range(2, 12):
                        score = float(parts[i].strip())
                        scores.append(score)
                    
                    total_score = sum(scores)
                    average_score = total_score / 10
                    rounded_average = round(average_score, 3)
                
                except ValueError:
                    continue
                
                student_dict = {
                    'name': name,
                    'section': section,
                    'scores': scores,
                    'average': rounded_average
                }
                
                dict_encapsulated_list.append(student_dict)
        
        return dict_encapsulated_list

    except IsADirectoryError:
        raise IsADirectoryError(f'Error occurred when opening {fname} to read')


