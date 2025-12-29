class Button:
    def click(self):
        raise NotImplementedError


class Checkbox:
    def check(self):
        raise NotImplementedError


class WinButton(Button):
    def click(self):
        return "WinButton"


class WinCheckbox(Checkbox):
    def check(self):
        return "WinCheckbox"


class MacButton(Button):
    def click(self):
        return "MacButton"


class MacCheckbox(Checkbox):
    def check(self):
        return "MacCheckbox"


class GUIFactory:
    def button(self):
        raise NotImplementedError

    def checkbox(self):
        raise NotImplementedError


class WinFactory(GUIFactory):
    def button(self):
        return WinButton()

    def checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):
    def button(self):
        return MacButton()

    def checkbox(self):
        return MacCheckbox()


if __name__ == "__main__":
    win = WinFactory()
    mac = MacFactory()
    print("Abstract Factory:", win.button().click(), win.checkbox().check(), "|", mac.button().click(), mac.checkbox().check())
