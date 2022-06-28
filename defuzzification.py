class H_Defuzzification:
    
    def healthy_value(self, x):
        if 0 <= x and x <= 0.25:
            return 1
        if 0.25 < x  and x <= 1:
            return (-1 / 0.75) * x + 1 / 0.75
        return 0

    def sick1_value(self, x):
        if 0 <= x and x <= 1:
            return x
        if 1 < x and x <= 2:
            return (-1) * x + 2
        return 0

    def sick2_value(self, x):
        if 1 <= x and x <= 2:
            return 1 * x - 1
        if 2 < x and x <= 3:
            return (-1) * x + 3
        return 0

    def sick3_value(self, x):
        if 2 <= x and x <= 3:
            return 1 * x - 2
        if 3 < x and x <= 4:
            return -1 * x + 4
        return 0

    def sick4_value(self, x):
        if 0 <= x and x <= 3:
            return 0
        if 3 < x and x <= 3.75:
            return (1 / 0.75) * x - 3 / 0.75
        return 1

    # return center of mass
    def calculate_center_of_mass(self,input_list):
        # 1000 is number of steps
        p = 0.0
        q = 0.0
        d = 5.0 / 1000
        for y in [i * d for i in range(1001)]:
            healthy = self.healthy_value(y)
            if healthy > input_list[0]:
                healthy = input_list[0]
            sick1 = self.sick1_value(y)
            if sick1 > input_list[1]:
                sick1 = input_list[1]
            sick2 = self.sick2_value(y)
            if sick2 > input_list[2]:
                sick2 = input_list[2]
            sick3 = self.sick3_value(y)
            if sick3 > input_list[3]:
                sick3 = input_list[3]
            sick4 = self.sick4_value(y)
            if sick4 > input_list[4]:
                sick4 = input_list[4]
            m = max(sick1, sick2, sick3, sick4, healthy)
            q = q + m * d
            p = p + m * d * y
            
        if q == 0:
            return 0
        else: 
            return p/q

    def return_string(self,input_list):
        x = self.calculate_center_of_mass(input_list)
        output_String = ""
        if x < 1.78:
            output_String = output_String + "Healthy  "
        if x >= 1 and x <= 2.51 :
            output_String = output_String + "Sick(s1)  "
        if x >= 1.78 and x <=3.25 :
            output_String = output_String + "Sick(s2)  "
        if x >= 1.5 and x <= 4.5 :
            output_String = output_String + "Sick(s3)  "
        if x > 3.25 :
            output_String = output_String + "Sick(s4)  "

        output_String = output_String + ": " + str(x)
        return output_String

