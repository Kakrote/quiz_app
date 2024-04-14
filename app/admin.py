
from .lib.struct import ADMIN
from .lib.sockets import ClientSocket, ServerSocket, EventEmitter
from .ui.admin.main import App
from .settings import addr

class Admin(ADMIN):

    def __init__(self, ) -> None:
        super().__init__()
        self.ui=App()
        self.server = ServerSocket(addr=addr)
    
    def start(self):
        self.server.start()
        self.ui.show()


def main():
    admin = Admin()
    admin.start()
    pass

if __name__=="__main__":
    main()