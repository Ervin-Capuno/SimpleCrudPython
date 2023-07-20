class ErrorClass:
    
    @staticmethod
    def data_type_error(variable_name, data_type):
        """
        Handle data type errors of user input.


        Args:
            variable_name(str): the name of the variable being asked for input.
            data_type(type): The data type of the input(e.g. int, float, str)

        Returns:
            The user-provided input, converted to the specified data type
        """
        while True:
            try:
                user_input=data_type(input(f"Enter a {variable_name}: "))
                return user_input
            except ValueError:
                print(f"Please enter valid {data_type} for {variable_name}")
            
    
