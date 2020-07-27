import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from kivy.storage.jsonstore import JsonStore
import datetime
from datetime import date
import random

class ChooseScreen(Screen):
    pass
class StartScreen(Screen):
    pass
class HomeScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class SaveScreen(Screen):
    pass
class ReadyExit(Screen):
    pass
class LoadScreen(Screen):
    pass

GUI = Builder.load_file("aukcioner.kv")

class MainApp(App):
    def build(self):
        self.count = 0
        self.check = True
        self.value = "+"

        self.d = datetime.date.today()
        self.years = self.d.year
        self.months = self.d.month
        self.days = self.d.day
        self.current_time = datetime.date.today()

        try:
            dirName = '/storage/emulated/0/Android/data/com.akcioner'
            try:
                os.mkdir(dirName)
            except FileExistsError:
                pass
        except FileNotFoundError:
            pass

        return GUI
    def change_screen(self, screen_name):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        start_screen = self.root.ids["start_screen"]
        second_screen = self.root.ids["second_screen"]
        text_name = start_screen.ids["text_name"]
        cost_input = second_screen.ids["cost_input"]
        cost_label = second_screen.ids["show_cost_label"]
        cost_show = second_screen.ids["show_cost"]
        cost_show.text = ""
        cost_label.text = ""
        cost_input.text = ""
        if text_name.text == "":
            screen_manager.current = "start_screen"
        else:
            screen_manager.current = screen_name

        if screen_name == "home_screen":
            self.exit = False
        if screen_name == "start_screen":
            text_name.text = ""
        if screen_name == "choose_screen":
            home_screen = self.root.ids["home_screen"]
            menu_name = home_screen.ids["menu_name"]
            menu_time = home_screen.ids["menu_time"]
            menu_count = home_screen.ids["menu_count"]
            menu_money = home_screen.ids["menu_money"]
            menu_capital = home_screen.ids["menu_capital"]
            apple_cost = home_screen.ids["apple_cost"]
            google_cost = home_screen.ids["google_cost"]
            facebook_cost = home_screen.ids["facebook_cost"]
            microsoft_cost = home_screen.ids["microsoft_cost"]
            yandex_cost = home_screen.ids["yandex_cost"]
            bitcoin_cost = home_screen.ids["bitcoin_cost"]
            kol_vo1 = home_screen.ids["kol_vo1"]
            kol_vo2 = home_screen.ids["kol_vo2"]
            kol_vo3 = home_screen.ids["kol_vo3"]
            kol_vo4 = home_screen.ids["kol_vo4"]
            kol_vo5 = home_screen.ids["kol_vo5"]
            kol_vo6 = home_screen.ids["kol_vo6"]
            raznica1 = home_screen.ids["raznica1"]
            raznica2 = home_screen.ids["raznica2"]
            raznica3 = home_screen.ids["raznica3"]
            raznica4 = home_screen.ids["raznica4"]
            raznica5 = home_screen.ids["raznica5"]
            raznica6 = home_screen.ids["raznica6"]

            menu_name.text = " "
            menu_time.text = str(self.current_time)
            menu_count.text = "0"
            menu_money.text = "10,000.00$"
            menu_capital.text = "10000.00$"
            apple_cost.text = "267$"
            google_cost.text = "39$"
            facebook_cost.text = "175$"
            microsoft_cost.text = "165$"
            yandex_cost.text = "36$"
            bitcoin_cost.text = "9232$"
            kol_vo1.text = "0"
            kol_vo2.text = "0"
            kol_vo3.text = "0"
            kol_vo4.text = "0"
            kol_vo5.text = "0"
            kol_vo6.text = "0"
            raznica1.text = "0"
            raznica2.text = "0"
            raznica3.text = "0"
            raznica4.text = "0"
            raznica5.text = "0"
            raznica6.text = "0"
    def change_screen_money(self, screen_name):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        if self.check == False:
            screen_manager.current = "second_screen"
        else:
            screen_manager.current = screen_name
    def change_screen_save(self):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = "save_screen"
        self.exit = True
    def capital(self):
        home_screen = self.root.ids["home_screen"]
        menu_money = home_screen.ids["menu_money"]
        menu_capital = home_screen.ids["menu_capital"]

        menumoney = menu_money.text.replace("$", "")
        menumoney = menumoney.replace(",", "")

        kol_vo1 = home_screen.ids["kol_vo1"]
        kol_vo2 = home_screen.ids["kol_vo2"]
        kol_vo3 = home_screen.ids["kol_vo3"]
        kol_vo4 = home_screen.ids["kol_vo4"]
        kol_vo5 = home_screen.ids["kol_vo5"]
        kol_vo6 = home_screen.ids["kol_vo6"]

        cost_1 = home_screen.ids["apple_cost"]
        cost1 = cost_1.text.replace("$", "")
        cost_2 = home_screen.ids["google_cost"]
        cost2 = cost_2.text.replace("$", "")
        cost_3 = home_screen.ids["facebook_cost"]
        cost3 = cost_3.text.replace("$", "")
        cost_4 = home_screen.ids["microsoft_cost"]
        cost4 = cost_4.text.replace("$", "")
        cost_5 = home_screen.ids["yandex_cost"]
        cost5 = cost_5.text.replace("$", "")
        cost_6 = home_screen.ids["bitcoin_cost"]
        cost6_2 = cost_6.text.replace("$", "")
        cost6 = cost6_2.replace(",", "")

        a = float(cost1) * int(kol_vo1.text)
        b = float(cost2) * int(kol_vo2.text)
        c = float(cost3) * int(kol_vo3.text)
        d = float(cost4) * int(kol_vo4.text)
        e = float(cost5) * int(kol_vo5.text)
        f = float(cost6) * int(kol_vo6.text)
        formula = float(menumoney) + a + b + c + d + e + f
        capital = '{:0,.2f}'.format(formula)
        menu_capital.text = str(capital) + "$"
    def change_text(self, label_text, choose):
        second_screen = self.root.ids["second_screen"]
        menu_label = second_screen.ids["menu_label"]
        home_screen = self.root.ids["home_screen"]
        kol_vo1 = home_screen.ids["kol_vo1"]
        kol_vo2 = home_screen.ids["kol_vo2"]
        kol_vo3 = home_screen.ids["kol_vo3"]
        kol_vo4 = home_screen.ids["kol_vo4"]
        kol_vo5 = home_screen.ids["kol_vo5"]
        kol_vo6 = home_screen.ids["kol_vo6"]

        menu_label.text = label_text

        home_screen = self.root.ids["home_screen"]
        company_label = second_screen.ids["company_label"]
        cost_label = second_screen.ids["cost_label"]
        apple_cost = home_screen.ids["apple_cost"]
        google_cost = home_screen.ids["google_cost"]
        facebook_cost = home_screen.ids["facebook_cost"]
        microsoft_cost = home_screen.ids["microsoft_cost"]
        yandex_cost = home_screen.ids["yandex_cost"]
        bitcoin_cost = home_screen.ids["bitcoin_cost"]

        if choose == 1:
            company_label.text = "Apple"
            cost_label.text = apple_cost.text
            self.kol_vo = kol_vo1
        if choose == 2:
            company_label.text = "Google"
            cost_label.text = google_cost.text
            self.kol_vo = kol_vo2
        if choose == 3:
            company_label.text = "Facebook"
            cost_label.text = facebook_cost.text
            self.kol_vo = kol_vo3
        if choose == 4:
            company_label.text = "Microsoft"
            cost_label.text = microsoft_cost.text
            self.kol_vo = kol_vo4
        if choose == 5:
            company_label.text = "Yandex"
            cost_label.text = yandex_cost.text
            self.kol_vo = kol_vo5
        if choose == 6:
            company_label.text = "Bitcoin"
            cost_label.text = bitcoin_cost.text
            self.kol_vo = kol_vo6

        buy_money = second_screen.ids["buy_money"]
        buy_button = second_screen.ids["buy_button"]
        menu_money = home_screen.ids["menu_money"]
        if label_text == "Покупка":
            buy_money.text = menu_money.text
            buy_button.text = "Заплатить"
        if label_text == "Продажа":
            buy_button.text = "Продать"
            if choose == 1:
                buy_money.text = kol_vo1.text + " акций"
            if choose == 2:
                buy_money.text = kol_vo2.text + " акций"
            if choose == 3:
                buy_money.text = kol_vo3.text + " акций"
            if choose == 4:
                buy_money.text = kol_vo4.text + " акций"
            if choose == 5:
                buy_money.text = kol_vo5.text + " акций"
            if choose == 6:
                buy_money.text = kol_vo6.text + " акций"
    def operation(self):
        second_screen = self.root.ids["second_screen"]
        menu_label = second_screen.ids["menu_label"]
        if menu_label.text == "Покупка":
            self.minus_money()
        if menu_label.text == "Продажа":
            self.plus_money()
    def change_name(self, label_name):
        home_screen = self.root.ids["home_screen"]
        menu_name = home_screen.ids["menu_name"]
        menu_name.text = label_name
    def change_time(self):
        home_screen = self.root.ids["home_screen"]
        self.menu_time = home_screen.ids["menu_time"]
        try:
            d = date(self.years, self.months, self.days)
        except ValueError:
            self.months += 1
            self.days = 1
            try:
                d = date(self.years, self.months, self.days)
            except ValueError:
                self.months = 1
                self.years += 1
                d = date(self.years, self.months, self.days)
        d.replace(day=self.days)
        self.days += 1
        self.menu_time.text = (str(d))
    def change_count(self):
        home_screen = self.root.ids["home_screen"]
        menu_count = home_screen.ids["menu_count"]
        self.count += 1
        menu_count.text = str(self.count)
    def change_value(self):
        home_screen = self.root.ids["home_screen"]
        cost_1 = home_screen.ids["apple_cost"]
        cost_1.text = cost_1.text.replace("$", "")
        cost_2 = home_screen.ids["google_cost"]
        cost_2.text = cost_2.text.replace("$", "")
        cost_3 = home_screen.ids["facebook_cost"]
        cost_3.text = cost_3.text.replace("$", "")
        cost_4 = home_screen.ids["microsoft_cost"]
        cost_4.text = cost_4.text.replace("$", "")
        cost_5 = home_screen.ids["yandex_cost"]
        cost_5.text = cost_5.text.replace("$", "")
        cost_6 = home_screen.ids["bitcoin_cost"]
        cost_6_2 = cost_6.text.replace("$", "")
        cost_6.text = cost_6_2.replace(",", "")
        cost = [cost_1, cost_2, cost_3, cost_4, cost_5, cost_6]
        raznica1 = home_screen.ids["raznica1"]
        raznica2 = home_screen.ids["raznica2"]
        raznica3 = home_screen.ids["raznica3"]
        raznica4 = home_screen.ids["raznica4"]
        raznica5 = home_screen.ids["raznica5"]
        raznica6 = home_screen.ids["raznica6"]
        raznica = [raznica1, raznica2, raznica3, raznica4, raznica5, raznica6]
        for i in range(0, 6):
            chance = random.randint(1, 10)
            if int(chance) <= 6:
                if self.value == "+":
                    self.value = "+"
                    value = 1
                elif self.value == "-":
                    self.value = "-"
                    value = -1
            if int(chance) >= 7:
                if self.value == "+":
                    self.value = "-"
                    value = -1
                elif self.value == "-":
                    self.value = "+"
                    value = 1
            number = random.uniform(0, 4)
            number = '{:0,.2f}'.format(number)
            cost2 = float(cost[i].text) * float(number) / 100
            cost3 = float(cost[i].text) + float(cost2 * value)
            cost3 = '{:0,.2f}'.format(cost3)
            cost4 = cost3.replace(",", "")
            cost[i].text = cost4 + "$"
            raznica[i].text = str(cost2)
            raznica_2 = '{:0,.2f}'.format(float(raznica[i].text))
            raznica[i].text = str(raznica_2) + "$"
            if self.value == "+":
                raznica[i].color = [0, 1, 0, 1]
            elif self.value == "-":
                raznica[i].color = [1, 0, 0, 1]
    def multiply(self):
        second_screen = self.root.ids["second_screen"]
        cost_label = second_screen.ids["show_cost_label"]
        cost_input = second_screen.ids["cost_input"]
        cost_show = second_screen.ids["show_cost"]
        cost = second_screen.ids["cost_label"]
        cost_text = cost.text
        cost_text = cost_text.replace("$", "")
        try:
            a = float(cost_text) * float(cost_input.text)
        except ValueError:
            a = 0
        ar = '{:0,.2f}'.format(a)
        cost_show.text = "стоит: "
        cost_label.text = str(ar) + "$"
    def max(self):
        second_screen = self.root.ids["second_screen"]
        cost_input = second_screen.ids["cost_input"]
        menu_label = second_screen.ids["menu_label"]
        buy_money = second_screen.ids["buy_money"]
        cost_label = second_screen.ids["cost_label"]
        cost_show = second_screen.ids["show_cost"]
        costlabel = second_screen.ids["show_cost_label"]
        company_label = second_screen.ids["company_label"]
        if menu_label.text == "Покупка":
            buy2 = buy_money.text.replace(",", "")
            buy = buy2.replace("$", "")
            if company_label.text == "Bitcoin":
                cost_2 = cost_label.text.replace("$", "")
                cost = cost_2.replace(",", "")
            else:
                cost = cost_label.text.replace("$", "")
            try:
                cost_input.text = str(int(float(buy) / float(cost)))
            except ValueError:
                pass
            a = int(cost_input.text) * float(cost)
            ar = '{:0,.2f}'.format(a)
            cost_show.text = "стоит: "
            costlabel.text = str(ar) + "$"
        elif menu_label.text == "Продажа":
            if company_label.text == "Bitcoin":
                cost_2 = cost_label.text.replace("$", "")
                cost = cost_2.replace(",", "")
            else:
                cost = cost_label.text.replace("$", "")
            buy = buy_money.text.replace(" акций", "")
            cost_input.text = buy
            a = int(cost_input.text) * float(cost)
            ar = '{:0,.2f}'.format(a)
            cost_show.text = "стоит: "
            costlabel.text = str(ar) + "$"
    def minus_money(self):
        self.check = True
        home_screen = self.root.ids["home_screen"]
        menu_money = home_screen.ids["menu_money"]
        second_screen = self.root.ids["second_screen"]
        cost_label = second_screen.ids["show_cost_label"]
        cost_input = second_screen.ids["cost_input"]
        self.multiply()
        b = "$,"
        for char in b:
            menu_money.text = menu_money.text.replace(char, "")
            cost_label.text = cost_label.text.replace(char, "")
        menumoney = float(menu_money.text) - float(cost_label.text)
        if menumoney < 0 or cost_input.text == "":
            self.check = False
            self.multiply()
            ar = '{:0,.2f}'.format(float(menu_money.text))
            menu_money.text = str(ar + "$")
        else:
            self.check = True
            ar = '{:0,.2f}'.format(menumoney)
            menu_money.text = str(ar + "$")
            self.kol_vo.text = str(int(self.kol_vo.text) + int(cost_input.text))
    def plus_money(self):
        self.check = True
        home_screen = self.root.ids["home_screen"]
        menu_money = home_screen.ids["menu_money"]
        second_screen = self.root.ids["second_screen"]
        cost_label = second_screen.ids["show_cost_label"]
        cost_input = second_screen.ids["cost_input"]
        self.multiply()
        b = "$,"
        for char in b:
            menu_money.text = menu_money.text.replace(char, "")
            cost_label.text = cost_label.text.replace(char, "")
        menumoney = float(menu_money.text) + float(cost_label.text)
        try:
            kol_vo = int(self.kol_vo.text) - int(cost_input.text)
        except ValueError:
            kol_vo = 0
        if kol_vo < 0 or cost_input.text == "":
            self.check = False
            self.multiply()
            ar = '{:0,.2f}'.format(float(menu_money.text))
            menu_money.text = str(ar + "$")
        else:
            self.check = True
            ar = '{:0,.2f}'.format(menumoney)
            menu_money.text = str(ar + "$")
            self.kol_vo.text = str(kol_vo)
    def plus_cost_input(self, plus):
        second_screen = self.root.ids["second_screen"]
        cost_input = second_screen.ids["cost_input"]
        try:
            cost = int(cost_input.text)
        except ValueError:
            cost = 0
        if plus == 10:
            cost_input.text = str(cost + 10)
        if plus == 20:
            cost_input.text = str(cost + 20)
        if plus == 30:
            cost_input.text = str(cost + 30)
        if plus == 40:
            cost_input.text = str(cost + 40)
        if plus == 50:
            cost_input.text = str(cost + 50)
    def check_cost_input(self, text):
        self.multiply()
    def load(self, file):
        home_screen = self.root.ids["home_screen"]
        menu_name = home_screen.ids["menu_name"]
        menu_time = home_screen.ids["menu_time"]
        menu_count = home_screen.ids["menu_count"]
        menu_money = home_screen.ids["menu_money"]
        menu_capital = home_screen.ids["menu_capital"]
        apple_cost = home_screen.ids["apple_cost"]
        google_cost = home_screen.ids["google_cost"]
        facebook_cost = home_screen.ids["facebook_cost"]
        microsoft_cost = home_screen.ids["microsoft_cost"]
        yandex_cost = home_screen.ids["yandex_cost"]
        bitcoin_cost = home_screen.ids["bitcoin_cost"]
        kol_vo1 = home_screen.ids["kol_vo1"]
        kol_vo2 = home_screen.ids["kol_vo2"]
        kol_vo3 = home_screen.ids["kol_vo3"]
        kol_vo4 = home_screen.ids["kol_vo4"]
        kol_vo5 = home_screen.ids["kol_vo5"]
        kol_vo6 = home_screen.ids["kol_vo6"]
        raznica1 = home_screen.ids["raznica1"]
        raznica2 = home_screen.ids["raznica2"]
        raznica3 = home_screen.ids["raznica3"]
        raznica4 = home_screen.ids["raznica4"]
        raznica5 = home_screen.ids["raznica5"]
        raznica6 = home_screen.ids["raznica6"]

        if file == 1:
            json = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file1.json')
        elif file == 2:
            json = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file2.json')
        elif file == 3:
            json = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file3.json')

        menu_name.text = json.get('menu_name')['name']
        menu_time.text = json.get('menu_time')['name']
        menu_count.text = json.get('menu_count')['name']
        menu_money.text = json.get('menu_money')['name']
        menu_capital.text = json.get('menu_capital')['name']
        apple_cost.text = json.get('apple_cost')['name']
        google_cost.text = json.get('google_cost')['name']
        facebook_cost.text = json.get('facebook_cost')['name']
        microsoft_cost.text = json.get('microsoft_cost')['name']
        yandex_cost.text = json.get('yandex_cost')['name']
        bitcoin_cost.text = json.get('bitcoin_cost')['name']
        kol_vo1.text = json.get('kol_vo1')['name']
        kol_vo2.text = json.get('kol_vo2')['name']
        kol_vo3.text = json.get('kol_vo3')['name']
        kol_vo4.text = json.get('kol_vo4')['name']
        kol_vo5.text = json.get('kol_vo5')['name']
        kol_vo6.text = json.get('kol_vo6')['name']
        raznica1.text = json.get('raznica1')['name']
        raznica2.text = json.get('raznica2')['name']
        raznica3.text = json.get('raznica3')['name']
        raznica4.text = json.get('raznica4')['name']
        raznica5.text = json.get('raznica5')['name']
        raznica6.text = json.get('raznica6')['name']

        self.change_screen("home_screen")
    def save(self, file):
        home_screen = self.root.ids["home_screen"]
        menu_name = home_screen.ids["menu_name"]
        menu_time = home_screen.ids["menu_time"]
        menu_count = home_screen.ids["menu_count"]
        menu_money = home_screen.ids["menu_money"]
        menu_capital = home_screen.ids["menu_capital"]
        apple_cost = home_screen.ids["apple_cost"]
        google_cost = home_screen.ids["google_cost"]
        facebook_cost = home_screen.ids["facebook_cost"]
        microsoft_cost = home_screen.ids["microsoft_cost"]
        yandex_cost = home_screen.ids["yandex_cost"]
        bitcoin_cost = home_screen.ids["bitcoin_cost"]
        kol_vo1 = home_screen.ids["kol_vo1"]
        kol_vo2 = home_screen.ids["kol_vo2"]
        kol_vo3 = home_screen.ids["kol_vo3"]
        kol_vo4 = home_screen.ids["kol_vo4"]
        kol_vo5 = home_screen.ids["kol_vo5"]
        kol_vo6 = home_screen.ids["kol_vo6"]
        raznica1 = home_screen.ids["raznica1"]
        raznica2 = home_screen.ids["raznica2"]
        raznica3 = home_screen.ids["raznica3"]
        raznica4 = home_screen.ids["raznica4"]
        raznica5 = home_screen.ids["raznica5"]
        raznica6 = home_screen.ids["raznica6"]

        if file == 1:
            json = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file1.json')
        elif file == 2:
            json = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file2.json')
        elif file == 3:
            json = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file3.json')

        json.put('menu_name', name=menu_name.text)
        json.put('menu_time', name=menu_time.text)
        json.put('menu_count', name=menu_count.text)
        json.put('menu_money', name=menu_money.text)
        json.put('menu_capital', name=menu_capital.text)
        json.put('apple_cost', name=apple_cost.text)
        json.put('google_cost', name=google_cost.text)
        json.put('facebook_cost', name=facebook_cost.text)
        json.put('microsoft_cost', name=microsoft_cost.text)
        json.put('yandex_cost', name=yandex_cost.text)
        json.put('bitcoin_cost', name=bitcoin_cost.text)
        json.put('kol_vo1', name=kol_vo1.text)
        json.put('kol_vo2', name=kol_vo2.text)
        json.put('kol_vo3', name=kol_vo3.text)
        json.put('kol_vo4', name=kol_vo4.text)
        json.put('kol_vo5', name=kol_vo5.text)
        json.put('kol_vo6', name=kol_vo6.text)
        json.put('raznica1', name=raznica1.text)
        json.put('raznica2', name=raznica2.text)
        json.put('raznica3', name=raznica3.text)
        json.put('raznica4', name=raznica4.text)
        json.put('raznica5', name=raznica5.text)
        json.put('raznica6', name=raznica6.text)

        if self.exit == False:
            self.change_screen("home_screen")
        else:
            self.change_screen("choose_screen")
            self.exit = False
    def show_save(self):
        save_screen = self.root.ids["save_screen"]
        label1 = save_screen.ids["label1"]
        label2 = save_screen.ids["label2"]
        label3 = save_screen.ids["label3"]

        file1 = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file1.json')
        file2 = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file2.json')
        file3 = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file3.json')

        try:
            if file1.exists('menu_name'):
                label_1 = "Имя: " + file1.get('menu_name')['name'] + ", Капитал: " + file1.get('menu_capital')['name']
                label1.text = label_1
            if file2.exists('menu_name'):
                label_2 = "Имя: " + file2.get('menu_name')['name'] + ", Капитал: " + file2.get('menu_capital')['name']
                label2.text = label_2
            if file3.exists('menu_name'):
                label_3 = "Имя: " + file3.get('menu_name')['name'] + ", Капитал: " + file3.get('menu_capital')['name']
                label3.text = label_3
        except FileNotFoundError:
            pass
    def show_load(self):
        load_screen = self.root.ids["load_screen"]
        label1 = load_screen.ids["label1"]
        label2 = load_screen.ids["label2"]
        label3 = load_screen.ids["label3"]

        file1 = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file1.json')
        file2 = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file2.json')
        file3 = JsonStore('/storage/emulated/0/Android/data/com.akcioner/file3.json')

        try:
            if file1.exists('menu_name'):
                label_1 = "Имя: " + file1.get('menu_name')['name'] + ", Капитал: " + file1.get('menu_capital')['name']
                label1.text = label_1
            if file2.exists('menu_name'):
                label_2 = "Имя: " + file2.get('menu_name')['name'] + ", Капитал: " + file2.get('menu_capital')['name']
                label2.text = label_2
            if file3.exists('menu_name'):
                label_3 = "Имя: " + file3.get('menu_name')['name'] + ", Капитал: " + file3.get('menu_capital')['name']
                label3.text = label_3
        except FileNotFoundError:
            pass

MainApp().run()
