class GrandParent:
     Asset = "100KG GOLD"
     Asset0 = "100 acre Land"

     def GrandParentMtd(self):
        print("Assets of GrandParent:")
        print('\nAsset',self.Asset)
        print('Asset0',self.Asset0)


class Parent(GrandParent):
    Asset1 = "3BHK house"
    Asset2 = "Audi Car"

    
    def ParentMtd(self):
        print("\nAssets of GrandParent Inherited by Parent:")
        print("\nAsset",self.Asset)
        print("Asset0",self.Asset0)
        print("\nAssets of Parent:")
        print('\nAsset1',self.Asset1)
        print('Asset2',self.Asset2)

class Child(Parent):
    Asset3 = "Toy House"

    def ChildMtd(self):
        print("\nAssets of GrandParent Inherited by Child:")
        print("\nAsset",self.Asset)
        print("Asset0",self.Asset0)
        print("\nAssets of Parent Inherited by Child:")
        print('\nAsset1',self.Asset1)
        print('Asset2',self.Asset2)
        print("\nAssets of Child:")
        print("\nAsset3",self.Asset3)

obj = Child()
obj.GrandParentMtd()
obj.ParentMtd()
obj.ChildMtd()
