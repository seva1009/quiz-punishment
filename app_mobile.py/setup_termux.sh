#!/data/data/com.termux/files/usr/bin/bash
# =============================================
# AUTOMATIC INSTALLER - QUIZ PUNISHMENT
# Version: 1.0
# =============================================

# Configuration
APP_NAME="Quiz Punishment"
VERSION="1.0"
REPO_URL="https://github.com/YOUR_USERNAME/quiz-punishment.git"
INSTALL_DIR="$HOME/quiz-punishment"

# Colors
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
NC='\033[0m'

# Functions
show_msg() { echo -e "${GREEN}[✓]${NC} $1"; }
show_error() { echo -e "${RED}[✗]${NC} $1"; }
show_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
show_info() { echo -e "${CYAN}[i]${NC} $1"; }

# Banner
clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════╗"
echo "║            $APP_NAME - $VERSION                ║"
echo "║          Automatic Termux Installer            ║"
echo "╚════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Check Termux
if [ ! -d "/data/data/com.termux" ]; then
    show_error "This script only works in Termux (Android)"
    echo "Please install Termux from Google Play Store"
    exit 1
fi

# Update packages
show_msg "Updating Termux packages..."
pkg update -y && pkg upgrade -y
show_msg "System updated"

# Install dependencies
show_msg "Installing Python and Git..."
pkg install -y python git
show_msg "Dependencies installed"

# Clone repository
show_msg "Downloading Quiz Punishment..."
if [ -d "$INSTALL_DIR" ]; then
    show_warning "App already installed, updating..."
    cd "$INSTALL_DIR"
    git pull
else
    git clone "$REPO_URL" "$INSTALL_DIR"
fi
show_msg "App downloaded"

# Set permissions
cd "$INSTALL_DIR"
chmod +x app_mobile.py setup_termux.sh
show_msg "Permissions configured"

# Create shortcut
show_msg "Creating shortcut 'quiz'..."
cat > $PREFIX/bin/quiz << EOF
#!/data/data/com.termux/files/usr/bin/bash
cd \$HOME/quiz-punishment
python app_mobile.py
EOF
chmod +x $PREFIX/bin/quiz
show_msg "Shortcut created"

# Finalize
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║        INSTALLATION COMPLETED ✅              ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}🎮 TO PLAY:${NC}"
echo "   Run: ${GREEN}quiz${NC}"
echo "   Or: ${GREEN}cd ~/quiz-punishment && python app_mobile.py${NC}"
echo ""
echo -e "${CYAN}🔧 USEFUL COMMANDS:${NC}"
echo "   Update: ${YELLOW}cd ~/quiz-punishment && git pull${NC}"
echo "   Uninstall: ${YELLOW}rm -rf ~/quiz-punishment${NC}"
echo ""
echo -e "${GREEN}👋 Enjoy Quiz Punishment!${NC}"