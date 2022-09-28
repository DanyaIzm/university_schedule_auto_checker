import time
from scrapper.base import BaseScrapper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class SutScrapper(BaseScrapper):
    def __init__(self, driver_service, env_manager, notifier_manager):
        super().__init__(driver_service, env_manager, notifier_manager)

    def check(self):
        url = self.env_manager.get_var('LK_URL')
        for student_info in self.env_manager.get_var('STUDENTS').split('|'):
            login, password = student_info.split(',')
            try:
                self.driver = webdriver.Chrome(service=self.driver_service)
                self._check_student(url, login, password)
                self.driver.close()
            except Exception as e:
                self.notifier_manager.send_error_message(f'Ошибка при попытке отметить {login};\n{e}')

    def _check_student(self, url, student_login, student_password):
        self.driver.get(url)

        ### Login page ###
        login_input = self._get_html_element(10, (By.ID, 'users'))
        password_input = self._get_html_element(10, (By.ID, 'parole'))
        login_sumbit_button = self._get_html_element(10, (By.ID, 'logButton'))

        login_input.send_keys(student_login)
        password_input.send_keys(student_password)
        login_sumbit_button.click()

        ### Main page ###
        study_button = self._get_html_elements(10, (By.CLASS_NAME, 'lm_item'))[0]
        study_button.click()
        
        schedule_link = self._get_html_element(10, (By.LINK_TEXT, 'Расписание'))
        schedule_link.click()

        table = self._get_html_element(10, (By.CLASS_NAME, 'simple-little-table'))
        
        lessons = table.find_elements(By.CSS_SELECTOR, '[style="background: #FF9933 !important "]')

        if not lessons:
            raise Exception('\nНе удалось найти активные пары на сегодня')
        
        for lesson in lessons:
            lesson_cells = lesson.find_elements(By.TAG_NAME, 'td')

            lesson_time = lesson_cells[0].text
            lesson_name = lesson_cells[1].find_element(By.TAG_NAME, 'b').text

            try:
                checking_link = lesson_cells[-1].find_element(By.TAG_NAME, 'a')

                if 'Начать' in checking_link.text:
                    while True:
                        # Пытаемся нажать на кнопку, так как она не всегда реагирует
                        checking_link.click()
                        if not self._is_element_exists(lesson_cells[-1], (By.TAG_NAME, 'a')):
                            self.notifier_manager.send_success_message(student_login, lesson_time, lesson_name)
                            break
                elif 'Обновить' in checking_link.text and not ('появится' in checking_link.text):
                    self.notifier_manager.send_lesson_not_started_message(student_login, lesson_time, lesson_name)
                
            except Exception as e:
                continue
    
    def _get_html_element(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def _get_html_elements(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    def _is_element_exists(self, root, selector):
        try:
            root.find_element(*selector)
            return True
        except NoSuchElementException:
            return False
