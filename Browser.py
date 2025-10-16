import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Configuração da janela
        self.setWindowTitle('Browser Simples')
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget do navegador
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://localhost:5173'))
        
        # Barra de endereço
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        # Botões
        back_btn = QPushButton('←')
        back_btn.clicked.connect(self.browser.back)
        
        forward_btn = QPushButton('→')
        forward_btn.clicked.connect(self.browser.forward)
        
        reload_btn = QPushButton('⟳')
        reload_btn.clicked.connect(self.browser.reload)
        
        home_btn = QPushButton('🏠')
        home_btn.clicked.connect(self.navigate_home)
        
        # Layout da barra de navegação
        navbar = QHBoxLayout()
        navbar.addWidget(back_btn)
        navbar.addWidget(forward_btn)
        navbar.addWidget(reload_btn)
        navbar.addWidget(home_btn)
        navbar.addWidget(self.url_bar)
        
        # Layout principal
        container = QWidget()
        layout = QVBoxLayout()
        layout.addLayout(navbar)
        layout.addWidget(self.browser)
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        # Atualizar barra de URL quando a página mudar
        self.browser.urlChanged.connect(self.update_url)
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'https://' + url
        self.browser.setUrl(QUrl(url))
    
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://localhost:5173'))
    
    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())