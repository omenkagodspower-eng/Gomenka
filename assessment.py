import json
import os
Data_file = "learn2earn_data_JSON"
resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

def borrow_resource(fellow_id, res_id, qty):
    qty = int(qty)
    if fellow_id not in fellows or qty <= 0: return print("❌ Rejected: Invalid fellow or Quantity.")
    res = next((r for r in resources if r["id"] == res_id), None)
    if not res or qty > res["available"]: return print(f"❌ Rejected: Insufficient stock for {res_id}.")
   
    res["available"] -= qty
    borrow_records.append({"fellow_id": fellow_id, "resource_id": res_id, "qty": qty})
    print(f"✅ {fellows[fellow_id]} borrowed {qty} {res['name']}(s). Available: {res['available']}")

def return_resource(fellow_id, res_id, qty):
    qty = int(qty)
    res = next((r for r in resources if r["id"] == res_id), None)
    borrowed = sum(rec["qty"] for rec in borrow_records if rec["fellow_id"] == fellow_id and rec["resource_id"] == res_id)
    if not res or qty <= 0 or qty > borrowed: return print("❌ Rejected: Return amount exceeds active loans.")
   
    borrow_records.append({"fellow_id": fellow_id, "resource_id": res_id, "qty": -qty})
    res["available"] += qty
    print(f"✅ {fellows[fellow_id]} returned {qty} {res['name']}(s). Available: {res['available']}")

def search_inventory(term):
    matches = [r for r in resources if term.lower() in r["name"].lower()]
    print(f"🔍 Search for '{term}': Found {[m['name'] for m in matches]}")

def generate_report():
    tot, av = sum(r["total"] for r in resources), sum(r["available"] for r in resources)
    low = [r["name"] for r in resources if r["available"] < 3]
    max_b = max((r["total"] - r["available"]) for r in resources)
    most_b = [r["name"] for r in resources if (r["total"] - r["available"]) == max_b and max_b > 0]
   
    print(f"\n📊 REPORT:\n- Total: {tot}\n- Available: {av}\n- Borrowed: {tot - av}")
    print(f"- Low Stock (<3): {', '.join(low)}\n- Most Borrowed: {', '.join(most_b)} ({max_b} units)")

print("1."); borrow_resource("F001", "R001", 2)
print("2."); borrow_resource("F002", "R002", 3)
print("3."); return_resource("F001", "R001", 1)
print("4."); borrow_resource("F003", "R003", 4)
print("5."); return_resource("F002", "R002", 4)
print("6."); search_inventory("LAPtop")
print("7."); generate_report()    


items = [2, 4, 6]
result = []
for item in items:
    if item % 4 == 0:
        continue
    result.append(item * 2)
print(result)


def borrow(resource, quantity):
    if resource["available"] < quantity:
        return "Not enough stock"
    resource["available"] -= quantity
    return "Success"


transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

def get_total_per_fellow(transactions_list):
    totals = {}

    for t in transactions_list:  
        name = t["fellow"]
        qty = t["quantity"]
        if name in totals:
            totals[name] += qty
        else:
            totals[name] = qty
            
    return totals

print(get_total_per_fellow(transactions))


resources = [
    {"name": "Laptop", "available": 0},
    {"name": "Mouse", "available": 0},
    {"name": "Keyboard", "available": 3}
]

# Keep only items with stock greater than 0
resources = [r for r in resources if r["available"] > 0]

print(resources)
