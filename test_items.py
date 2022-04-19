import time

class TestStore:
    def test_guest_should_see_basket_button(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        
        #Задержка по условию задания для визуальной проверки
        time.sleep(30)
        
        buttons = browser.find_elements_by_css_selector("#add_to_basket_form button")
        
        assert len(buttons)==1, 'Не найдена кнопка корзины или кнопок больше одной'
        