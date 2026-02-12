class Treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        # self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def prints(self):
        print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                print("   |__" + child.data)
                for words in child.children:
                    print("      |__" + words.data)


def product_tree():
    root1 = Treenode('Electronics')

    laptop = Treenode('laptop')
    laptop.add_child(Treenode('hp'))
    laptop.add_child(Treenode('asus'))

    tv = Treenode('tv')
    tv.add_child(Treenode('lg'))
    tv.add_child(Treenode('samsung'))

    root1.add_child(laptop)
    root1.add_child(tv)

    return root1
    
    # root2 = Treenode('Food')

    # breakfast = Treenode('Breakfast')
    # breakfast.add_child(Treenode('Bread'))
    # breakfast.add_child(Treenode('poha'))

    # dinner = Treenode('Dinner')
    # dinner.add_child(Treenode('Sabji-roti'))
    # dinner.add_child(Treenode('Dal-Rice'))

    # root2.add_child(breakfast)
    # root2.add_child(dinner)

    
    # return root2

dharm = product_tree()
# print(dharm.data)
dharm.prints()
