class H_Inference:
    
    # return [healthy, sick1, sick2, sick3, sick4]
    def inference(self,input_dict: dict):
        healthy = []
        sick1 = []
        sick2 = []
        sick3 = []
        sick4 = []

        # RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;
        sick4.append(min(input_dict['chest_pain'][1], input_dict['age'][3]))
        # RULE 2: IF (maximum_heart_rate IS high) AND (age IS old) THEN health IS sick_4;
        sick4.append(min(input_dict['age'][2], input_dict['heart_rate'][2]))
        # RULE 3: IF (sex IS male) AND (maximum_heart_rate IS medium) THEN health IS sick_3;
        sick3.append(min(input_dict['sex'][1], input_dict['heart_rate'][1]))
        # RULE 4: IF (sex IS female) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
        sick2.append(min(input_dict['sex'][0], input_dict['heart_rate'][1]))
        # RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;
        sick3.append(min(input_dict['chest_pain'][2],input_dict['blood_pressure'][2]))
        # RULE 6: IF (chest_pain IS typical_anginal) AND (maximum_heart_rate IS medium) THEN health IS sick_2;
        sick2.append(min(input_dict['chest_pain'][0],input_dict['heart_rate'][1]))
        # RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;
        sick3.append(min(input_dict['blood_sugar'][0] , input_dict['age'][1]))
        # RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;
        sick2.append(min(input_dict['blood_sugar'][1],input_dict['blood_pressure'][3]))
        # RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;
        sick1.append(min(input_dict['chest_pain'][3],input_dict['age'][3]))
        # RULE 10: IF (blood_pressure IS high) OR (maximum_heart_rate IS low) THEN health IS sick_1;
        sick1.append(min(input_dict['blood_pressure'][2],input_dict['heart_rate'][0]))
        # RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;
        healthy.append((input_dict['chest_pain'][0]))
        # RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;
        sick1.append((input_dict['chest_pain'][1]))
        # RULE 13: IF (chest_pain IS non_aginal_pain) THEN health IS sick_2;
        sick2.append((input_dict['chest_pain'][2]))
        # RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;
        sick3.append((input_dict['chest_pain'][3]))
        # RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;
        sick4.append((input_dict['chest_pain'][3]))
        # RULE 16: IF (sex IS female) THEN health IS sick_1;
        sick1.append(input_dict['sex'][0])
        # RULE 17: IF (sex IS male) THEN health IS sick_2;
        sick2.append(input_dict['sex'][1])
        # RULE 18: IF (blood_pressure IS low) THEN health IS healthy;
        healthy.append(input_dict['blood_pressure'][0])
        # RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;
        sick1.append(input_dict['blood_pressure'][1])
        # RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;
        sick2.append(input_dict['blood_pressure'][2])
        # RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;
        sick3.append(input_dict['blood_pressure'][2])
        # RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;
        sick4.append(input_dict['blood_pressure'][3])
        # RULE 23: IF (cholesterol IS low) THEN health IS healthy;
        healthy.append(input_dict["cholestrol"][0])
        # RULE 24: IF (cholesterol IS medium) THEN health IS sick_1;
        sick1.append(input_dict["cholestrol"][1])
        # RULE 25: IF (cholesterol IS high) THEN health IS sick_2;
        sick2.append(input_dict["cholestrol"][2])
        # RULE 26: IF (cholesterol IS high) THEN health IS sick_3;
        sick3.append(input_dict["cholestrol"][2])
        # RULE 27: IF (cholesterol IS very_high) THEN health IS sick_4;
        sick4.append(input_dict["cholestrol"][3])
        # RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;
        sick2.append(input_dict['blood_pressure'][0])
        # RULE 29: IF (ECG IS normal) THEN health IS healthy;
        healthy.append(input_dict['ecg'][0])
        # RULE 30: IF (ECG IS normal) THEN health IS sick_1;
        sick1.append(input_dict['ecg'][0])
        # RULE 31: IF (ECG IS abnormal) THEN health IS sick_2;
        sick2.append(input_dict['ecg'][1])
        # RULE 32: IF (ECG IS hypertrophy) THEN health IS sick_3;
        sick3.append(input_dict['ecg'][2])
        # RULE 33: IF (ECG IS hypertrophy) THEN health IS sick_4;
        sick4.append(input_dict['ecg'][2])
        # RULE 34: IF (maximum_heart_rate IS low) THEN health IS healthy;
        healthy.append(input_dict['heart_rate'][0])
        # RULE 35: IF (maximum_heart_rate IS medium) THEN health IS sick_1;
        sick1.append(input_dict['heart_rate'][1])
        # RULE 36: IF (maximum_heart_rate IS medium) THEN health IS sick_2;
        sick2.append(input_dict['heart_rate'][1])
        # RULE 37: IF(maximum_heart_rate IS high) THEN health IS sick_3;
        sick3.append(input_dict['heart_rate'][2])
        # RULE 38: IF(maximum_heart_rate IS high) THEN health IS sick_4;
        sick4.append(input_dict['heart_rate'][2])
        # RULE 39: IF (exercise IS true) THEN health IS sick_2;
        sick2.append(input_dict['exercise'][1])
        # RULE 40: IF (old_peak IS low) THEN health IS healthy;
        healthy.append(input_dict['old_peak'][0])
        # RULE 41: IF (old_peak IS low) THEN health IS sick_1;
        sick1.append(input_dict['old_peak'][0])
        # RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;
        sick2.append(input_dict['old_peak'][2])
        # RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;
        sick3.append(input_dict['old_peak'][2])
        # RULE 44: IF (old_peak IS risk) THEN health IS sick_4;
        sick4.append(input_dict['old_peak'][1])
        # RULE 45: IF (thallium IS normal) THEN health IS healthy;
        healthy.append(input_dict['thallium_scan'][0])
        # RULE 46: IF (thallium IS normal) THEN health IS sick_1;
        sick1.append(input_dict['thallium_scan'][0])
        # RULE 47: IF (thallium IS medium) THEN health IS sick_2;
        sick2.append(input_dict['thallium_scan'][1])
        # RULE 48: IF (thallium IS high) THEN health IS sick_3;
        sick3.append(input_dict['thallium_scan'][2])
        # RULE 49: IF (thallium IS high) THEN health IS sick_4;
        sick4.append(input_dict['thallium_scan'][2])
        # RULE 50: IF (age IS young) THEN health IS healthy;
        healthy.append(input_dict['age'][0])
        # RULE 51: IF (age IS mild) THEN health IS sick_1;
        sick1.append(input_dict['age'][1])
        # RULE 52: IF (age IS old) THEN health IS sick_2;
        sick2.append(input_dict['age'][2])
        # RULE 53: IF (age IS old) THEN health IS sick_3;
        sick3.append(input_dict['age'][2])
        # RULE 54: IF (age IS very_old) THEN health IS sick_4;
        sick4.append(input_dict['age'][3])

        return [max(healthy),max(sick1),max(sick2),max(sick3),max(sick4)]

