# <div class="form_holder">
#     <!-- <p> step {{wizard.steps.step1}} of {{wizard.steps.count}}</p> -->
#     {% for field in form %}
#     {{ field.error}}
#     {% endfor %}

#     <!-- <h2 class="fs-title">Submit your Manuscript</h2> -->
#     <h6 class="fs-subtitle">This is {{wizard.steps.step1}} of {{wizard.steps.count}}</h6>
#    <h4>{{token}}</h4> 
#     <form id="msform" action="" method="POST"> {% csrf_token %}
#         {{wizard.management_form}}
#         {% if wizard.form.forms %}
#             {{wizard.form.management_form}}
#             {% for form in wizard.form.forms %}
#             <div class="row">
#                 <div class="col-lg-8">
#                     {{form|crispy}}
#                 </div>
#             </div>
                
#             {% endfor %}
#         {% else %}
#         <div class="row">
#             <div class="col-lg-8">
#                 {{wizard.form|crispy}}
               
               
       
#         {% endif %}

#         {% if wizard.steps.prev %}
#         <!-- <button class="btn btn-primary" type="submit" name="wizard_goto_step"  value="{{wizard.steps.first}}">First step</button> -->
#         <button class="btn btn-secondary"  formnovalidate="formnovalidate" name="wizard_goto_step"  value="{{wizard.steps.prev}}">Previous</button>
#         {% endif %}
#         <input type="submit" name="submit" class="btn btn-info" value="Next" />

#     </div>
# </div>
        

      
#     </form>
#     </div>


   # multipart form wizard url
    # path('dashboard/submit/', SubmitWizard.as_view([ManuscriptForm,CoAuthorsForm,UploadsForm]), name="submit_script"),




#     class SubmitWizard(SessionWizardView):
#     template_name = "dashboard/submit_script.html"
#     # random_num =  random.randint(23456789, 992345678)
#     token = 22
#     file_storage = DefaultStorage()
#     def done(self, form_list, **kwargs):
#         form_data = process_form_data(form_list)
#         return render('dashboard/submit_done.html', {'form_data': form_data})
# def process_form_data(form_list):
#     form_data = [form.cleaned_data for form in form_list]

    # send_mail(form_data, ['contactravenmedia@gmail.com'], fail_silently=False)
    # if form_data.is_valid():
    #     form_data.save()







  
#   <!-- Modal -->
#   <!-- <form action="" method="POST">
#   <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
#     <div class="modal-dialog" role="document">
#       <div class="modal-content">
#         <div class="modal-header">
#           <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
#           <button type="button" class="close" data-dismiss="modal" aria-label="Close">
#             <span aria-hidden="true">&times;</span>
#           </button>
#         </div>
#         <div class="modal-body">
#         {{coauthorform|crispy}}
#         </div>
#         <div class="modal-footer">
#           <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
#           <button type="button" class="btn btn-primary">Add</button>
#         </div>
#       </div>
#     </div>
#   </div>
# </form> -->
# <!-- Button trigger modal -->
