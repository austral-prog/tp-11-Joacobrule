def read_file_to_dict(filename):

    result = {}
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if not content:
                return result
            
            sales = content.split(';')
            for sale in sales:
                if sale:
                    product, amount = sale.split(':')
                    amount = float(amount)
                    if product in result:
                        result[product].append(amount)
                    else:
                        result[product] = [amount]
        return result
        
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no existe")
    except ValueError:
        raise ValueError("El archivo tiene un formato inválido")
    except Exception as e:
        raise Exception(f"Error al procesar el archivo: {str(e)}")

def process_dict(sales_dict):
    output_lines = []
    for product in sorted(sales_dict.keys()):
        sales = sales_dict[product]
        total = sum(sales)
        average = total / len(sales)
        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")