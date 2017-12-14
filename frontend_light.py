import tkinter as tk
import tkinter.scrolledtext
from tkinter import StringVar,filedialog
import datetime
import datepicker
import logging


class MainApp(tk.Frame):
    window = tk.Tk()
    logger = logging.getLogger(__name__)
    logger.addHandler(
        logging.StreamHandler())  ##要加這個setLevel才有用 https://stackoverflow.com/questions/22612913/python3-pycharm-debug-logging-levels-in-run-debug
    logger.setLevel(logging.INFO)
    def popcsvdialog(self,event):
        openfilename = tk.filedialog.askopenfilename(title="請選擇要匯入的CSV檔案",
                                                     filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        self.logger.info('CVS file selected:' + openfilename)
        event.widget.delete(0, "end")
        event.widget.insert(0, openfilename)

    def popinidialog(self,event):
        openfilename = tk.filedialog.askopenfilename(title="請選擇要使用的組態檔案",
                                                     filetypes=(("ini files", "*.conf"), ("all files", "*.*")))
        self.logger.info('INI file selected:' + openfilename)
        event.widget.delete(0, "end")
        event.widget.insert(0, openfilename)

    def popdirdialog(self,event):
        opendirname = tk.filedialog.askdirectory(title="請選擇要存放匯出檔案的目錄")
        self.logger.info('Export Directory selected:' + opendirname)
        event.widget.delete(0, "end")
        event.widget.insert(0, opendirname)

    def execonv():
        print("CONVERT")

    def __init__(self, *args, **kwargs):
        #tk.Frame.__init__(self, parent, *args, **kwargs)
        #self.parent = parent
        #windows = self.window
        window = self.window
        window.title('my window')
        window.geometry('600x550')
        window.columnconfigure([0, 1, 2, 3], minsize=100)
        window.rowconfigure([3, 4, 5, 6, 7, 8], minsize=30)
        window.columnconfigure(0, weight=0)
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=1)
        window.columnconfigure(4, weight=0)
        self.logger.info('start')

        tk.Label(window, text='Magento TO UIS 轉檔程式', anchor='w', font=('微軟中黑體', 16)).grid(row=0, column=0, columnspan=4)
        tk.Label(window, text='選擇預定到貨日', anchor='w').grid(row=3, column=0, sticky='W')
        tk.Label(window, text='選擇轉入的Magento檔案', anchor='w').grid(row=4, column=0, sticky='W')
        tk.Label(window, text='轉出檔案存放目錄', anchor='w').grid(row=5, column=0, sticky='W')
        tk.Label(window, text='組態檔', anchor='w').grid(row=8, column=0, sticky='W')

        # 選擇日期的欄位
        initdate = StringVar()
        initdate.set(datetime.datetime.now().strftime("%Y%m%d"))
        dp = datepicker.Datepicker(window, dateformat="%Y%m%d", datevar=initdate, entrywidth='100')
        dp.grid(row=3, column=1, sticky='w')

        # 選擇檔案的欄位
        fileedit = tk.Entry(window, width='200')
        fileedit.grid(row=4, column=1, sticky='W', columnspan=2)
        fileedit.bind('<Button-1>', self.popcsvdialog)

        # 選擇存放匯出檔案的地方
        diredit = tk.Entry(window, width='200')
        diredit.grid(row=5, column=1, sticky='W', columnspan=2)
        diredit.bind('<Button-1>', self.popdirdialog)

        # 取消按鈕
        cancelbtn = tk.Button(window, text='離開', command=window.destroy)
        cancelbtn.grid(row=6, column=1, sticky='E')

        # 確定轉換的按鈕
        convbtn = tk.Button(window, text="執行轉檔", command=self.execonv)
        convbtn.grid(row=6, column=2, sticky='E')

        # logwindow
        logtext = tk.scrolledtext.ScrolledText(window)
        logtext.config(state='disable')
        logtext.grid(row=7, column=0, columnspan=4)

        # 選擇檔案的欄位
        iniedit = tk.Entry(window, width='200')
        iniedit.grid(row=8, column=1, sticky='W', columnspan=2)
        iniedit.bind('<Button-1>', self.popinidialog)


