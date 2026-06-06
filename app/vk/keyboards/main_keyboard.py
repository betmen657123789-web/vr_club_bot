from vkbottle import Keyboard, Text


def get_main_keyboard():

    keyboard = Keyboard(one_time=False)

    keyboard.add(Text("🟢 Свободно ли сейчас"))
    keyboard.row()

    keyboard.add(Text("📞 Забронировать"))
    keyboard.add(Text("ℹ️ О клубе"))
    keyboard.row()

    keyboard.add(Text("🎮 Тарифы и услуги"))
    keyboard.add(Text("❓ FAQ"))

    return keyboard.get_json()