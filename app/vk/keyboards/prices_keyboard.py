from vkbottle import Keyboard, Text


def get_prices_keyboard():

    keyboard = Keyboard(one_time=False)

    keyboard.add(Text("🎮 PlayStation"))
    keyboard.row()

    keyboard.add(Text("🥽 VR"))
    keyboard.row()

    keyboard.add(Text("🎉 Мероприятия"))
    keyboard.row()

    keyboard.add(Text("⭐ Доп. услуги"))
    keyboard.row()

    keyboard.add(Text("⬅️ Назад"))

    return keyboard.get_json()