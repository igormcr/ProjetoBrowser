import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Configurar variáveis de ambiente para ignorar erros de certificado
os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--ignore-certificate-errors --ignore-ssl-errors --allow-running-insecure-content'

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Configuração da janela
        self.setWindowTitle('Browser TsaOne')
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget do navegador
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        
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
        
        # Botão para forçar HTTPS
        https_btn = QPushButton('🔒')
        https_btn.setToolTip('Forçar HTTPS')
        https_btn.clicked.connect(self.force_https)
        
        # Layout da barra de navegação
        navbar = QHBoxLayout()
        navbar.addWidget(back_btn)
        navbar.addWidget(forward_btn)
        navbar.addWidget(reload_btn)
        navbar.addWidget(home_btn)
        navbar.addWidget(https_btn)
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
        url = self.url_bar.text().strip()
        
        # Se não tiver protocolo, adicionar https://
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        # Se tiver http://, converter para https://
        elif url.startswith('http://'):
            url = url.replace('http://', 'https://', 1)
        
        self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
    
    def force_https(self):
        """Força a conversão da URL atual para HTTPS"""
        current_url = self.url_bar.text()
        if current_url:
            self.navigate_to_url()
    
    def navigate_home(self):
        home_url = 'https://www.google.com'
        self.url_bar.setText(home_url)
        self.browser.setUrl(QUrl(home_url))
    
    def update_url(self, q):
        """Atualiza a barra de URL quando a página muda"""
        url_string = q.toString()
        
        # Sempre mostrar como HTTPS se for HTTP
        if url_string.startswith('http://'):
            url_string = url_string.replace('http://', 'https://', 1)
        
        self.url_bar.setText(url_string)

if __name__ == '__main__':
    # Configurar atributos para High DPI
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())