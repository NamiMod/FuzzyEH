'''
Second Project of CI

Fuzzy system for diagnosing heart disease

Writer : Nami Modarressi (@SnamiMod)

'''

import fuzzification
import inference
import defuzzification
class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        p = fuzzification.H_fuzzification()
        q = inference.H_Inference()
        s = defuzzification.H_Defuzzification()
        t1 = p.return_fuzzy_numbers(input_dict)
        t2 = q.inference(t1)
        return s.return_string(t2)
        