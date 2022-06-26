import fuzzification
class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        p = fuzzification.Pa_fuzzification()
        print(p.chest_pain(1) , "******^^^&&&")
        return "salam"
        # pass
