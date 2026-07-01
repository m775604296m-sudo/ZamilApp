from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window

# استيراد الشاشات
from splash_screen import SplashScreen
from home_screen import HomeScreen, FullPlayerScreen

# تعيين حجم النافذة للتجربة على الكمبيوتر
Window.size = (360, 640)


class ZamilApp(MDApp):
    def build(self):
        # 1. إعدادات المظهر والثيم الأساسية
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        # 2. تسجيل وتخصيص الخطوط العربية للـ العناوين والنصوص فقط دون التأثير على الأيقونات
        self.theme_cls.font_styles["H1"] = ["ArabicFont", 96, False, -1.5]
        self.theme_cls.font_styles["H2"] = ["ArabicFont", 60, False, -0.5]
        self.theme_cls.font_styles["H3"] = ["ArabicFont", 48, False, 0]
        self.theme_cls.font_styles["H4"] = ["ArabicFont", 34, False, 0.25]
        self.theme_cls.font_styles["H5"] = ["ArabicFont", 24, False, 0]
        self.theme_cls.font_styles["H6"] = ["ArabicFont", 20, False, 0.15]
        self.theme_cls.font_styles["Subtitle1"] = ["ArabicFont", 16, False, 0.15]
        self.theme_cls.font_styles["Subtitle2"] = ["ArabicFont", 14, False, 0.1]
        self.theme_cls.font_styles["Body1"] = ["ArabicFont", 16, False, 0.5]
        self.theme_cls.font_styles["Body2"] = ["ArabicFont", 14, False, 0.25]
        self.theme_cls.font_styles["Button"] = ["ArabicFont", 14, True, 1.25]
        self.theme_cls.font_styles["Caption"] = ["ArabicFont", 12, False, 0.4]

        # 3. إنشاء مدير الشاشات
        self.sm = ScreenManager()

        # 4. إضافة الشاشات بترتيبها
        self.sm.add_widget(SplashScreen(name="splash"))

        self.home_screen = HomeScreen(name="home")
        self.sm.add_widget(self.home_screen)

        self.player_screen = FullPlayerScreen(home_ref=self.home_screen, name="player")
        self.sm.add_widget(self.player_screen)

        # 5. الانتقال التلقائي بعد 7 ثوانٍ
        Clock.schedule_once(self.switch_to_home, 7)

        return self.sm

    def switch_to_home(self, dt):
        if self.sm.current == "splash":
            self.sm.transition.direction = "left"
            self.sm.current = "home"


if __name__ == "__main__":
    # تسجيل الخط العربي خارج الـ App لضمان استقراره
    LabelBase.register(name="ArabicFont", fn_regular="assets/font/arial.ttf")

    # تشغيل التطبيق
    ZamilApp().run()