# Extension to Folder mapping
FILE_CATEGORIES = {
    'PDFs': ['.pdf'],
    'Executáveis': ['.exe', '.msi', '.bat', '.sh','.dmg'],
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Vídeos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
    'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Documentos': ['.docx', '.doc', '.txt', '.odt','.md'],
    'Áudio': ['.mp3', '.wav', '.flac', '.ogg', '.m4a'],
    'Planilhas':['.xlsx', '.xls','.csv','.ods'],
    'Apresentações':['.pptx', '.ppt','odp'],
    'Códigos': ['.py', '.java', '.js', '.ts', '.html', '.css', '.cpp', '.c', '.cs', '.php'],
    'Configuração': ['.json', '.xml', '.yml', '.yaml', '.ini', '.env'],
    'Imagens de Disco': ['.iso', '.img'],
    'Segurança': ['.pem', '.key', '.crt', '.cer'],
    'Bibliotecas': ['.dll', '.so', '.dylib']
}

# Theme settings
APP_THEME = 'darkly'  # Available: cosmo, flatly, journal, lumen, paper, readable, sandstone, simplex, yeti, darkly, superhero, solar, cyborg, vapor
APP_TITLE = "Organizador Automático de Arquivos"
WINDOW_SIZE = (800, 600)

# Default behavior
DEFAULT_OTHER_FOLDER = "Outros"
RECURSIVE_SCAN = False  # Set to True to organize subfolders
LOG_FILE_NAME = "organizer.log"
