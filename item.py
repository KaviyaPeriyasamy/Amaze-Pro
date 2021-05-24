from erpnext.stock.doctype.item.item import Item
class ERPNextItem(Item):
    def autoname(self):
        if self.item_group == "Alloy":
        	self.item_name = f'{self.alloy_name } {self.hardness} {self. thickness} {self.grade} {self.item_type}'
		self.item_code = f'{self.alloy_name[0:2]}-{self.hardness[0:3]}-{self.thickness[0:3]}-{self.grade[0:3]}- {self.item_type[0:2]}'
        if self.item_group == "Spring ":
            self.item_name = f'{self.coil_hook } {self.length} {self. coil_number }'
            self.item_code = f'{self.coil_hook[0:2]}-{self.length}-{self.coil_number}'
            if self.item_group == "Rivet":
                self.item_name = f'{self.item_type} {self.od}{self.head_diameter}/ {self.shunk_diameter}{self.length} {self.head_type}'
                self.item_code = f'{self.item_type[0:2]}-{ self.od}{self.head_diameter}/ {self.shunk_diameter}{self.length}-{self.head_type[0:3]}'
