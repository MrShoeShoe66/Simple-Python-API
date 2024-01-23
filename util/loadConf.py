import decimal

def load_utility_file(file_path):
    settings = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'): 
                key, value = line.split(':')
                value = value.strip()
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        try:
                            value = decimal.Decimal(value)
                        except (ValueError, decimal.InvalidOperation):
                            if value.lower() == 'true':
                                value = True
                            elif value.lower() == 'false':
                                value = False
                            else:
                                value = value.strip()
                settings[key.strip()] = value
    return settings