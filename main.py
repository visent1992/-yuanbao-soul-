# main.py - 最小测试版，仅验证编译和安装
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# 设个背景色，方便确认启动成功
Window.clearcolor = (0.1, 0.1, 0.15, 1)

class YuanSoulApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        label = Label(
            text="元宝 Soul\n编译成功！",
            font_size=28,
            color=(1, 1, 1, 1),
            halign='center'
        )
        btn = Button(
            text="点我测试",
            font_size=20,
            size_hint=(1, 0.3)
        )
        btn.bind(on_press=lambda x: setattr(label, 'text', "✅ 运行正常！"))
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    YuanSoulApp().run()
