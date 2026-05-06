from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QGridLayout, QFrame, QLineEdit,
    QSizePolicy
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon, QPainter, QBrush

from config.settings import APP_NAME


class DesktopWindow(QWidget):
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.bg_pixmap = None

        self.setWindowTitle(APP_NAME)
        self.showMaximized()

        # Load wallpaper
        self.set_wallpaper("assets/wallpapers/default.jpg")

        self.init_ui()

    # =========================
    # WALLPAPER
    # =========================

    def set_wallpaper(self, path: str):
        """Load a wallpaper from the given path. Call this to change it dynamically."""
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            self.bg_pixmap = pixmap
        else:
            self.bg_pixmap = None
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        """Draw the wallpaper scaled to fill the entire window."""
        painter = QPainter(self)
        if self.bg_pixmap:
            scaled = self.bg_pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
            # Center the scaled image
            x = (self.width() - scaled.width()) // 2
            y = (self.height() - scaled.height()) // 2
            painter.drawPixmap(x, y, scaled)
        else:
            # Fallback: dark background
            painter.fillRect(self.rect(), QBrush(Qt.GlobalColor.black))
        painter.end()

    def resizeEvent(self, event):
        self.update()  # Redraw wallpaper on resize
        super().resizeEvent(event)

    # =========================
    # UI INIT
    # =========================

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 12, 20, 14)
        main_layout.setSpacing(0)

        # ── TOP BAR ──────────────────────────────────────────────────────────
        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(0, 0, 0, 10)

        title_icon = QLabel("🦙")
        title_icon.setStyleSheet("color: white; font-size: 18px;")
        title_text = QLabel("llamaOS")
        title_text.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")

        right_info = QLabel("☁ 9°C    00:00")
        right_info.setStyleSheet("color: white; font-size: 13px;")

        top_bar.addWidget(title_icon)
        top_bar.addSpacing(6)
        top_bar.addWidget(title_text)
        top_bar.addStretch()
        top_bar.addWidget(right_info)

        # ── CENTER AREA ───────────────────────────────────────────────────────
        center_layout = QHBoxLayout()
        center_layout.setContentsMargins(0, 10, 0, 10)

        # LEFT — Apps Grid
        apps_grid = QGridLayout()
        apps_grid.setSpacing(20)
        apps_grid.setContentsMargins(0, 0, 0, 0)

        apps = [
            ("Calculadora",       "assets/icons/calculator_icon.png",   self.on_open_calculator),
            ("Tareas",            "assets/icons/task_manager_icon.png",  self.on_open_tasks),
            ("Explorador\nde archivos", "assets/icons/file_explorer_icon.png", self.on_open_explorer),
            ("Cámara",            "assets/icons/camera_icon.png",        self.on_open_camera),
        ]

        row, col = 0, 0
        for name, path, callback in apps:
            widget = self.create_app_icon(name, path, callback)
            apps_grid.addWidget(widget, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1

        left_container = QWidget()
        left_container.setLayout(apps_grid)
        left_container.setStyleSheet("background: transparent;")
        left_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)

        # CENTER — Llama mascot
        # mascot_label = QLabel()
        # mascot_pixmap = QPixmap("assets/logo/llama_logo.png")
        # if not mascot_pixmap.isNull():
        #     mascot_label.setPixmap(
        #         mascot_pixmap.scaled(130, 130,
        #                              Qt.AspectRatioMode.KeepAspectRatio,
        #                              Qt.TransformationMode.SmoothTransformation)
        #     )
        # mascot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # mascot_label.setStyleSheet("background: transparent;")

        # RIGHT — Widgets panel
        right_widgets = QVBoxLayout()
        right_widgets.setSpacing(12)
        right_widgets.setContentsMargins(0, 0, 0, 0)

        right_widgets.addWidget(self.news_card())
        right_widgets.addWidget(self.weather_card())
        right_widgets.addWidget(self.search_card())
        right_widgets.addStretch()

        right_container = QWidget()
        right_container.setLayout(right_widgets)
        right_container.setStyleSheet("background: transparent;")
        right_container.setFixedWidth(220)

        # Compose center
        center_layout.addWidget(left_container)
        center_layout.addStretch()
        # center_layout.addWidget(mascot_label, 0, Qt.AlignmentFlag.AlignCenter)
        # center_layout.addStretch()
        center_layout.addWidget(right_container)

        # ── DOCK ─────────────────────────────────────────────────────────────
        dock_frame = QFrame()
        dock_layout = QHBoxLayout(dock_frame)
        dock_layout.setContentsMargins(20, 8, 20, 8)
        dock_layout.setSpacing(30)

        dock_items = [
            ("assets/logo/llama_logo.png",          "Inicio",         self.on_dock_home),
            ("assets/icons/web_icon.png",            "Navegador",      self.on_dock_browser),
            ("assets/icons/music_icon.png",          "Música",         self.on_dock_music),
            ("assets/icons/configuration_icon.png",  "Configuración",  self.on_dock_settings),
        ]

        for icon_path, tooltip, callback in dock_items:
            btn = QPushButton()
            icon = QIcon(icon_path)
            btn.setIcon(icon)
            btn.setIconSize(QSize(34, 34))
            btn.setToolTip(tooltip)
            btn.setFixedSize(54, 54)
            btn.clicked.connect(callback)
            btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    border-radius: 12px;
                    background: transparent;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.15);
                }
                QPushButton:pressed {
                    background-color: rgba(255, 255, 255, 0.08);
                }
            """)
            dock_layout.addWidget(btn)

        dock_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(20, 20, 20, 0.82);
                border-radius: 18px;
                border: 1px solid rgba(255,255,255,0.08);
            }
        """)

        dock_wrapper = QHBoxLayout()
        dock_wrapper.addStretch()
        dock_wrapper.addWidget(dock_frame)
        dock_wrapper.addStretch()

        # ── ASSEMBLE ─────────────────────────────────────────────────────────
        main_layout.addLayout(top_bar)
        main_layout.addLayout(center_layout, stretch=1)
        main_layout.addLayout(dock_wrapper)

        # Make sure all direct children have transparent backgrounds
        # so the painted wallpaper shows through
        self._make_transparent(self)

    # =========================
    # HELPER: TRANSPARENT BG
    # =========================

    def _make_transparent(self, widget):
        """Recursively ensure child widgets don't draw opaque backgrounds."""
        for child in widget.findChildren(QWidget):
            # Only override widgets that don't already set their own stylesheet
            existing = child.styleSheet()
            if "background-color" not in existing and "background:" not in existing:
                child.setStyleSheet(child.styleSheet() + " background: transparent;")
            child.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)

    # =========================
    # COMPONENTS
    # =========================

    def create_app_icon(self, name: str, icon_path: str, callback=None):
        """Create a desktop icon widget with an optional click callback."""
        container = QWidget()
        container.setFixedSize(90, 90)
        container.setStyleSheet("background: transparent;")

        layout = QVBoxLayout(container)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)

        btn = QPushButton()
        btn.setIcon(QIcon(icon_path))
        btn.setIconSize(QSize(52, 52))
        btn.setFixedSize(64, 64)
        btn.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 14px;
                background-color: rgba(40, 40, 40, 0.65);
                padding: 6px;
            }
            QPushButton:hover {
                background-color: rgba(80, 80, 80, 0.75);
            }
            QPushButton:pressed {
                background-color: rgba(20, 20, 20, 0.85);
            }
        """)
        if callback:
            btn.clicked.connect(callback)

        label = QLabel(name)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: white; font-size: 11px; background: transparent;")
        label.setWordWrap(True)

        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(label)

        return container

    def news_card(self):
        frame = QFrame()
        frame.setFixedWidth(210)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(6)

        title = QLabel("NEWS")
        title.setStyleSheet("color: #E07B39; font-weight: bold; font-size: 12px; background: transparent;")

        content = QLabel("¡Presidente Trump anuncia nuevo acuerdo comercial con la Unión Europea…")
        content.setStyleSheet("color: #cccccc; font-size: 11px; background: transparent;")
        content.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(content)

        frame.setStyleSheet("""
            QFrame {
                background-color: rgba(28, 28, 28, 0.80);
                border-radius: 10px;
                border: 1px solid rgba(255,255,255,0.06);
            }
        """)
        return frame

    def weather_card(self):
        frame = QFrame()
        frame.setFixedWidth(210)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(6)

        title = QLabel("WEATHER")
        title.setStyleSheet("color: #E07B39; font-weight: bold; font-size: 12px; background: transparent;")

        row = QHBoxLayout()
        sun = QLabel("☀ 24°C")
        sun.setStyleSheet("color: white; font-size: 13px; background: transparent;")
        cloud = QLabel("🌧 12%")
        cloud.setStyleSheet("color: #aaaaaa; font-size: 13px; background: transparent;")
        row.addWidget(sun)
        row.addStretch()
        row.addWidget(cloud)

        layout.addWidget(title)
        layout.addLayout(row)

        frame.setStyleSheet("""
            QFrame {
                background-color: rgba(28, 28, 28, 0.80);
                border-radius: 10px;
                border: 1px solid rgba(255,255,255,0.06);
            }
        """)
        return frame

    def search_card(self):
        frame = QFrame()
        frame.setFixedWidth(210)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(6)

        title = QLabel("SEARCH")
        title.setStyleSheet("color: #E07B39; font-weight: bold; font-size: 12px; background: transparent;")

        search_box = QLineEdit()
        search_box.setPlaceholderText("🔍  Buscar en llamaOS...")
        search_box.setStyleSheet("""
            QLineEdit {
                background-color: rgba(50, 50, 50, 0.85);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 12px;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(search_box)

        frame.setStyleSheet("""
            QFrame {
                background-color: rgba(28, 28, 28, 0.80);
                border-radius: 10px;
                border: 1px solid rgba(255,255,255,0.06);
            }
        """)
        return frame

    # =========================
    # APP LISTENERS
    # =========================

    def on_open_calculator(self):
        """TODO: Launch Calculator app."""
        print("[llamaOS] Opening Calculator...")

    def on_open_tasks(self):
        """TODO: Launch Task Manager app."""
        print("[llamaOS] Opening Task Manager...")

    def on_open_explorer(self):
        """TODO: Launch File Explorer app."""
        print("[llamaOS] Opening File Explorer...")

    def on_open_camera(self):
        """TODO: Launch Camera app."""
        print("[llamaOS] Opening Camera...")

    # =========================
    # DOCK LISTENERS
    # =========================

    def on_dock_home(self):
        """TODO: Home / show desktop."""
        print("[llamaOS] Dock → Home")

    def on_dock_browser(self):
        """TODO: Launch Web Browser."""
        print("[llamaOS] Dock → Browser")

    def on_dock_music(self):
        """TODO: Launch Music player."""
        print("[llamaOS] Dock → Music")

    def on_dock_settings(self):
        """TODO: Open Settings panel."""
        print("[llamaOS] Dock → Settings")