customers = ["a","b","c","d"]
order_totals = [1000,2000,1500,750]
'''
customers.append("aa")
order_totals.append(500)

result_customers = customers
result_order_totals = order_totals
print(result_customers)
print(result_order_totals)

customers.pop()
order_totals.pop()
print(result_customers)
print(result_order_totals)
'''
for i in range(0,len(customers)):
    result = f"{customers[i]} isimli müşterinin sipariş toplamı {order_totals[i]} liradır."
    print(result)


result = customers.sort()  # alfabetik sıralama

result = order_totals.reverse() # azalan şekilde sıralama

result = min(order_totals)
result = max(order_totals)

result = customers.count("a") # kaç tane a var

result = customers.remove("c") # c değerini sil

result = customers.clear()
result = order_totals.clear() # tüm elemanlar silinir.


username = input("name: ")
order = input("total: ")

customers.append(username)
order_totals.append(order)