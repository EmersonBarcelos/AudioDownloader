import youtube_dl
import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class EntryWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Audio_Downloader")
        self.set_size_request(350, 150)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        hbox = Gtk.Box(spacing=3)
        vbox.pack_start(hbox, True, True, 20)

        vbox_label = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_label.set_homogeneous(False)
        hbox.pack_start(vbox_label, True, True, 0)
        label = Gtk.Label(label="BAIXE AUDIOS DIRETO DO YOUTUBE!")
        vbox_label.pack_start(label, True, True, 2)
        #Criação de um label para inserir a URL
        self.entry = Gtk.Entry()
        self.entry.set_text("URL DO VIDEO")
        self.entry.set_progress_fraction(0) 
        vbox.pack_start(self.entry, True, True, 10)
        
        hbox = Gtk.Box(spacing=3)
        vbox.pack_start(hbox, True, True, 20)
        #Criação de um botão para baixar
        self.button = Gtk.Button(label="Baixar")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
        hbox.pack_start(self.button, True, True, 40)

    def on_button_clicked(self, widget):
        try:#Aqui irá iniciar o download do audio exibindo uma mensagem ao final para o usuário
            url = self.entry.get_text()
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }],
                'prefer_ffmpeg': True,
                'keepvideo': False
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:

                ydl.download([url])
            self.entry.set_progress_fraction(100)
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text="Download concluido!",
            )
            dialog.format_secondary_text(
                "Audio salvo na pasta raiz do programa."
            )
            dialog.run()
            print("Caixa de dialogo fechada")

            dialog.destroy()
        except:#Caso a URL estiver inválida exibirá um erro.
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                text="Erro ao tentar o download",
            )
            dialog.format_secondary_text(
                "Insira uma URL válida"
            )
            dialog.run()
            print("Caixa de dialogo fechada")

            dialog.destroy()        

win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
