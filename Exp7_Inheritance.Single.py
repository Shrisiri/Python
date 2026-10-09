class Parent:
    Asset1 = "3BHK house"
    Asset2 = "Audi Car"


    def ParentMtd(self):
        print("Assets of Parent:")
        print('\nAsset1',self.Asset1)
        print('Asset2',self.Asset2)

class Child(Parent):
    Asset3 = "Toy House"

    def ChildMtd(self):
        print("\nAssets of Parent Inherited by Child:")
        print('\nAsset1',self.Asset1)
        print('Asset2',self.Asset2)
        print("\nAssets of Child:")
        print("\nAsset3",self.Asset3)

obj = Child()
obj.ParentMtd()
obj.ChildMtd()
    
