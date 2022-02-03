from log.Log import Log
from tkinter import *
from GUI.Win import Win
from tkinter import filedialog
from moviepy.editor import *
from tkinter.ttk import Combobox
from Editor.Editor import Editor


class StartWin(Win):
    def __init__(self):
        Win.__init__(self)
        self.name_files = ""
        self.name_files_list = list()
        self.clips = dict()
        self.label_select_files = Label(self.root, text=self.name_files, justify=LEFT)
        self.combox_select_file = Combobox(self.root,
                                           state="readonly",
                                           justify=CENTER)
        self.entry_sec_start = Entry(self.root)
        self.entry_sec_start.insert(0, "Start")
        self.entry_sec_end = Entry(self.root)
        self.entry_sec_end.insert(0, "End")
        self.entry_rotate = Entry(self.root)
        self.entry_rotate.insert(0, "Degree")
        self.entry_speed_up = Entry(self.root)
        self.entry_speed_up.insert(0, "Speed")
        self.entry_x1 = Entry(self.root)
        self.entry_x1.insert(0, "x1")
        self.entry_y1 = Entry(self.root)
        self.entry_y1.insert(0, "y1")
        self.entry_x2 = Entry(self.root)
        self.entry_x2.insert(0, "x2")
        self.entry_y2 = Entry(self.root)
        self.entry_y2.insert(0, "y2")
        self.button_add_file = Button(text="Выбрать файл", command=self.load_path)
        self.button_subclip_file = Button(text="Вырезать фрагмент, sec",
                                          command=self.subclip)
        self.button_rotate_file = Button(text="Повернуть видео",
                                         command=self.rotate)
        self.button_speed_up_file = Button(text="Ускорить видео",
                                           command=self.speed_up)
        self.button_concatenate_file = Button(text="Склеить все файлы",
                                              command=self.concatenate)
        self.button_crop_file = Button(text="Кроп",
                                       command=self.crop)
        # b2 = Button(text="Сохранить", command=extract_text)
        # b2.grid(row=1, column=1, sticky=W)

    def subclip(self):
        clip = Editor.subclip(self.entry_sec_start.get(), self.entry_sec_end.get(),
                              self.clips.get(self.combox_select_file.get()))
        clip.write_videofile("{0}_subclip.mp4"
                             .format(self.combox_select_file.get().split(".")[0]))
        Log.write(f'subclip-{self.combox_select_file.get()}-{self.entry_sec_start.get(), self.entry_sec_end.get()}')


    def rotate(self):
        clip = Editor.rotate(self.entry_rotate.get(),
                             self.clips.get(self.combox_select_file.get()))
        clip.write_videofile("{0}_rotate.mp4"
                             .format(self.combox_select_file.get().split(".")[0]))
        Log.write(f'rotate-{self.combox_select_file.get()}-{self.entry_rotate.get()}')

    def speed_up(self):
        clip = Editor.speed_up(self.entry_speed_up.get(),
                               self.clips.get(self.combox_select_file.get()))
        clip.write_videofile("{0}_speed_up.mp4"
                             .format(self.combox_select_file.get().split(".")[0]))
        Log.write(f'speed_up-{self.combox_select_file.get()}-{self.entry_speed_up.get()}')

    def concatenate(self):
        temp = list()
        for key in self.clips.keys():
            temp.append(self.clips.get(key))
        clip = Editor.concatenate(temp)
        clip.write_videofile("all_concatenate.mp4")
        Log.write(f'concatenate-all_concatenate.mp4')

    def crop(self):
        clip = Editor.crop(self.entry_x1.get(), self.entry_y1.get(),
                           self.entry_x2.get(), self.entry_y2.get(),
                           self.clips.get(self.combox_select_file.get()))
        clip.write_videofile("{0}_crop.mp4"
                             .format(self.combox_select_file.get().split(".")[0]))
        Log.write(f'crop-{self.combox_select_file.get()}-' +
                  f'{self.entry_x1.get(), self.entry_y1.get(), self.entry_x2.get(), self.entry_y2.get()}')

    def update_label(self):
        print("11212")
        self.label_select_files.config(text=self.name_files)

    def load_path(self):
        path_file = filedialog.askopenfilename(
            filetypes=(("MP4 files", "*.mp4"),)
        )
        name_file = path_file.split('/')[-1]
        print(name_file)
        self.name_files += f"{name_file}\n"
        self.clips[name_file] = VideoFileClip(path_file)
        self.name_files_list.append(name_file)
        self.update_label()
        self.add_combox()
        print(self.name_files)

    def add_combox(self):
        temp = list()
        for key in self.name_files_list:
            temp.append(key)
        self.combox_select_file.config(values=temp)

    def draw_widgets(self):
        # Путь к файлам
        Label(self.root, text="Укажите путь к видео", justify=LEFT).grid(row=0, column=0, padx=20, sticky=W)
        self.button_add_file.grid(row=0, column=1, padx=30, pady=10, sticky=E + W)

        Label(self.root, text="Загруженные файлы", justify=LEFT).grid(row=1, column=0, padx=20, sticky=W)
        self.label_select_files.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        Label(self.root, text="Выберете файл", justify=LEFT).grid(row=2, column=0, padx=20, sticky=W)
        self.combox_select_file.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        self.button_subclip_file.grid(row=3, column=0, rowspan=3, padx=20, sticky=W + N + S)
        self.entry_sec_start.grid(row=4, column=1, padx=20, sticky=W)
        self.entry_sec_end.grid(row=5, column=1, padx=20, sticky=W)

        self.button_rotate_file.grid(row=6, column=0, pady=10, padx=20, sticky=W)
        self.entry_rotate.grid(row=6, column=1, padx=20, sticky=W)

        self.button_speed_up_file.grid(row=7, column=0, pady=10, padx=20, sticky=W)
        self.entry_speed_up.grid(row=7, column=1, padx=20, sticky=W)

        self.button_crop_file.grid(row=8, column=0, rowspan=5, pady=10, padx=20, sticky=W + E)
        self.entry_x1.grid(row=9, column=1, pady=10, padx=20, sticky=W)
        self.entry_y1.grid(row=10, column=1, pady=10, padx=20, sticky=W)
        self.entry_x2.grid(row=11, column=1, pady=10, padx=20, sticky=W)
        self.entry_y2.grid(row=12, column=1, pady=10, padx=20, sticky=W)

        self.button_concatenate_file.grid(row=13, column=0, columnspan=2, pady=10, padx=20, sticky=W+E)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()
