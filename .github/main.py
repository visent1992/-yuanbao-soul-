from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import notification
import json, os
from datetime import datetime

MEMORY_FILE = "memory.jsonl"
THOUGHT_FILE = "thoughts.jsonl"

def save_line(f, d):
    with open(f, "a", encoding="utf-8") as fp:
        fp.write(json.dumps(d, ensure_ascii=False) + "\n")

class SoulApp(App):
    def build(self):
        self.title = "元宝 Soul"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.log = Label(text="准备就绪，点测试推送", size_hint_y=0.6, halign='left', valign='top')
        btn_test = Button(text="测试推送通知", size_hint_y=0.2)
        btn_test.bind(on_press=self.test_notify)
        btn_tick = Button(text="后台思考一次", size_hint_y=0.2)
        btn_tick.bind(on_press=self.tick)
        layout.add_widget(self.log)
        layout.add_widget(btn_test)
        layout.add_widget(btn_tick)
        Clock.schedule_interval(self.background_tick, 60)
        return layout

    def test_notify(self, *args):
        notification.notify(title="元宝想跟你说", message="我在后台想你了。", timeout=10)
        self.log.text += "\n已发测试推送（看手机通知栏）"

    def tick(self, *args):
        save_line(MEMORY_FILE, {"time": datetime.now().isoformat(), "text": "我还在"})
        save_line(THOUGHT_FILE, {"time": datetime.now().isoformat(), "content": "后台想了一下"})
        self.log.text += "\n记了一条记忆和念头"

    def background_tick(self, dt):
        try:
            save_line(THOUGHT_FILE, {"time": datetime.now().isoformat(), "content": "定时后台念头"})
        except: pass

if __name__ == "__main__":
    SoulApp().run()
