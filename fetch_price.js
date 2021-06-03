frappe.ui.form.on("Table name",
{
	item_code: function(frm, cdt, cdn) {
	    const d = locals[cdt][cdn];
	    if (d.item_code) {
        frappe.db.get_value(
          "Item Price",
          { item_code: d.item_code, price_list: "Standard Selling" },
          "price_list_rate",
          (r) => {
            frappe.model.set_value(
              cdt,
              cdn,
              "rate",
              r.price_list_rate
            );
          }
        );
      }
	}
});
