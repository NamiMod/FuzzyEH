import fuzzification
import inference
class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        print(input_dict)
        p = fuzzification.H_fuzzification()
        q = inference.H_Inference()
        t = p.return_fuzzy_numbers(input_dict)
        print(q.inference(t) , "******^^^&&&")
        pass

