class Pycharm:
    def open(self):
        print("open methord in pycharm")
    def run(self):
        print("run folty in pycharm")
    def debug(self):
        print("debugging using pycharm")
class vscode:
    def open(self):
        print("open method in vscode")
    def run(self):
            print("run folty in vscode")
    def debug(self):
            print("debugging using vscode")
class Programmer:
    def coading(self,ide):
        ide.open()
        ide.run()
        ide.debug()
py=Pycharm()
vs=vscode()
pg=Programmer()
#pg.coading(py)
pg.coading(vs)
