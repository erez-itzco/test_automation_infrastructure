import allure

from extentions.verifications import Verifications
from workflows.api_flows import APIFlows

team_name = 'Erez'
team_email = 'erez@gmail.com'

class Test_API:
    @allure.title('Test01: Create team & Verify Status Code')
    @allure.description('this test creates new team in grafana')
    def test_create_and_verify_team(self):
        actual = APIFlows.create_team(team_name, team_email)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test02: Verify Team Name')
    @allure.description('this test verifies the grafana team member name')
    def test_verify_team_member_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name)

    @allure.title('Test03: Update Team & Verify Status Code')
    @allure.description('this test Update Team & Verify Status Code')
    def test_update_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.update_team(team_name + ' Itzcovich', team_email, id)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test04: Update Team Name')
    @allure.description('this test Verifies team member name')
    def test_verify_team_updated_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual,team_name + ' Itzcovich')

    @allure.title('Test05: Delete Team & Verify Status Code')
    @allure.description('this test delete and verify status code')
    def test_delete_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.delete_team(id)
        Verifications.verify_equals(actual, 200)








