import uisconv
import frontend_light

uiswin=frontend_light.MainApp()

m2u = uisconv.UisConv()
print(m2u.configfile)
m2u.read_cfg("D:/PycharmProjects/magento2uis/uis.conf")
#m2u.import_csv()
#m2u.export_uis()
#m2u.update_cfg()

uiswin.window.mainloop()