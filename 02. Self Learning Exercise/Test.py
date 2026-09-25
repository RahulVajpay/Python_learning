raw_records = [
    ["C1", "  jordan lee  ", 120, 80],
    ["C2", "TAYLOR KIM", 200, 150],
    ["C3", "  Riley Chen", 60, 90],
    ["C4", "morgan patel  ", 300, 100],
    ["C5", "  ALEX OWEN  ", 45, 55],
]

def clean_customers(records):
    result = {}
    for row in records:
        customer_id = row[0]
        raw_name = row[1]
        purchase_1 = row[2]
        purchase_2 = row[3]
        cleaned_name = raw_name.strip().title()
        average = (purchase_1 + purchase_2) / 2 
        flag = ""
        if average < 60:
            flag = "Low Value"
        else:
            flag = "High Value"    

        if customer_id not in result:
            result[customer_id] = {
                "name": cleaned_name,
                "average_purchase": average,
                "flag": flag
            }
        else:
            result[customer_id]["average_purchase"] = (result[customer_id]["average_purchase"] + average) / 2            
    return result

cleaned_data = clean_customers(raw_records)

for customer_id, data in cleaned_data.items():
    print(f"{customer_id}: Name: {data['name']}, Average Purchase: {data['average_purchase']:.2f}, Flag: {data['flag']}")