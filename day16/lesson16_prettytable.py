import prettytable

# one way
table = prettytable.PrettyTable()

table.field_names = ["Pokemon", "Type"]
table.add_row(["Pickachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

# another way!
table_2 = prettytable.PrettyTable()

table_2.add_column("Pokemon", ["Ponyta", "Bulbassaur"])
table_2.add_column("Type", ["Fire", "Grass"])

print(table)
print(table_2)

table.align["Pokemon"] = "l"
table.align["Type"] = "l"

print(table)
