class Pa_fuzzification:
    
    def chest_pain(x):
        return 0

    def cholestrol(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0

    def ecg(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0

    def exercise(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0
    
    def thallium_scan(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0

    def age(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0
        

    def sex(x):
        # male => x = 0
        # female => x = 1
        return x

    def old_peak(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0
    
    def heart_rate(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0

    def blood_sugar(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0

    def blood_pressure(x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0

    def return_fuzzy_numbers(input_dict: dict):
        # return dictionary
        return 0