import time

import allure
from selenium.webdriver.common.keys import Keys

import utilities.manage_pages as page
from extentions.ui_actions import UiActions


class ElectronFlows:
    @staticmethod
    @allure.step('Add new task flow')
    def add_new_task_flow(task_name):
        # Enter task name and simulate pressing Enter
        UiActions.update_text(page.electron_task.get_create(), task_name)
        UiActions.update_text(page.electron_task.get_create(), Keys.RETURN)

    @staticmethod
    @allure.step('Get number of tasks flow')
    def get_number_of_tasks_flow():
        # Return the number of task elements currently in the list
        return len(page.electron_task.get_tasks())

    @staticmethod
    @allure.step('Empty task from list flow')
    def empty_list_flow():
        # Loop through tasks and delete them one by one
        for x in range(ElectronFlows.get_number_of_tasks_flow()):
            time.sleep(0.5)
            UiActions.mouse_over_tooltip(page.electron_task.get_delete_buttons()[0])

