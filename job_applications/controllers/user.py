import frappe

def assgin_role_on_submit(doc, event):
    doc.role_profile_name = "Job Applicant"
    doc.save(ignore_permissions=True)
                


    

