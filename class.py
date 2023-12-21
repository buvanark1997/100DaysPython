class FirstClass:
    #initilizing method to set values to variable / attributes
    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name

#creating object of a class
first_object = FirstClass(1,2)
print(first_object.user_id)
print(first_object.user_name)
