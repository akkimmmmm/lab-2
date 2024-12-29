import xml.etree.ElementTree as ET

file_path = 'currency.xml'
tree = ET.parse(file_path)
root = tree.getroot()

data = []
for valute in root.findall('Valute'):
    data.append({
        'CharCode': valute.find('CharCode').text,
        'Name': valute.find('Name').text,
        'Nominal': int(valute.find('Nominal').text),
        'Value': float(valute.find('Value').text.replace(',', '.'))
    })

for item in data:
    print(f"{item['CharCode']} - {item['Name']}: {item['Nominal']} единиц = {item['Value']} RUB")
