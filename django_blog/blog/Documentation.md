#Authentication

1) Set Up User Authentication Views

- Authentication includes register, login and logout 
- To registeration: - SignUpView created on views.py which inherits built in CreateView class
                    - On forms.py, CustomUserCreationForm created which inherits built in UserCreationForm class andemail address added as registration attribute.
                    - On templates registration/signup.html added for registration.
                    - signup.html, file extended from base html, has forms with methode POST.
                    - url pattern added as required.

- To logout: - Built in LogoutView inherited and the url pattern defined.
             - Template defined as as origional view. 
             - Logout redirect towards /accounts/profile defined on settings.py

- To login: - Built in LoginView inherited on url patterns configuration.
            - Template defined registration/login.html.
            - Login redirect towards /registration/profile.

2) Implement Profile Management

- For authenticated users: - Allowed to change their information.
                           - CustomUserChangeForm created by inheriting built in class UserChangeForm.
                           - login_required created and used in views.


#Creating Blog Post Management Features

-ListView : -Used to display all views, overwrite model, context_object_name and template name
            -The context_object_name creates objects of all elements in Post model and pass it to template
            
-DetailView: -Used to display the detail of each post overwrite model, context_object_name and template name
             -The html will provide post.content (content of that blog)

-CreateView: -Used to to create blog
             -Uses LoginRequiredMixin snce it requires authentication
             -Overwrites form_class, by defining the fields to be given for creating new post
             -Set the author of the post to the current logged-in user

-UpdateView and DeleteView: -Used to update/edit their blog for users.
             -LoginRequiredMixin, to authenticate user
             -UserPassesTestMixin, to check if the editor is the author of the post


