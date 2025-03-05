# Input test
# (Exception)

class Utils():
        
    def isCsvSuffix(file_name: str, type_file: str):
        valid_location_suffix = len(file_name)-len(type_file)
        is_valid_location_suffix = valid_location_suffix == file_name.lower().find(type_file.lower())
        if valid_location_suffix == 0 or type_file.lower() not in file_name.lower() or not is_valid_location_suffix:
            print("\nThe file name extension is invalid.")
            raise Exception("SuffixInvalid")
    

    def isIntNumber(in_put, id_age_index: str):
      if not in_put.isdigit():
        print("Attention! '" + id_age_index + "' must be a positive integer. '" + str(in_put) + "' is not positive integer")
        raise Exception("IsNotDigits")


    def isPositiveNumber(in_put, field_name: str):
       Utils.isFloat(in_put, field_name)
       in_put = float(in_put)
       if in_put < 0:
            Utils.notPositiveNumberRaise(in_put, field_name)
       else:
            return True


    def isFloat(in_put, field_name):
       try:
          float(in_put)
          return True
       except ValueError:
          Utils.notPositiveNumberRaise(in_put, field_name)


    def notPositiveNumberRaise(in_put, field_name: str):
       print("Attention! '" + field_name + "' must be a positive number. '" + str(in_put) + "' is not positive number")
       raise Exception("IsNotPositiveNumber")
          

# file_name = "exsmaple.txt"
# type_file = ".CSV"

# try:
#     a = Utils.isCsvSuffix(file_name, type_file)
#     print(a)
# except Exception as e:
#     print("\n===== An error occurred =====")
#     print("Error: " + str(e))