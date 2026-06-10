data_path = "data/"

def store_data(filename: str, data: str):
    file_path = data_path + filename
    try:
        with open(file_path, "w") as f:
            f.write(data)
    except Exception as e:
        print("Error")
        print(str(e))
        return False
    return True

def get_file(filename: str):
    file_path = "data/" + filename
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError as e:
        return str(e) 