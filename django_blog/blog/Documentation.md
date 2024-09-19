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