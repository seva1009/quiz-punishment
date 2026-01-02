#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUIZ CASTIGO - Versión Móvil
se castigo con tiempo por cada error 
Autor: [seva 1009]
Versión: 1.0
"""

import os
import sys
import time
import random
from datetime import datetime

# ========== CONFIGURACIÓN ==========
APP_NAME = "Quiz Castigo 📱"
VERSION = "1.0"
AUTOR = "TuNombre"
CASTIGO_BASE = 60  # 60 segundos = 1 minuto (cambia a 300 para 5 min)

# ========== CLASE PRINCIPAL ==========
class QuizCastigoApp:
    def __init__(self):
        self.puntos = 0
        self.errores_consecutivos = 0
        self.historial = []
        self.usuario = ""
        
        # Base de datos de preguntas (FÁCIL DE MODIFICAR)
        self.preguntas = self.cargar_preguntas()
    
    def cargar_preguntas(self):
        """Carga todas las preguntas del quiz"""
        return [
            # MATEMÁTICAS
            {
                "id": 1,
                "categoria": "Matemáticas",
                "dificultad": "Fácil",
                "texto": "¿Cuánto es 15 + 27?",
                "opciones": {"A": "40", "B": "42", "C": "45", "D": "50"},
                "correcta": "B",
                "explicacion": "15 + 27 = 42"
            },
            {
                "id": 2,
                "categoria": "Matemáticas",
                "dificultad": "Media",
                "texto": "¿Cuánto es 8 × 7?",
                "opciones": {"A": "54", "B": "56", "C": "58", "D": "60"},
                "correcta": "B",
                "explicacion": "8 × 7 = 56 (tabla del 8)"
            },
            {
                "id": 3,
                "categoria": "Matemáticas",
                "dificultad": "Difícil",
                "texto": "¿Raíz cuadrada de 144?",
                "opciones": {"A": "10", "B": "11", "C": "12", "D": "13"},
                "correcta": "C",
                "explicacion": "12 × 12 = 144"
            },
            
            # CULTURA GENERAL
            {
                "id": 4,
                "categoria": "Cultura General",
                "dificultad": "Fácil",
                "texto": "¿Capital de Francia?",
                "opciones": {"A": "Londres", "B": "Berlín", "C": "París", "D": "Madrid"},
                "correcta": "C",
                "explicacion": "París es la capital de Francia"
            },
            {
                "id": 5,
                "categoria": "Cultura General",
                "dificultad": "Media",
                "texto": "¿Planeta más grande del sistema solar?",
                "opciones": {"A": "Tierra", "B": "Marte", "C": "Júpiter", "D": "Saturno"},
                "correcta": "C",
                "explicacion": "Júpiter es el planeta más grande"
            },
            {
                "id": 6,
                "categoria": "Cultura General",
                "dificultad": "Difícil",
                "texto": "¿Año en que llegó el hombre a la Luna?",
                "opciones": {"A": "1965", "B": "1969", "C": "1972", "D": "1975"},
                "correcta": "B",
                "explicacion": "Apolo 11 llegó a la Luna en 1969"
            },
            
            # CIENCIA
            {
                "id": 7,
                "categoria": "Ciencia",
                "dificultad": "Fácil",
                "texto": "¿H2O es la fórmula del...?",
                "opciones": {"A": "Oxígeno", "B": "Dióxido de carbono", "C": "Agua", "D": "Sal"},
                "correcta": "C",
                "explicacion": "H2O es la fórmula química del agua"
            },
            {
                "id": 8,
                "categoria": "Ciencia",
                "dificultad": "Media",
                "texto": "¿Órgano principal del sistema circulatorio?",
                "opciones": {"A": "Pulmón", "B": "Hígado", "C": "Corazón", "D": "Riñón"},
                "correcta": "C",
                "explicacion": "El corazón bombea la sangre"
            },
            
            # HISTORIA
            {
                "id": 9,
                "categoria": "Historia",
                "dificultad": "Media",
                "texto": "¿Quién pintó la Mona Lisa?",
                "opciones": {"A": "Miguel Ángel", "B": "Leonardo da Vinci", "C": "Picasso", "D": "Van Gogh"},
                "correcta": "B",
                "explicacion": "Leonardo da Vinci pintó la Mona Lisa"
            },
            
            # GEOGRAFÍA
            {
                "id": 10,
                "categoria": "Geografía",
                "dificultad": "Media",
                "texto": "¿Río más largo del mundo?",
                "opciones": {"A": "Amazonas", "B": "Nilo", "C": "Misisipi", "D": "Yangtsé"},
                "correcta": "A",
                "explicacion": "El río Amazonas es el más largo"
            }
        ]
    
    def limpiar_pantalla(self):
        """Limpia la pantalla (compatible con Termux y PC)"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_banner(self):
        """Muestra el banner principal"""
        self.limpiar_pantalla()
        print("\033[1;36m" + "═" * 52 + "\033[0m")
        print("\033[1;35m           🧠 QUIZ CASTIGO 📱           \033[0m")
        print("\033[1;36m" + "═" * 52 + "\033[0m")
        print("    Cada error = Bloqueo temporal")
        print("    Versión: {} | Autor: {}".format(VERSION, AUTOR))
        print("\033[1;36m" + "═" * 52 + "\033[0m")
    
    def mostrar_progreso(self, actual, total):
        """Muestra barra de progreso"""
        porcentaje = (actual / total) * 100
        barras = int(porcentaje / 2)  # 50 caracteres máximo
        espacios = 50 - barras
        
        print(f"\n📊 Progreso: [\033[1;32m{'█' * barras}\033[0m{'░' * espacios}] {porcentaje:.1f}%")
        print(f"   Pregunta {actual} de {total}")
        print(f"   🏆 Puntos: {self.puntos} | ❌ Errores seguidos: {self.errores_consecutivos}")
        print("─" * 52)
    
    def calcular_castigo(self):
        """Calcula tiempo de castigo (progresivo)"""
        base = CASTIGO_BASE
        extra = self.errores_consecutivos * 30  # 30 segundos extra por error seguido
        return min(base + extra, 300)  # Máximo 5 minutos
    
    def mostrar_pregunta(self, numero, pregunta):
        """Muestra una pregunta con formato"""
        self.mostrar_banner()
        self.mostrar_progreso(numero, len(self.preguntas))
        
        print(f"\n\033[1;33m[{pregunta['categoria']}] - Dificultad: {pregunta['dificultad']}\033[0m")
        print(f"\n\033[1;37m{pregunta['texto']}\033[0m")
        print("\n" + "─" * 52)
        
        for letra, texto in pregunta['opciones'].items():
            print(f"  \033[1;32m{letra})\033[0m {texto}")
        
        print("─" * 52)
    
    def obtener_respuesta(self):
        """Obtiene y valida respuesta del usuario"""
        while True:
            try:
                respuesta = input("\nTu respuesta (A/B/C/D) o 'S' para salir: ").upper().strip()
                
                if respuesta == 'S':
                    return None  # Señal para salir
                
                if respuesta in ['A', 'B', 'C', 'D']:
                    return respuesta
                
                print("\033[1;31m❌ Error: Solo A, B, C o D\033[0m")
                
            except KeyboardInterrupt:
                print("\n\n👋 Saliendo del quiz...")
                return None
    
    def ejecutar_bloqueo(self, segundos):
        """Ejecuta la pantalla de bloqueo"""
        self.mostrar_banner()
        
        print("\n\033[1;31m" + "╔" + "═" * 48 + "╗" + "\033[0m")
        print("\033[1;31m" + "║" + " " * 10 + "🚫 APLICACIÓN BLOQUEADA" + " " * 10 + "║" + "\033[0m")
        print("\033[1;31m" + "╚" + "═" * 48 + "╝" + "\033[0m")
        
        print(f"\n📛 Razón: Error en pregunta del quiz")
        
        minutos = segundos // 60
        segs = segundos % 60
        if minutos > 0:
            print(f"⏰ Tiempo de bloqueo: {minutos} minuto{'s' if minutos > 1 else ''} {segs} segundo{'s' if segs != 1 else ''}")
        else:
            print(f"⏰ Tiempo de bloqueo: {segundos} segundo{'s' if segundos > 1 else ''}")
        
        print("\n💡 Usa este tiempo para pensar en la respuesta correcta.")
        print("   ¡La próxima vez lo harás mejor!")
        print("\n" + "─" * 50)
        
        # Contador regresivo
        for i in range(segundos, 0, -1):
            minutos = i // 60
            segs = i % 60
            tiempo_formateado = f"{minutos:02d}:{segs:02d}"
            print(f"\r⏳ Tiempo restante: \033[1;33m{tiempo_formateado}\033[0m", end='', flush=True)
            time.sleep(1)
        
        print("\n\n\033[1;32m✅ ¡DESBLOQUEADO! Continuando...\033[0m")
        time.sleep(2)
    
    def registrar_intento(self, pregunta, respuesta, correcta):
        """Registra el intento en historial"""
        self.historial.append({
            'pregunta': pregunta['texto'],
            'respuesta': respuesta,
            'correcta': correcta,
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'puntos': self.puntos
        })
    
    def ejecutar_quiz(self):
        """Ejecuta el quiz completo"""
        # Presentación
        self.mostrar_banner()
        
        if not self.usuario:
            self.usuario = input("👤 ¿Cómo te llamas? ").strip()
            if not self.usuario:
                self.usuario = "Jugador"
        
        print(f"\n¡Hola {self.usuario}! Bienvenido a Quiz Castigo.")
        print("\n🎮 REGLAS DEL JUEGO:")
        print("• Responde preguntas con A, B, C, D")
        print(f"• Cada error = Bloqueo de {CASTIGO_BASE//60} minuto{'s' if CASTIGO_BASE//60 > 1 else ''}")
        print("• Errores consecutivos aumentan el castigo")
        print("• Cada acierto = +10 puntos")
        print("• Escribe 'S' para salir en cualquier momento")
        
        input("\nPresiona Enter para comenzar...")
        
        # Mezclar preguntas
        preguntas_mezcladas = self.preguntas.copy()
        random.shuffle(preguntas_mezcladas)
        
        # Ejecutar preguntas
        for i, pregunta in enumerate(preguntas_mezcladas, 1):
            self.mostrar_pregunta(i, pregunta)
            respuesta = self.obtener_respuesta()
            
            if respuesta is None:  # Usuario quiere salir
                print(f"\n👋 ¡Hasta luego {self.usuario}!")
                return
            
            es_correcta = respuesta == pregunta['correcta']
            self.registrar_intento(pregunta, respuesta, es_correcta)
            
            if es_correcta:
                self.puntos += 10
                self.errores_consecutivos = 0
                print(f"\n\033[1;32m✅ ¡CORRECTO! +10 puntos\033[0m")
                print(f"💡 {pregunta['explicacion']}")
                print(f"🏆 Puntos totales: \033[1;33m{self.puntos}\033[0m")
            else:
                self.errores_consecutivos += 1
                respuesta_correcta = pregunta['opciones'][pregunta['correcta']]
                print(f"\n\033[1;31m❌ INCORRECTO!\033[0m")
                print(f"💡 La respuesta era: \033[1;32m{pregunta['correcta']}) {respuesta_correcta}\033[0m")
                print(f"💡 {pregunta['explicacion']}")
                
                # Calcular y aplicar castigo
                castigo = self.calcular_castigo()
                minutos = castigo // 60
                segundos = castigo % 60
                
                if minutos > 0:
                    print(f"\n⏳ Castigo: {minutos} min {segundos} seg")
                else:
                    print(f"\n⏳ Castigo: {segundos} seg")
                
                print(f"📛 Errores seguidos: {self.errores_consecutivos}")
                
                input("\nPresiona Enter para comenzar el bloqueo...")
                self.ejecutar_bloqueo(castigo)
            
            # Pausa entre preguntas (excepto última)
            if i < len(preguntas_mezcladas):
                input("\nPresiona Enter para la siguiente pregunta...")
        
        # Mostrar resultados finales
        self.mostrar_resultados()
    
    def mostrar_resultados(self):
        """Muestra resultados finales"""
        self.mostrar_banner()
        
        print("\n" + "═" * 52)
        print("           🎉 RESULTADOS FINALES 🎉")
        print("═" * 52)
        
        max_puntos = len(self.preguntas) * 10
        porcentaje = (self.puntos / max_puntos) * 100
        
        print(f"\n👤 Jugador: {self.usuario}")
        print(f"📊 Preguntas totales: {len(self.preguntas)}")
        print(f"🏆 Puntos obtenidos: {self.puntos}/{max_puntos}")
        print(f"📈 Porcentaje: {porcentaje:.1f}%")
        
        errores = len([h for h in self.historial if not h['correcta']])
        print(f"❌ Errores cometidos: {errores}")
        
        if self.historial:
            tiempo_total = len(self.historial) * 30  # Estimado
            print(f"⏱️  Tiempo estimado de juego: {tiempo_total//60} min")
        
        print("\n" + "═" * 52)
        print("\n🏅 CLASIFICACIÓN:")
        
        if porcentaje == 100:
            print("🌟 ¡PERFECTO! Nivel: Genio Total")
            print("   No mereces castigos, ¡eres increíble!")
        elif porcentaje >= 90:
            print("⭐ ¡EXCELENTE! Nivel: Maestro")
            print("   Casi perfecto, muy bien hecho.")
        elif porcentaje >= 70:
            print("👍 ¡MUY BIEN! Nivel: Avanzado")
            print("   Buen trabajo, sigue así.")
        elif porcentaje >= 50:
            print("💪 ¡BIEN! Nivel: Intermedio")
            print("   Vas por buen camino, practica más.")
        elif porcentaje >= 30:
            print("📚 ¡REGULAR! Nivel: Principiante")
            print("   Necesitas estudiar más.")
        else:
            print("🎯 ¡A PRACTICAR! Nivel: Novato")
            print("   No te rindas, la práctica hace al maestro.")
        
        print("\n" + "═" * 52)
        
        # Preguntar si quiere jugar de nuevo
        opcion = input("\n¿Jugar de nuevo? (S/N): ").upper()
        if opcion == 'S':
            self.reiniciar_juego()
            self.ejecutar_quiz()
        else:
            print(f"\n👋 ¡Gracias por jugar, {self.usuario}!")
            print("📱 Para jugar otra vez: python app_movil.py")
    
    def reiniciar_juego(self):
        """Reinicia el juego"""
        self.puntos = 0
        self.errores_consecutivos = 0
        self.historial = []
        # No reiniciamos el nombre del usuario

# ========== FUNCIONES AUXILIARES ==========
def verificar_entorno():
    """Verifica si está en Termux o PC"""
    es_termux = 'com.termux' in sys.executable if hasattr(sys, 'executable') else False
    
    print("\n" + "═" * 52)
    if es_termux:
        print("✅ Entorno detectado: Termux (Android)")
    else:
        print("💻 Entorno detectado: PC/Simulación")
        print("💡 Para Android, instala Termux desde Play Store")
    print("═" * 52 + "\n")
    
    return es_termux

def main():
    """Función principal"""
    try:
        app = QuizCastigoApp()
        verificar_entorno()
        app.ejecutar_quiz()
        
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("🔧 Por favor, reporta este error.")
        input("\nPresiona Enter para salir...")

# ========== EJECUCIÓN ==========
if __name__ == "__main__":
    main()