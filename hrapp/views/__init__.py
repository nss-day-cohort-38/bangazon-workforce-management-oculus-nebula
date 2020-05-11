from .home import home
from .auth.logout import logout_user

from .training_programs.training_programs_list import training_programs_list
from .training_programs.training_program_details import training_program_details
from .training_programs.training_program_form import training_program_form
from .training_programs.training_program_form import training_program_edit_form
from .training_programs.training_programs_attendees import employee_attendees
# from .training_programs.training_programs_list import list_count
# from .training_programs.training_program_details import attendee_list

from .computers import computer_list
from .computers import computer_list, computer_details
from .computers import computer_list, computer_details, computer_form, confirm_computer_delete

from .employees import employee_list, employee_details, employee_edit, employee_add

from .departments import department_list
