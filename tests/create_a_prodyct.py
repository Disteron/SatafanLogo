from core.driver_action import DriverAction

WEB_NAME = 'http://admin.sarafan-test.app.cloud.ylab.site/login'

DICT_XPATH = {
    'Логин': '//input[@placeholder="Введите ваш Email"]',
    'Пароль': '//input[@placeholder="Введите ваш пароль"]',
    'Войти': '//button[@ng-click="login()"]',
    'Товары': '//i[@class="icon-bag icon text-success-lter"]',
    'Удалить': '//a[@class="btn btn-danger"]',
    'Ок': '//button[@class="btn btn-warning"]',
    'Страница3': '//a[@data-page="2"]',
    'Создать проект': '//a[text()="Создать продукт"]',
    'Название': '//input[@name="ProductCreateForm[title]"]',
    'Красткое описание': '//textarea[@name="ProductCreateForm[short_description]"]',
    'Описание': '//textarea[@name="ProductCreateForm[description]"]',
    'Сохронить': '//button[@name="signup-button"]',
    'clickНазвание': '//select[@name="ProductCreateForm[category_id]"]',
    'Подгруппа': '//option[@value="167"]',
    'Артикул (SKU)': '//input[@name="ProductCreateForm[vendor_code]"]',
    'clickЕдиницы измерения количества': '//select[@name="ProductCreateForm[quantity_units]"]',
    'Площадь': '//option[@value="area_m2"]',
    'Доступен в продаже': '//input[@name="ProductCreateForm[enabled]"]/..',
    'Рекомендованная цена': '//input[@name="ProductCreateForm[price]"]'
}


def get_xpath(name):
    return DICT_XPATH.get(name)


def test(start_browser):
    driver = start_browser
    driverObject = DriverAction(driver=driver, timeout=15)
    driverObject.go_to_web(WEB_NAME)
    driverObject.fill_field(field_xpath=get_xpath("Логин"), value=("admin@example.com"))
    driverObject.fill_field(field_xpath=get_xpath("Пароль"), value=("admin"))
    driverObject.click_button(xpath=get_xpath("Войти"))
    driverObject.click_button(xpath=get_xpath("Товары"))
    driverObject.click_button(xpath=get_xpath("Создать проект"))
    driverObject.fill_field(field_xpath=get_xpath("Название"), value=("test"))
    driverObject.click_button(xpath=get_xpath("clickНазвание"))
    driverObject.click_button(xpath=get_xpath("Подгруппа"))
    driverObject.fill_field(field_xpath=get_xpath("Артикул (SKU)"), value=("test"))
    driverObject.fill_field(field_xpath=get_xpath("Красткое описание"), value=("test"))
    driverObject.fill_field(field_xpath=get_xpath("Описание"), value=("test"))
    driverObject.click_button(xpath=get_xpath("clickЕдиницы измерения количества"))
    driverObject.click_button(xpath=get_xpath("Площадь"))
    driverObject.click_button(xpath=get_xpath("Доступен в продаже"))
    driverObject.fill_field(field_xpath=get_xpath("Рекомендованная цена"), value=("500.0000"))
    driverObject.click_button(xpath=get_xpath("Сохронить"))



