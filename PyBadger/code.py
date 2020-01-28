from adafruit_pybadger import PyBadger

badge = PyBadger()

def show_badge():
    badge.show_badge(
        hello_font="Aller-14.bdf",
        hello_scale=1,
        my_name_is_font='Aller-14.bdf',
        my_name_is_scale=1,
        name_string="Mikey",
        name_scale=1,
        name_font="Warehouse-40.bdf",
    )

show_badge()

while True:
    badge.auto_dim_display(delay=30)
    if badge.button.a:
        badge.show_business_card(
            image_name="m_libby.bmp",
            name_string="Michael C. Libby",
            name_scale=1,
            name_font="Aller-14.bdf",
            email_string_one="m@",
            email_string_two="mlibby.com",
        )
    elif badge.button.b:
        badge.show_qr_code(data="https://mlibby.com")
    elif badge.button.start:
        show_badge()
