class employee:
    name = "amr"
    address = "algeria"
    def printdata(self):
        print(self.name + ";" + self.address)

class emp(employee):
    pass

e1 =emp()
print(e1.name)
print("===============")

e1.printdata()
