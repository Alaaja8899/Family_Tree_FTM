// Copyright (c) 2025, Abdirizak abdullahi (alaaja) and contributors
// For license information, please see license.txt

frappe.ui.form.on('Person Profile', {
	// refresh: function(frm) {

	// }
	// on person_type change
	person_type: function(frm) {
		if (frm.doc.person_type == "Big Parent") {
			// hide the parent field
			frm.set_df_property("parent_profile", "hidden", 1);
		}else{
			frm.set_df_property("parent_profile", "hidden", 0);
		}
	},
	// parent_profile doctype i need to show only gender ==  male only make filter
	parent_profile: function(frm) {
		frm.set_query("parent_profile", function() {
					return {
						"filters": {
							"gender": "Male"
						}
					};
				}
			);
		}
	
});