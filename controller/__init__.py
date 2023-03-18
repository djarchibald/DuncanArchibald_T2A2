from controller.home_controller import home
from controller.users_controller import user
from controller.lenses_controller import lens
from controller.comments_controller import comment
from controller.borrows_controller import borrow


registerable_controllers = [

    home,
    user,
    lens,
    comment,
    borrow,
]