
override_doctype_class = {
	"Customer": "path to.custom.ERPNextCustomer",
	"Contact": "path.custom.ERPNextContact"
}

doc_events = {
	"Supplier": {
		"after_insert": "patch.custom.update_supplier_contact"
	}
}