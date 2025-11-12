# Author   : Atharva Kadam
# Email    : aakadam@umass.edu
# Spire ID : 35090900


import os

def read_csv(fname):
    dict_encapsulated_list = []

    try:
        f = open(fname, 'r')
        lines = f.readlines()
        
        if not lines:
            f.close()
            return None
        
        for line in lines:
            parts = line.strip().split(',')
            
            if len(parts) < 12:
                continue

            try:
                name = parts[0].strip()
                section = parts[1].strip()

                scores = []
                for i in range(2, 12):
                    score = float(parts[i].strip())
                    scores.append(score)
                
                if scores:
                    total_score = sum(scores)
                    average_score = total_score / len(scores)
                    rounded_average = round(average_score, 3)
                else:
                    rounded_average = 0.0

            except ValueError:
                continue
            
            student_dict = {}
            student_dict['name'] = name
            student_dict['section'] = section
            student_dict['scores'] = scores
            student_dict['average'] = rounded_average
            
            dict_encapsulated_list.append(student_dict)

        f.close()
        
        return dict_encapsulated_list

    except:
        if not os.path.exists(fname):
            raise IsADirectoryError(f'Error occurred when opening {fname} to read')
        return None
