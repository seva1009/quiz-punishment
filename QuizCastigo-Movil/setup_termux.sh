#!/data/data/com.termux/files/usr/bin/bash
# =============================================
# INSTALADOR AUTOMÁTICO - QUIZ CASTIGO
# Versión: 1.0
# =============================================

# Configuración
APP_NAME="Quiz Castigo"
VERSION="1.0"
REPO_URL="https://github.com/TU_USUARIO/quiz-castigo.git"
INSTALL_DIR="$HOME/quiz-castigo"

# Colores
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
NC='\033[0m'

# Funciones
show_msg() { echo -e "${GREEN}[✓]${NC} $1"; }
show_error() { echo -e "${RED}[✗]${NC} $1"; }
show_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
show_info() { echo -e "${CYAN}[i]${NC} $1"; }

# Banner
clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════╗"
echo "║            $APP_NAME - $VERSION                ║"
echo "║          Instalador Automático Termux          ║"
echo "╚════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Verificar Termux
if [ ! -d "/data/data/com.termux" ]; then
    show_error "Este script solo funciona en Termux (Android)"
    echo "Por favor, instala Termux desde Google Play Store"
    exit 1
fi

# Actualizar paquetes
show_msg "Actualizando paquetes de Termux..."
pkg update -y && pkg upgrade -y
show_msg "Sistema actualizado"

# Instalar dependencias
show_msg "Instalando Python y Git..."
pkg install -y python git
show_msg "Dependencias instaladas"

# Clonar repositorio
show_msg "Descargando Quiz Castigo..."
if [ -d "$INSTALL_DIR" ]; then
    show_warning "La app ya está instalada, actualizando..."
    cd "$INSTALL_DIR"
    git pull
else
    git clone "$REPO_URL" "$INSTALL_DIR"
fi
show_msg "App descargada"

# Configurar permisos
cd "$INSTALL_DIR"
chmod +x app_movil.py setup_termux.sh
show_msg "Permisos configurados"

# Crear acceso directo
show_msg "Creando acceso directo 'quiz'..."
cat > $PREFIX/bin/quiz << EOF
#!/data/data/com.termux/files/usr/bin/bash
cd \$HOME/quiz-castigo
python app_movil.py
EOF
chmod +x $PREFIX/bin/quiz
show_msg "Acceso directo creado"

# Finalizar
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║        INSTALACIÓN COMPLETADA ✅              ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}🎮 PARA JUGAR:${NC}"
echo "   Ejecuta: ${GREEN}quiz${NC}"
echo "   O: ${GREEN}cd ~/quiz-castigo && python app_movil.py${NC}"
echo ""
echo -e "${CYAN}🔧 COMANDOS ÚTILES:${NC}"
echo "   Actualizar: ${YELLOW}cd ~/quiz-castigo && git pull${NC}"
echo "   Desinstalar: ${YELLOW}rm -rf ~/quiz-castigo${NC}"
echo ""
echo -e "${GREEN}👋 ¡Disfruta de Quiz Castigo!${NC}"