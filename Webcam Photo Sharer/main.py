from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from filesharer import FileSharer

import time
import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """Starts camera and changes Button text"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"

    def stop(self):
        """Stops camera and changes Button text"""
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current time and captures and saves
        a photo image under that filename"""

        # Create unique names for captured picture using time lib
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.file_path = f"files/{current_time}.png"
        # Export files
        self.ids.camera.export_to_png(self.file_path)
        # Access to ImageScreen after pushing capture button.
        self.manager.current = 'image_screen'
        # Show captured picture in ImageScreen
        self.manager.current_screen.ids.img.source = self.file_path


class ImageScreen(Screen):
    # error generates on create_link() and open_link() methods
    link_message = "Create a Link First"

    def create_link(self):
        """Accesses photo filepath, uploads it to the web,
        and insert the link in the label widget"""

        file_path = App.get_running_app().root.ids.camera_screen.file_path
        fileshare = FileSharer(filepath=file_path)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """Copy link to clipboard available for posting"""

        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Opens the link in the default browser"""

        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
