frutas = ["Maça", "Banana", "Laranja"]

#Index()
print("Index(): ", frutas.index("Banana"))

# Count()
print("Count(): ", frutas.count("Banana"))

# Append
frutas.append("Uva")
print("Append(): ", frutas)

# Extend()
outras_frutas = ["Abacaxi", "Morango"]
frutas.extend(outras_frutas)
print("Extend(): ", frutas)