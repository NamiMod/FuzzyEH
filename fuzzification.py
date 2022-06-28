class H_fuzzification:
    
    # return [typical, atypical, non, asy]
    def chest_pain(self,x):
        if x == 1:
            return [1,0,0,0]
        if x == 2:
            return [0,1,0,0]
        if x == 3:
            return [0,0,1,0]
        # x = 4
        return [0,0,0,1]

    # return [low, medium, high, very_high]
    def cholestrol(self,x):
        low = 0
        medium = 0
        high = 0
        very_high = 0

        if x <= 151:
            low = 1
        if x >= 197:
            low = 0
        if x > 151 and x < 197:
            low = ((-1/46)*(x - 151)) + 1
        if x <= 188 or x >=250:
            medium = 0
        if x > 188 and x <= 215:
            medium = ((1/27)*(x - 188))
        if x > 215 and x < 250:
            medium = ((-1/35)*(x - 215)) + 1
        if x <=217 or x > 307:
            high = 0
        if x > 217 and x <=263:
            high = ((1/46)*(x - 217))
        if x > 263 and x < 307:
            high = ((-1/44)*(x - 263))+1
        if x <= 281:
            very_high = 0
        if x >= 347:
            very_high = 1
        if x < 347 and x > 281:
            very_high = ((1/66)*(x - 281))

        return [low,medium,high,very_high]

    # return [normal, abnormal, hypertropy]
    def ecg(self,x):
        normal = 0
        abnormal = 0
        hypertropy = 0

        if x <= 0:
            normal = 1
        if x >= 0.4 :
            normal = 0
        if x > 0 and x < 0.4 :
            normal = -2.5*x + 1
        if x <= 0.2 or x <= 1.8:
            abnormal = 0
        if x > 0.2 and x <= 1:
            abnormal = 1.25 * x - 0.25
        if x > 1 and x < 1.8:
            abnormal = -1.25 * x + 2.25
        if x <= 1.4:
            hypertropy = 0
        if x >= 1.9:
            hypertropy = 1
        if x > 1.4 and x < 1.9:
            hypertropy = 2*x - 2.8

        return [normal, abnormal, hypertropy]

    # return [notOK, OK]
    def exercise(self,x):
        return [x,1-x]
    
    # return [normal, medium, high]
    def thallium_scan(self,x):
        if x == 3 :
            return [1,0,0]
        if x == 6:
            return [0,1,0]
        # x = 7
        return [0,0,1]
        
    # return [young, mid, old, very old]
    def age(self,x):
        young = 0
        mid = 0
        old = 0
        very_old = 0

        if x >= 38 :
            young = 0
        if x <= 29:
            young = 1
        if x < 38 and x > 29:
            young = ((-1/9)*(x - 29)) + 1
        if x >= 45 or x <=33 :
            mid = 0
        if x > 33 and x <= 38 :
            mid = ((1/5)*(x - 33))
        if x > 38 and x < 45 :
            mid = ((-1/7)*(x - 38))+1
        if x >= 58 or x <=40 :
            old = 0
        if x > 40 and x <= 48 :
            old = ((1/8)*(x - 40))
        if x > 48 and x < 58 :
            old = ((-1/10)*(x - 48)) + 1
        if x < 52 :
            very_old = 0
        if x > 60 :
            very_old = 1
        if x >=52 and x<=60 :
            very_old = ((1/8)*(x - 52))
        return [young,mid,old,very_old]
        
    #return [female, male]
    def sex(self,x):
        return [x,1-x]

    # return [low, risk, terrible]
    def old_peak(self,x):
        low = 0
        risk = 0
        terrible = 0

        if x <= 1:
            low = 1
        if x >= 2:
            low = 0
        if x > 1 and x < 2:
            low = -1*x + 2
        if x >=1.5 or x < 4.2:
            risk = 0
        if x > 1.5 and x <= 2.8:
            risk = ((10/13)*(x - 1.5))
        if x > 2.8 and x < 4.2:
            risk = ((-5/7)*(x - 2.8)) + 1
        if x <= 2.5:
            terrible = 0
        if x > 4:
            terrible = 1
        if x > 2.5 and x < 4:
            terrible = ((2/3)*(x - 2.5))
        
        return [low, risk, terrible]
        
    # return [low, medium, high]
    def heart_rate(self,x):
        low = 0
        medium = 0
        high = 0
        
        if x <= 100:
            low = 1
        if x >= 141:
            low = 0
        if x > 100 and x < 141:
            low = ((-1/41)*(x - 100)) + 1
        if x <= 111 or x >= 194:
            medium = 0
        if x > 111 and x <= 152:
            medium = ((1/41)*(x - 111))
        if x > 152 and x < 194:
            medium = ((-1/42)*(x - 152)) + 1
        if x <= 152:
            high = 0
        if x >= 210:
            high = 1
        if x > 152 and x < 210:
            high = ((1/58)*(x - 152))

        return [low, medium , high]

    # return [true, false]
    def blood_sugar(self,x):
        if x >=120:
            return [1,0]
        return [0,1]

    # return [bp_low, bl_medium, bp_high, bp_very_high]
    def blood_pressure(self,x):
        bp_low = 0
        bp_medium = 0
        bp_high = 0
        bp_very_high = 0

        if x <= 111:
            bp_low = 1
        if x >=134:
            bp_low = 0
        if x > 111 and x < 134:
            bp_low = ((-1/23)*(x - 111)) + 1
        if x <= 127 or x >=153 :
            bp_medium = 0
        if x > 127 and x <=139:
            bp_medium = ((1/12)*(x - 127))
        if x > 139 and x < 153:
            bp_medium = ((-1/14)*(x - 139)) + 1
        if x <= 142 or x >=172 :
            bp_high = 0
        if x > 142 and x <=157:
            bp_high = ((1/15)*(x - 142))
        if x > 157 and x <172:
            bp_high = ((-1/15)*(x - 157)) + 1
        if x <= 154:
            bp_very_high = 0
        if x >= 171:
            bp_very_high = 1
        if x >154 and x < 171 :
            bp_very_high = ((1/17)*(x - 154))

        return [bp_low,bp_medium,bp_high,bp_very_high]

    # call functions and return a dictionary
    def return_fuzzy_numbers(self,input_dict: dict):
        temp = {}
        temp.update({'chest_pain': self.chest_pain(int(input_dict['chest_pain']))})
        temp.update({'cholestrol': self.cholestrol(int(input_dict['cholestrol']))})
        temp.update({'ecg': self.ecg(float(input_dict['ecg']))})
        temp.update({'exercise': self.exercise(int(input_dict['exercise']))})
        temp.update({'thallium_scan': self.thallium_scan(int(input_dict['thallium_scan']))})
        temp.update({'age': self.age(int(input_dict['age']))})
        temp.update({'blood_pressure': self.blood_pressure(int(input_dict['blood_pressure']))})
        temp.update({'blood_sugar': self.blood_sugar(int(input_dict['blood_sugar']))})
        temp.update({'heart_rate': self.heart_rate(int(input_dict['heart_rate']))})
        temp.update({'old_peak': self.old_peak(float(input_dict['old_peak']))})
        temp.update({'sex': self.sex(int(input_dict['sex']))})
        return temp