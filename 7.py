class first_model :
    def camera(self):
        print("60mp")
    def acomulator (self):
        print("1000mah")
class previos_model(first_model):
    def acomulator(self):
        print("3000mah")
class last_model(previos_model):
    def __init__(self):
        super().camera()
        super().acomulator()
galaxy_s_23ultra= last_model()