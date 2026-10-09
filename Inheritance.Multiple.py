class Parent:
    Asset1 = "3BHK house"
    Asset2 = "Audi Car"
class Parent2:
    Asset4 = "1BHK house"
    Asset5 = "Bmw Bike"


    def ParentMtd(self):
        print("Assets of Parent1:")
        print('\nAsset1',self.Asset1)
        print('Asset2',self.Asset2)
    def ParentMtd2(self):
        print("Assets of Parent2:")
        print('\nAsset4',self.Asset4)
        print('Asset5',self.Asset5)
        
class Child(Parent,Parent2):
    Asset3 = "Toy House"

    def ChildMtd(self):
        print("\nAssets of Parent Inherited by Child:")
        print('\nAsset1',self.Asset1)
        print('Asset2',self.Asset2)
        print('Asset4',self.Asset4)
        print('Asset5',self.Asset5)
        print("\nAssets of Child:")
        print("\nAsset3",self.Asset3)

obj = Child()
obj.ParentMtd()
obj.ParentMtd2()
obj.ChildMtd()
    
