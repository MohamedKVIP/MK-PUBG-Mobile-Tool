# -*- coding: utf-8 -*-
# QFont\(\)\s+font\d+\.setFamily\(u"Agency FB"\)  to QFont(font_family)


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from . import resource_path
from .ui_images import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1310, 739)
        MainWindow.setMinimumSize(QSize(1310, 739))
        MainWindow.setMaximumSize(QSize(1310, 739))
        font_id = QFontDatabase.addApplicationFont(resource_path(r"assets\fonts\AGENCYR.TTF"))
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(resource_path(r"assets\icons\logo.ico"), QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMenu::item { background-color: rgb(85, 85, 85); }\n"
"                QComboBox::drop-down {\n"
"                border-image: none;\n"
"                }\n"
"                QComboBox {\n"
"                border-image: url(:/Graphics/fps.png);\n"
"                text-align: center;\n"
"                color: #969696;\n"
"                padding-left: 15px;\n"
"                padding-top: -5px;\n"
"                }\n"
"\n"
"                QPushButton {\n"
"                border-image: url(:/Graphics/fps.png);\n"
"                background-color: none;\n"
"                background-repeat: no-repeat;\n"
"                text-align: center;\n"
"                border: none;\n"
"                color: #969696;\n"
"                padding-top: -3px;\n"
"                }\n"
"\n"
"                QPushButton:checked,\n"
"                QPushButton:pressed {\n"
"                border-image: url(:/Graphics/fps_ckecked.png);\n"
"                background-repeat: no-repeat;\n"
"                color: #c7fff"
                        "6;\n"
"                text-align: center;\n"
"                }\n"
"\n"
"                QPushButton:disabled {\n"
"                color: rgb(80, 80, 80);\n"
"                background-color: rgba(6, 6, 6, 200);\n"
"                }\n"
"            ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.appbackground = QLabel(self.centralwidget)
        self.appbackground.setObjectName(u"appbackground")
        self.appbackground.setEnabled(True)
        self.appbackground.setGeometry(QRect(0, 0, 1311, 741))
        self.appbackground.setStyleSheet(u"border-image: url(:/Graphics/bg.png);")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(29, 80, 1081, 651))
        self.stackedWidget.setStyleSheet(u"QStackedWidget { background-color: #f5f5f5; }")
        self.gfx_page = QWidget()
        self.gfx_page.setObjectName(u"gfx_page")
        self.gfx_page_background = QLabel(self.gfx_page)
        self.gfx_page_background.setObjectName(u"gfx_page_background")
        self.gfx_page_background.setEnabled(True)
        self.gfx_page_background.setGeometry(QRect(-30, -80, 1311, 741))
        self.gfx_page_background.setStyleSheet(u"border-image: url(:/Graphics/bg.png);")
        self.ShadowFrame = QFrame(self.gfx_page)
        self.ShadowFrame.setObjectName(u"ShadowFrame")
        self.ShadowFrame.setGeometry(QRect(10, 450, 307, 113))
        self.ShadowFrame.setMinimumSize(QSize(1, 1))
        self.ShadowFrame.setMaximumSize(QSize(9999, 9999))
        self.ShadowFrame.setStyleSheet(u"")
        self.shadow_label = QLabel(self.ShadowFrame)
        self.shadow_label.setObjectName(u"shadow_label")
        self.shadow_label.setGeometry(QRect(10, 10, 126, 37))
        font1 = QFont(font_family)
        font1.setPointSize(23)
        font1.setBold(True)
        font1.setWeight(75)
        self.shadow_label.setFont(font1)
        self.shadow_label.setStyleSheet(u"color: #ffffff;")
        self.layoutWidget_2 = QWidget(self.ShadowFrame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 60, 287, 43))
        self.ShadowLayout = QHBoxLayout(self.layoutWidget_2)
        self.ShadowLayout.setSpacing(1)
        self.ShadowLayout.setObjectName(u"ShadowLayout")
        self.ShadowLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ShadowLayout.setContentsMargins(2, 1, 2, 1)
        self.disable_shadow_btn = QPushButton(self.layoutWidget_2)
        self.disable_shadow_btn.setObjectName(u"disable_shadow_btn")
        self.disable_shadow_btn.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disable_shadow_btn.sizePolicy().hasHeightForWidth())
        self.disable_shadow_btn.setSizePolicy(sizePolicy)
        self.disable_shadow_btn.setMinimumSize(QSize(141, 41))
        self.disable_shadow_btn.setMaximumSize(QSize(141, 41))
        font2 = QFont(font_family)
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.disable_shadow_btn.setFont(font2)
        self.disable_shadow_btn.setStyleSheet(u"")
        self.disable_shadow_btn.setCheckable(True)
        self.disable_shadow_btn.setFlat(True)

        self.ShadowLayout.addWidget(self.disable_shadow_btn)

        self.enable_shadow_btn = QPushButton(self.layoutWidget_2)
        self.enable_shadow_btn.setObjectName(u"enable_shadow_btn")
        self.enable_shadow_btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.enable_shadow_btn.sizePolicy().hasHeightForWidth())
        self.enable_shadow_btn.setSizePolicy(sizePolicy)
        self.enable_shadow_btn.setMinimumSize(QSize(141, 41))
        self.enable_shadow_btn.setMaximumSize(QSize(141, 41))
        self.enable_shadow_btn.setFont(font2)
        self.enable_shadow_btn.setStyleSheet(u"")
        self.enable_shadow_btn.setCheckable(True)
        self.enable_shadow_btn.setFlat(True)

        self.ShadowLayout.addWidget(self.enable_shadow_btn)

        self.FramerateFrame = QFrame(self.gfx_page)
        self.FramerateFrame.setObjectName(u"FramerateFrame")
        self.FramerateFrame.setGeometry(QRect(10, 110, 875, 117))
        self.FramerateFrame.setMinimumSize(QSize(821, 117))
        self.FramerateFrame.setMaximumSize(QSize(9999, 9999))
        self.FramerateFrame.setStyleSheet(u"")
        self.fps_label = QLabel(self.FramerateFrame)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setGeometry(QRect(10, 10, 180, 37))
        self.fps_label.setFont(font1)
        self.fps_label.setStyleSheet(u"color: #ffffff;")
        self.layoutWidget = QWidget(self.FramerateFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 61, 855, 43))
        self.FramerateLayout = QHBoxLayout(self.layoutWidget)
        self.FramerateLayout.setSpacing(1)
        self.FramerateLayout.setObjectName(u"FramerateLayout")
        self.FramerateLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.FramerateLayout.setContentsMargins(2, 1, 2, 1)
        self.low_fps_btn = QPushButton(self.layoutWidget)
        self.low_fps_btn.setObjectName(u"low_fps_btn")
        sizePolicy.setHeightForWidth(self.low_fps_btn.sizePolicy().hasHeightForWidth())
        self.low_fps_btn.setSizePolicy(sizePolicy)
        self.low_fps_btn.setMinimumSize(QSize(141, 41))
        self.low_fps_btn.setMaximumSize(QSize(141, 41))
        self.low_fps_btn.setFont(font2)
        self.low_fps_btn.setStyleSheet(u"")
        self.low_fps_btn.setCheckable(True)
        self.low_fps_btn.setFlat(True)

        self.FramerateLayout.addWidget(self.low_fps_btn)

        self.medium_fps_btn = QPushButton(self.layoutWidget)
        self.medium_fps_btn.setObjectName(u"medium_fps_btn")
        sizePolicy.setHeightForWidth(self.medium_fps_btn.sizePolicy().hasHeightForWidth())
        self.medium_fps_btn.setSizePolicy(sizePolicy)
        self.medium_fps_btn.setMinimumSize(QSize(141, 41))
        self.medium_fps_btn.setMaximumSize(QSize(141, 41))
        self.medium_fps_btn.setFont(font2)
        self.medium_fps_btn.setStyleSheet(u"")
        self.medium_fps_btn.setCheckable(True)
        self.medium_fps_btn.setFlat(True)

        self.FramerateLayout.addWidget(self.medium_fps_btn)

        self.high_fps_btn = QPushButton(self.layoutWidget)
        self.high_fps_btn.setObjectName(u"high_fps_btn")
        sizePolicy.setHeightForWidth(self.high_fps_btn.sizePolicy().hasHeightForWidth())
        self.high_fps_btn.setSizePolicy(sizePolicy)
        self.high_fps_btn.setMinimumSize(QSize(141, 41))
        self.high_fps_btn.setMaximumSize(QSize(141, 41))
        self.high_fps_btn.setFont(font2)
        self.high_fps_btn.setStyleSheet(u"")
        self.high_fps_btn.setCheckable(True)
        self.high_fps_btn.setFlat(True)

        self.FramerateLayout.addWidget(self.high_fps_btn)

        self.ultra_fps_btn = QPushButton(self.layoutWidget)
        self.ultra_fps_btn.setObjectName(u"ultra_fps_btn")
        sizePolicy.setHeightForWidth(self.ultra_fps_btn.sizePolicy().hasHeightForWidth())
        self.ultra_fps_btn.setSizePolicy(sizePolicy)
        self.ultra_fps_btn.setMinimumSize(QSize(141, 41))
        self.ultra_fps_btn.setMaximumSize(QSize(141, 41))
        self.ultra_fps_btn.setFont(font2)
        self.ultra_fps_btn.setStyleSheet(u"")
        self.ultra_fps_btn.setCheckable(True)
        self.ultra_fps_btn.setFlat(True)

        self.FramerateLayout.addWidget(self.ultra_fps_btn)

        self.extreme_fps_btn = QPushButton(self.layoutWidget)
        self.extreme_fps_btn.setObjectName(u"extreme_fps_btn")
        sizePolicy.setHeightForWidth(self.extreme_fps_btn.sizePolicy().hasHeightForWidth())
        self.extreme_fps_btn.setSizePolicy(sizePolicy)
        self.extreme_fps_btn.setMinimumSize(QSize(141, 41))
        self.extreme_fps_btn.setMaximumSize(QSize(141, 41))
        self.extreme_fps_btn.setFont(font2)
        self.extreme_fps_btn.setStyleSheet(u"")
        self.extreme_fps_btn.setCheckable(True)
        self.extreme_fps_btn.setFlat(True)

        self.FramerateLayout.addWidget(self.extreme_fps_btn)

        self.fps90_fps_btn = QPushButton(self.layoutWidget)
        self.fps90_fps_btn.setObjectName(u"fps90_fps_btn")
        sizePolicy.setHeightForWidth(self.fps90_fps_btn.sizePolicy().hasHeightForWidth())
        self.fps90_fps_btn.setSizePolicy(sizePolicy)
        self.fps90_fps_btn.setMinimumSize(QSize(141, 41))
        self.fps90_fps_btn.setMaximumSize(QSize(141, 41))
        self.fps90_fps_btn.setFont(font2)
        self.fps90_fps_btn.setStyleSheet(u"")
        self.fps90_fps_btn.setCheckable(True)
        self.fps90_fps_btn.setFlat(True)

        self.FramerateLayout.addWidget(self.fps90_fps_btn)

        self.GraphicsFrame = QFrame(self.gfx_page)
        self.GraphicsFrame.setObjectName(u"GraphicsFrame")
        self.GraphicsFrame.setGeometry(QRect(10, 10, 883, 93))
        self.GraphicsFrame.setMinimumSize(QSize(1, 1))
        self.GraphicsFrame.setMaximumSize(QSize(99999, 999999))
        self.GraphicsFrame.setStyleSheet(u"")
        self.graphics_label = QLabel(self.GraphicsFrame)
        self.graphics_label.setObjectName(u"graphics_label")
        self.graphics_label.setGeometry(QRect(11, 0, 136, 37))
        self.graphics_label.setFont(font1)
        self.graphics_label.setStyleSheet(u"\n"
"\n"
"                                    color: #fff;\n"
"                                ")
        self.layoutWidget1 = QWidget(self.GraphicsFrame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 50, 861, 43))
        self.GraphicsLayout = QHBoxLayout(self.layoutWidget1)
        self.GraphicsLayout.setSpacing(1)
        self.GraphicsLayout.setObjectName(u"GraphicsLayout")
        self.GraphicsLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.GraphicsLayout.setContentsMargins(2, 1, 2, 1)
        self.smooth_graphics_btn = QPushButton(self.layoutWidget1)
        self.smooth_graphics_btn.setObjectName(u"smooth_graphics_btn")
        sizePolicy.setHeightForWidth(self.smooth_graphics_btn.sizePolicy().hasHeightForWidth())
        self.smooth_graphics_btn.setSizePolicy(sizePolicy)
        self.smooth_graphics_btn.setMinimumSize(QSize(141, 41))
        self.smooth_graphics_btn.setMaximumSize(QSize(141, 41))
        self.smooth_graphics_btn.setFont(font2)
        self.smooth_graphics_btn.setStyleSheet(u"")
        self.smooth_graphics_btn.setCheckable(True)
        self.smooth_graphics_btn.setFlat(True)

        self.GraphicsLayout.addWidget(self.smooth_graphics_btn)

        self.balanced_graphics_btn = QPushButton(self.layoutWidget1)
        self.balanced_graphics_btn.setObjectName(u"balanced_graphics_btn")
        sizePolicy.setHeightForWidth(self.balanced_graphics_btn.sizePolicy().hasHeightForWidth())
        self.balanced_graphics_btn.setSizePolicy(sizePolicy)
        self.balanced_graphics_btn.setMinimumSize(QSize(141, 41))
        self.balanced_graphics_btn.setMaximumSize(QSize(141, 41))
        self.balanced_graphics_btn.setFont(font2)
        self.balanced_graphics_btn.setStyleSheet(u"")
        self.balanced_graphics_btn.setCheckable(True)
        self.balanced_graphics_btn.setFlat(True)

        self.GraphicsLayout.addWidget(self.balanced_graphics_btn)

        self.hd_graphics_btn = QPushButton(self.layoutWidget1)
        self.hd_graphics_btn.setObjectName(u"hd_graphics_btn")
        sizePolicy.setHeightForWidth(self.hd_graphics_btn.sizePolicy().hasHeightForWidth())
        self.hd_graphics_btn.setSizePolicy(sizePolicy)
        self.hd_graphics_btn.setMinimumSize(QSize(141, 41))
        self.hd_graphics_btn.setMaximumSize(QSize(141, 41))
        self.hd_graphics_btn.setFont(font2)
        self.hd_graphics_btn.setStyleSheet(u"")
        self.hd_graphics_btn.setCheckable(True)
        self.hd_graphics_btn.setFlat(True)

        self.GraphicsLayout.addWidget(self.hd_graphics_btn)

        self.hdr_graphics_btn = QPushButton(self.layoutWidget1)
        self.hdr_graphics_btn.setObjectName(u"hdr_graphics_btn")
        sizePolicy.setHeightForWidth(self.hdr_graphics_btn.sizePolicy().hasHeightForWidth())
        self.hdr_graphics_btn.setSizePolicy(sizePolicy)
        self.hdr_graphics_btn.setMinimumSize(QSize(141, 41))
        self.hdr_graphics_btn.setMaximumSize(QSize(141, 41))
        self.hdr_graphics_btn.setFont(font2)
        self.hdr_graphics_btn.setStyleSheet(u"")
        self.hdr_graphics_btn.setCheckable(True)
        self.hdr_graphics_btn.setFlat(True)

        self.GraphicsLayout.addWidget(self.hdr_graphics_btn)

        self.ultrahd_graphics_btn = QPushButton(self.layoutWidget1)
        self.ultrahd_graphics_btn.setObjectName(u"ultrahd_graphics_btn")
        sizePolicy.setHeightForWidth(self.ultrahd_graphics_btn.sizePolicy().hasHeightForWidth())
        self.ultrahd_graphics_btn.setSizePolicy(sizePolicy)
        self.ultrahd_graphics_btn.setMinimumSize(QSize(141, 41))
        self.ultrahd_graphics_btn.setMaximumSize(QSize(141, 41))
        self.ultrahd_graphics_btn.setFont(font2)
        self.ultrahd_graphics_btn.setStyleSheet(u"")
        self.ultrahd_graphics_btn.setCheckable(True)
        self.ultrahd_graphics_btn.setFlat(True)

        self.GraphicsLayout.addWidget(self.ultrahd_graphics_btn)

        self.uhd_graphics_btn = QPushButton(self.layoutWidget1)
        self.uhd_graphics_btn.setObjectName(u"uhd_graphics_btn")
        self.uhd_graphics_btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.uhd_graphics_btn.sizePolicy().hasHeightForWidth())
        self.uhd_graphics_btn.setSizePolicy(sizePolicy)
        self.uhd_graphics_btn.setMinimumSize(QSize(141, 41))
        self.uhd_graphics_btn.setMaximumSize(QSize(141, 41))
        self.uhd_graphics_btn.setFont(font2)
        self.uhd_graphics_btn.setStyleSheet(u"")
        self.uhd_graphics_btn.setCheckable(True)
        self.uhd_graphics_btn.setFlat(True)

        self.GraphicsLayout.addWidget(self.uhd_graphics_btn)

        self.StyleFrame = QFrame(self.gfx_page)
        self.StyleFrame.setObjectName(u"StyleFrame")
        self.StyleFrame.setEnabled(True)
        self.StyleFrame.setGeometry(QRect(10, 220, 871, 237))
        self.StyleFrame.setMinimumSize(QSize(820, 231))
        self.StyleFrame.setMaximumSize(QSize(9999, 9999))
        self.StyleFrame.setStyleSheet(u"QPushButton {\n"
"                                border: none;\n"
"                                border-image: none;\n"
"                                background: transparent;\n"
"                                icon-size: 100%;\n"
"                                qproperty-iconSize: 150px; /* set the size of the button icon */\n"
"                                qproperty-text: \"\"; /* set the text displayed on the button */\n"
"                                qproperty-flat: true; /* remove the default button border */\n"
"                                padding: 0; /* remove any padding */\n"
"                                }\n"
"\n"
"                                QPushButton:checked {\n"
"                                border-width: 5px; /* set the width of the border */\n"
"                                border-image: url(:/Graphics/checked.png);\n"
"                                }\n"
"                            ")
        self.style_label = QLabel(self.StyleFrame)
        self.style_label.setObjectName(u"style_label")
        self.style_label.setGeometry(QRect(10, 10, 78, 37))
        self.style_label.setFont(font1)
        self.style_label.setStyleSheet(u"color: #ffffff;")
        self.layoutWidget2 = QWidget(self.StyleFrame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 60, 851, 167))
        self.StyleLayout = QHBoxLayout(self.layoutWidget2)
        self.StyleLayout.setObjectName(u"StyleLayout")
        self.StyleLayout.setContentsMargins(0, 0, 0, 0)
        self.classic_style_btn = QPushButton(self.layoutWidget2)
        self.classic_style_btn.setObjectName(u"classic_style_btn")
        sizePolicy.setHeightForWidth(self.classic_style_btn.sizePolicy().hasHeightForWidth())
        self.classic_style_btn.setSizePolicy(sizePolicy)
        self.classic_style_btn.setMinimumSize(QSize(165, 165))
        self.classic_style_btn.setMaximumSize(QSize(165, 165))
        self.classic_style_btn.setStyleSheet(u"QPushButton {\n"
"                                                qproperty-icon: url(:/Graphics/Classic.png); /* set the button icon */\n"
"                                                }\n"
"                                            ")
        self.classic_style_btn.setCheckable(True)

        self.StyleLayout.addWidget(self.classic_style_btn)

        self.colorful_style_btn = QPushButton(self.layoutWidget2)
        self.colorful_style_btn.setObjectName(u"colorful_style_btn")
        sizePolicy.setHeightForWidth(self.colorful_style_btn.sizePolicy().hasHeightForWidth())
        self.colorful_style_btn.setSizePolicy(sizePolicy)
        self.colorful_style_btn.setMinimumSize(QSize(165, 165))
        self.colorful_style_btn.setMaximumSize(QSize(165, 165))
        self.colorful_style_btn.setStyleSheet(u"QPushButton {\n"
"                                                qproperty-icon: url(:/Graphics/Colorful.png); /* set the button icon */\n"
"                                                }\n"
"\n"
"                                            ")
        self.colorful_style_btn.setCheckable(True)

        self.StyleLayout.addWidget(self.colorful_style_btn)

        self.realistic_style_btn = QPushButton(self.layoutWidget2)
        self.realistic_style_btn.setObjectName(u"realistic_style_btn")
        sizePolicy.setHeightForWidth(self.realistic_style_btn.sizePolicy().hasHeightForWidth())
        self.realistic_style_btn.setSizePolicy(sizePolicy)
        self.realistic_style_btn.setMinimumSize(QSize(165, 165))
        self.realistic_style_btn.setMaximumSize(QSize(165, 165))
        self.realistic_style_btn.setStyleSheet(u"QPushButton {\n"
"                                                qproperty-icon: url(:/Graphics/Realistic.png); /* set the button icon */\n"
"                                                }\n"
"\n"
"                                            ")
        self.realistic_style_btn.setCheckable(True)

        self.StyleLayout.addWidget(self.realistic_style_btn)

        self.soft_style_btn = QPushButton(self.layoutWidget2)
        self.soft_style_btn.setObjectName(u"soft_style_btn")
        sizePolicy.setHeightForWidth(self.soft_style_btn.sizePolicy().hasHeightForWidth())
        self.soft_style_btn.setSizePolicy(sizePolicy)
        self.soft_style_btn.setMinimumSize(QSize(165, 165))
        self.soft_style_btn.setMaximumSize(QSize(165, 165))
        self.soft_style_btn.setStyleSheet(u"QPushButton {\n"
"                                                qproperty-icon: url(:/Graphics/Soft.png); /* set the button icon */\n"
"                                                }\n"
"                                            ")
        self.soft_style_btn.setCheckable(True)

        self.StyleLayout.addWidget(self.soft_style_btn)

        self.movie_style_btn = QPushButton(self.layoutWidget2)
        self.movie_style_btn.setObjectName(u"movie_style_btn")
        sizePolicy.setHeightForWidth(self.movie_style_btn.sizePolicy().hasHeightForWidth())
        self.movie_style_btn.setSizePolicy(sizePolicy)
        self.movie_style_btn.setMinimumSize(QSize(165, 165))
        self.movie_style_btn.setMaximumSize(QSize(165, 165))
        self.movie_style_btn.setStyleSheet(u"QPushButton {\n"
"                                                qproperty-icon: url(:/Graphics/Movie.png); /* set the button icon */\n"
"                                                }\n"
"                                            ")
        self.movie_style_btn.setCheckable(True)

        self.StyleLayout.addWidget(self.movie_style_btn)

        self.submit_gfx_btn = QPushButton(self.gfx_page)
        self.submit_gfx_btn.setObjectName(u"submit_gfx_btn")
        self.submit_gfx_btn.setGeometry(QRect(960, 580, 121, 51))
        font3 = QFont(font_family)
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.submit_gfx_btn.setFont(font3)
        self.submit_gfx_btn.setStyleSheet(u"QPushButton {\n"
"                                border-image: url(:/Graphics/submit.png);\n"
"                                border: 1px solid black;\n"
"                                color: rgb(0, 0, 0);\n"
"                                }\n"
"\n"
"                                QPushButton:checked,\n"
"                                QPushButton:pressed {\n"
"                                border-image: url(:/Graphics/submit_pressed.png);\n"
"                                background-color: rgba(0, 0, 0, 0);\n"
"                                border: 3px solid #969696;\n"
"                                background-repeat: no-repeat;\n"
"                                color: #c7fff6;\n"
"                                text-align: center;\n"
"                                }\n"
"                                QPushButton:disabled {\n"
"                                color: rgb(80, 80, 80);\n"
"                                background-color: rgba(6, 6, 6, 200);\n"
"                           "
                        "     }\n"
"                            ")
        self.connect_gameloop_btn = QPushButton(self.gfx_page)
        self.connect_gameloop_btn.setObjectName(u"connect_gameloop_btn")
        self.connect_gameloop_btn.setEnabled(True)
        self.connect_gameloop_btn.setGeometry(QRect(710, 580, 241, 51))
        font4 = QFont(font_family)
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.connect_gameloop_btn.setFont(font4)
        self.connect_gameloop_btn.setStyleSheet(u"QPushButton:checked {\n"
"                                color: rgb(0, 170, 0);\n"
"                                }\n"
"                            ")
        self.connect_gameloop_btn.setCheckable(True)
        self.ResolutionkrFrame = QFrame(self.gfx_page)
        self.ResolutionkrFrame.setObjectName(u"ResolutionkrFrame")
        self.ResolutionkrFrame.setGeometry(QRect(550, 450, 319, 111))
        self.ResolutionkrFrame.setMinimumSize(QSize(1, 1))
        self.ResolutionkrFrame.setMaximumSize(QSize(9999, 9999))
        self.resolution_label = QLabel(self.ResolutionkrFrame)
        self.resolution_label.setObjectName(u"resolution_label")
        self.resolution_label.setGeometry(QRect(10, 10, 299, 35))
        font5 = QFont(font_family)
        font5.setPointSize(22)
        font5.setBold(True)
        font5.setWeight(75)
        self.resolution_label.setFont(font5)
        self.resolution_label.setStyleSheet(u"color: #ffffff;")
        self.resolution_btn = QPushButton(self.ResolutionkrFrame)
        self.resolution_btn.setObjectName(u"resolution_btn")
        self.resolution_btn.setGeometry(QRect(10, 60, 141, 41))
        sizePolicy.setHeightForWidth(self.resolution_btn.sizePolicy().hasHeightForWidth())
        self.resolution_btn.setSizePolicy(sizePolicy)
        self.resolution_btn.setMinimumSize(QSize(141, 41))
        self.resolution_btn.setMaximumSize(QSize(141, 41))
        self.resolution_btn.setFont(font2)
        self.resolution_btn.setStyleSheet(u"")
        self.resolution_btn.setCheckable(True)
        self.resolution_btn.setFlat(True)
        self.PubgchooseFrame = QFrame(self.gfx_page)
        self.PubgchooseFrame.setObjectName(u"PubgchooseFrame")
        self.PubgchooseFrame.setGeometry(QRect(450, 570, 261, 90))
        self.PubgchooseFrame.setFrameShape(QFrame.StyledPanel)
        self.PubgchooseFrame.setFrameShadow(QFrame.Raised)
        self.pubgchoose_btn = QPushButton(self.PubgchooseFrame)
        self.pubgchoose_btn.setObjectName(u"pubgchoose_btn")
        self.pubgchoose_btn.setGeometry(QRect(180, 10, 71, 51))
        sizePolicy.setHeightForWidth(self.pubgchoose_btn.sizePolicy().hasHeightForWidth())
        self.pubgchoose_btn.setSizePolicy(sizePolicy)
        self.pubgchoose_btn.setFont(font2)
        self.pubgchoose_btn.setStyleSheet(u"")
        self.pubgchoose_btn.setFlat(True)
        self.pubgchoose_dropdown = QComboBox(self.PubgchooseFrame)
        self.pubgchoose_dropdown.setObjectName(u"pubgchoose_dropdown")
        self.pubgchoose_dropdown.setGeometry(QRect(0, 10, 171, 51))
        font6 = QFont(font_family)
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setWeight(75)
        self.pubgchoose_dropdown.setFont(font6)
        self.pubgchoose_dropdown.setStyleSheet(u"")
        self.pubgchoose_label = QLabel(self.PubgchooseFrame)
        self.pubgchoose_label.setObjectName(u"pubgchoose_label")
        self.pubgchoose_label.setGeometry(QRect(0, 59, 251, 21))
        font7 = QFont(font_family)
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.pubgchoose_label.setFont(font7)
        self.pubgchoose_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"                                    text-align: center;\n"
"                                    padding-top: -30px;\n"
"                                ")
        self.stackedWidget.addWidget(self.gfx_page)
        self.other_page = QWidget()
        self.other_page.setObjectName(u"other_page")
        self.other_page_background = QLabel(self.other_page)
        self.other_page_background.setObjectName(u"other_page_background")
        self.other_page_background.setGeometry(QRect(-10, -80, 1311, 741))
        self.other_page_background.setStyleSheet(u"border-image: url(:/Graphics/bg.png);")
        self.tempcleaner_other_btn = QPushButton(self.other_page)
        self.tempcleaner_other_btn.setObjectName(u"tempcleaner_other_btn")
        self.tempcleaner_other_btn.setGeometry(QRect(50, 120, 411, 51))
        self.tempcleaner_other_btn.setMinimumSize(QSize(141, 1))
        self.tempcleaner_other_btn.setMaximumSize(QSize(999, 999))
        font8 = QFont(font_family)
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setWeight(75)
        font8.setKerning(False)
        self.tempcleaner_other_btn.setFont(font8)
        self.tempcleaner_other_btn.setStyleSheet(u"")
        self.tempcleaner_other_btn.setCheckable(False)
        self.glsmartsettings_other_btn = QPushButton(self.other_page)
        self.glsmartsettings_other_btn.setObjectName(u"glsmartsettings_other_btn")
        self.glsmartsettings_other_btn.setGeometry(QRect(50, 190, 411, 51))
        self.glsmartsettings_other_btn.setMinimumSize(QSize(141, 1))
        self.glsmartsettings_other_btn.setMaximumSize(QSize(999, 999))
        self.glsmartsettings_other_btn.setFont(font8)
        self.glsmartsettings_other_btn.setStyleSheet(u"")
        self.glsmartsettings_other_btn.setCheckable(False)
        self.gloptimizer_other_btn = QPushButton(self.other_page)
        self.gloptimizer_other_btn.setObjectName(u"gloptimizer_other_btn")
        self.gloptimizer_other_btn.setGeometry(QRect(50, 260, 411, 51))
        self.gloptimizer_other_btn.setMinimumSize(QSize(141, 1))
        self.gloptimizer_other_btn.setMaximumSize(QSize(999, 999))
        self.gloptimizer_other_btn.setFont(font8)
        self.gloptimizer_other_btn.setStyleSheet(u"")
        self.gloptimizer_other_btn.setCheckable(False)
        self.all_other_btn = QPushButton(self.other_page)
        self.all_other_btn.setObjectName(u"all_other_btn")
        self.all_other_btn.setGeometry(QRect(50, 330, 411, 51))
        self.all_other_btn.setMinimumSize(QSize(141, 1))
        self.all_other_btn.setMaximumSize(QSize(999, 999))
        self.all_other_btn.setFont(font8)
        self.all_other_btn.setStyleSheet(u"")
        self.all_other_btn.setCheckable(False)
        self.forceclosegl_other_btn = QPushButton(self.other_page)
        self.forceclosegl_other_btn.setObjectName(u"forceclosegl_other_btn")
        self.forceclosegl_other_btn.setGeometry(QRect(50, 420, 411, 51))
        self.forceclosegl_other_btn.setMinimumSize(QSize(141, 1))
        self.forceclosegl_other_btn.setMaximumSize(QSize(999, 999))
        self.forceclosegl_other_btn.setFont(font8)
        self.forceclosegl_other_btn.setStyleSheet(u"QPushButton {\n"
"                                background-color: rgba(255, 0, 4, 50);\n"
"                                }\n"
"\n"
"\n"
"                            ")
        self.forceclosegl_other_btn.setCheckable(False)
        self.dns_dropdown = QComboBox(self.other_page)
        self.dns_dropdown.addItem("")
        self.dns_dropdown.addItem("")
        self.dns_dropdown.addItem("")
        self.dns_dropdown.addItem("")
        self.dns_dropdown.addItem("")
        self.dns_dropdown.setObjectName(u"dns_dropdown")
        self.dns_dropdown.setGeometry(QRect(540, 280, 301, 46))
        self.dns_dropdown.setFont(font4)
        self.dns_dropdown.setStyleSheet(u"")
        self.shortcut_dropdown = QComboBox(self.other_page)
        self.shortcut_dropdown.addItem("")
        self.shortcut_dropdown.addItem("")
        self.shortcut_dropdown.addItem("")
        self.shortcut_dropdown.addItem("")
        self.shortcut_dropdown.addItem("")
        self.shortcut_dropdown.setObjectName(u"shortcut_dropdown")
        self.shortcut_dropdown.setGeometry(QRect(540, 150, 301, 46))
        self.shortcut_dropdown.setFont(font4)
        self.shortcut_dropdown.setStyleSheet(u"")
        self.optimizer_label = QLabel(self.other_page)
        self.optimizer_label.setObjectName(u"optimizer_label")
        self.optimizer_label.setGeometry(QRect(30, 50, 351, 51))
        font9 = QFont(font_family)
        font9.setPointSize(28)
        font9.setBold(True)
        font9.setWeight(75)
        self.optimizer_label.setFont(font9)
        self.optimizer_label.setStyleSheet(u"text-align: center;\n"
"                                border: none;\n"
"                                color: rgb(255, 255, 255);\n"
"                            ")
        self.shortcut_other_btn = QPushButton(self.other_page)
        self.shortcut_other_btn.setObjectName(u"shortcut_other_btn")
        self.shortcut_other_btn.setGeometry(QRect(854, 150, 221, 46))
        self.shortcut_other_btn.setFont(font8)
        self.shortcut_other_btn.setStyleSheet(u"")
        self.shortcut_other_btn.setCheckable(False)
        self.line = QFrame(self.other_page)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(480, 110, 20, 361))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.shortcut_label = QLabel(self.other_page)
        self.shortcut_label.setObjectName(u"shortcut_label")
        self.shortcut_label.setGeometry(QRect(520, 90, 351, 51))
        self.shortcut_label.setFont(font9)
        self.shortcut_label.setStyleSheet(u"text-align: center;\n"
"                                border: none;\n"
"                                color: rgb(255, 255, 255);\n"
"                            ")
        self.dns_label = QLabel(self.other_page)
        self.dns_label.setObjectName(u"dns_label")
        self.dns_label.setGeometry(QRect(520, 220, 351, 51))
        self.dns_label.setFont(font9)
        self.dns_label.setStyleSheet(u"text-align: center;\n"
"                                border: none;\n"
"                                color: rgb(255, 255, 255);\n"
"                            ")
        self.dns_other_btn = QPushButton(self.other_page)
        self.dns_other_btn.setObjectName(u"dns_other_btn")
        self.dns_other_btn.setGeometry(QRect(854, 280, 221, 46))
        self.dns_other_btn.setFont(font8)
        self.dns_other_btn.setStyleSheet(u"")
        self.dns_other_btn.setCheckable(False)
        self.dns_status_label = QLabel(self.other_page)
        self.dns_status_label.setObjectName(u"dns_status_label")
        self.dns_status_label.setGeometry(QRect(550, 330, 301, 31))
        self.dns_status_label.setFont(font6)
        self.dns_status_label.setStyleSheet(u"color: #969696;")
        self.ipad_label = QLabel(self.other_page)
        self.ipad_label.setObjectName(u"ipad_label")
        self.ipad_label.setGeometry(QRect(520, 350, 351, 51))
        self.ipad_label.setFont(font9)
        self.ipad_label.setStyleSheet(u"text-align: center;\n"
"                                border: none;\n"
"                                color: rgb(255, 255, 255);\n"
"                            ")
        self.ipad_other_btn = QPushButton(self.other_page)
        self.ipad_other_btn.setObjectName(u"ipad_other_btn")
        self.ipad_other_btn.setGeometry(QRect(854, 410, 221, 46))
        self.ipad_other_btn.setFont(font8)
        self.ipad_other_btn.setStyleSheet(u"")
        self.ipad_other_btn.setCheckable(False)
        self.ipad_dropdown = QComboBox(self.other_page)
        self.ipad_dropdown.addItem("")
        self.ipad_dropdown.addItem("")
        self.ipad_dropdown.addItem("")
        self.ipad_dropdown.addItem("")
        self.ipad_dropdown.setObjectName(u"ipad_dropdown")
        self.ipad_dropdown.setGeometry(QRect(540, 410, 301, 46))
        self.ipad_dropdown.setFont(font4)
        self.ipad_dropdown.setStyleSheet(u"")
        self.ipad_code = QLineEdit(self.other_page)
        self.ipad_code.setObjectName(u"ipad_code")
        self.ipad_code.setGeometry(QRect(540, 470, 301, 31))
        font10 = QFont(font_family)
        font10.setPointSize(17)
        font10.setBold(True)
        font10.setWeight(75)
        self.ipad_code.setFont(font10)
        self.ipad_code.setStyleSheet(u"border-image: url(:/Graphics/fps.png);\n"
"                                text-align: center;\n"
"                                color: #969696;\n"
"\n"
"                            ")
        self.ipad_code.setAlignment(Qt.AlignCenter)
        self.ipad_code.setReadOnly(True)
        self.ipad_code_label = QLabel(self.other_page)
        self.ipad_code_label.setObjectName(u"ipad_code_label")
        self.ipad_code_label.setGeometry(QRect(550, 500, 251, 21))
        font11 = QFont(font_family)
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.ipad_code_label.setFont(font11)
        self.ipad_code_label.setStyleSheet(u"color: #969696;")
        self.ipad_rest_btn = QPushButton(self.other_page)
        self.ipad_rest_btn.setObjectName(u"ipad_rest_btn")
        self.ipad_rest_btn.setGeometry(QRect(854, 470, 221, 31))
        font12 = QFont(font_family)
        font12.setPointSize(15)
        font12.setBold(True)
        font12.setWeight(75)
        font12.setKerning(False)
        self.ipad_rest_btn.setFont(font12)
        self.ipad_rest_btn.setStyleSheet(u"")
        self.ipad_rest_btn.setCheckable(False)
        self.stackedWidget.addWidget(self.other_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.about_page.setMaximumSize(QSize(1081, 651))
        self.label_8 = QLabel(self.about_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QRect(-30, -80, 1311, 741))
        self.label_8.setStyleSheet(u"border-image: url(:/Graphics/bg.png);")
        self.about_label_text = QLabel(self.about_page)
        self.about_label_text.setObjectName(u"about_label_text")
        self.about_label_text.setGeometry(QRect(20, 0, 1061, 571))
        self.about_label_text.setMaximumSize(QSize(1061, 571))
        font13 = QFont(font_family)
        font13.setPointSize(20)
        font13.setBold(False)
        font13.setWeight(50)
        self.about_label_text.setFont(font13)
        self.about_label_text.setStyleSheet(u"text-align: center;\n"
"                                border: none;\n"
"                                color: rgb(255, 255, 255);\n"
"                            ")
        self.about_label_text.setOpenExternalLinks(True)
        self.stackedWidget.addWidget(self.about_page)
        self.appname_label = QLabel(self.centralwidget)
        self.appname_label.setObjectName(u"appname_label")
        self.appname_label.setGeometry(QRect(30, 0, 669, 57))
        font14 = QFont(font_family)
        font14.setPointSize(35)
        font14.setBold(True)
        font14.setWeight(75)
        self.appname_label.setFont(font14)
        self.appname_label.setStyleSheet(u"text-align: center;\n"
"                        border: none;\n"
"                        color: rgb(255, 255, 255);\n"
"                    ")
        self.appstatus_label = QLabel(self.centralwidget)
        self.appstatus_label.setObjectName(u"appstatus_label")
        self.appstatus_label.setGeometry(QRect(10, 672, 93, 44))
        font15 = QFont(font_family)
        font15.setPointSize(19)
        font15.setBold(True)
        font15.setWeight(75)
        self.appstatus_label.setFont(font15)
        self.appstatus_label.setStyleSheet(u"color: #ffffff;")
        self.appstatus_text_lable = QLabel(self.centralwidget)
        self.appstatus_text_lable.setObjectName(u"appstatus_text_lable")
        self.appstatus_text_lable.setGeometry(QRect(70, 673, 401, 44))
        font16 = QFont(font_family)
        font16.setPointSize(16)
        font16.setBold(True)
        font16.setWeight(75)
        self.appstatus_text_lable.setFont(font16)
        self.appstatus_text_lable.setStyleSheet(u"color: #ffffff;")
        self.close_btn = QPushButton(self.centralwidget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(1240, 10, 51, 41))
        font17 = QFont()
        font17.setFamily(u"MS Shell Dlg 2")
        font17.setPointSize(30)
        font17.setBold(True)
        font17.setWeight(75)
        self.close_btn.setFont(font17)
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"                        border-image: none;\n"
"                        background-color: none;\n"
"                        background-repeat: no-repeat;\n"
"                        text-align: center;\n"
"                        border: none;\n"
"                        color: #FFF;\n"
"                        padding-top: -3px;\n"
"                        }\n"
"\n"
"                        QPushButton:checked,\n"
"                        QPushButton:pressed {\n"
"                        border-image: none;\n"
"                        background-color: rgba(0, 0, 0, 0);\n"
"                        background-repeat: no-repeat;\n"
"                        color: #c7fff6;\n"
"                        text-align: center;\n"
"                        }\n"
"                    ")
        self.close_btn.setFlat(True)
        self.minimize_btn = QPushButton(self.centralwidget)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(1180, 10, 51, 41))
        font18 = QFont()
        font18.setFamily(u"MS Shell Dlg 2")
        font18.setPointSize(36)
        font18.setBold(True)
        font18.setWeight(75)
        self.minimize_btn.setFont(font18)
        self.minimize_btn.setStyleSheet(u"QPushButton {\n"
"                        border-image: none;\n"
"                        background-color: none;\n"
"                        background-repeat: no-repeat;\n"
"                        text-align: center;\n"
"                        border: none;\n"
"                        color: #FFF;\n"
"                        padding-top: -3px;\n"
"                        }\n"
"\n"
"                        QPushButton:checked,\n"
"                        QPushButton:pressed {\n"
"                        border-image: none;\n"
"                        background-color: rgba(0, 0, 0, 0);\n"
"                        background-repeat: no-repeat;\n"
"                        color: #c7fff6;\n"
"                        text-align: center;\n"
"                        }\n"
"                    ")
        self.minimize_btn.setFlat(True)
        self.PagesFrame = QFrame(self.centralwidget)
        self.PagesFrame.setObjectName(u"PagesFrame")
        self.PagesFrame.setGeometry(QRect(1140, 50, 168, 661))
        self.PagesFrame.setStyleSheet(u"QPushButton {\n"
"                        border-image: none;\n"
"                        text-align: center;\n"
"                        border: none;\n"
"                        color: #969696; /* sets the text color to #969696 */\n"
"                        text-align: center; /* aligns the text to the left */\n"
"\n"
"                        }\n"
"\n"
"                        QPushButton:checked {\n"
"\n"
"                        border-image: url(:/Graphics/menu_checked.png);\n"
"\n"
"                        color: #f7d620; /* sets the text color to #b7ece4 */\n"
"                        background-repeat: no-repeat;\n"
"                        text-align: center;\n"
"                        }\n"
"                    ")
        self.PagesFrame.setFrameShape(QFrame.StyledPanel)
        self.PagesFrame.setFrameShadow(QFrame.Raised)
        self.gfx_button = QPushButton(self.PagesFrame)
        self.gfx_button.setObjectName(u"gfx_button")
        self.gfx_button.setGeometry(QRect(0, 10, 168, 80))
        self.gfx_button.setFont(font1)
        self.gfx_button.setStyleSheet(u"")
        self.gfx_button.setCheckable(True)
        self.gfx_button.setChecked(True)
        self.gfx_button.setFlat(True)
        self.other_button = QPushButton(self.PagesFrame)
        self.other_button.setObjectName(u"other_button")
        self.other_button.setGeometry(QRect(0, 90, 168, 80))
        self.other_button.setFont(font1)
        self.other_button.setStyleSheet(u"")
        self.other_button.setCheckable(True)
        self.other_button.setFlat(True)
        self.about_button = QPushButton(self.PagesFrame)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setGeometry(QRect(0, 565, 168, 80))
        self.about_button.setFont(font1)
        self.about_button.setStyleSheet(u"")
        self.about_button.setCheckable(True)
        self.about_button.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MK PUBG Mobile Tool", None))
        self.appbackground.setText("")
        self.gfx_page_background.setText("")
        self.shadow_label.setText(QCoreApplication.translate("MainWindow", u"Shadow", None))
#if QT_CONFIG(tooltip)
        self.disable_shadow_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Soon Can Edit", None))
#endif // QT_CONFIG(tooltip)
        self.disable_shadow_btn.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
#if QT_CONFIG(tooltip)
        self.enable_shadow_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Soon Can Edit", None))
#endif // QT_CONFIG(tooltip)
        self.enable_shadow_btn.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.fps_label.setText(QCoreApplication.translate("MainWindow", u"Frame Rate", None))
        self.low_fps_btn.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.medium_fps_btn.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.high_fps_btn.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.ultra_fps_btn.setText(QCoreApplication.translate("MainWindow", u"Ultra", None))
        self.extreme_fps_btn.setText(QCoreApplication.translate("MainWindow", u"Extreme", None))
        self.fps90_fps_btn.setText(QCoreApplication.translate("MainWindow", u"Extreme+", None))
        self.graphics_label.setText(QCoreApplication.translate("MainWindow", u"Graphics", None))
        self.smooth_graphics_btn.setText(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.balanced_graphics_btn.setText(QCoreApplication.translate("MainWindow", u"Balanced", None))
        self.hd_graphics_btn.setText(QCoreApplication.translate("MainWindow", u"HD", None))
        self.hdr_graphics_btn.setText(QCoreApplication.translate("MainWindow", u"HDR", None))
        self.ultrahd_graphics_btn.setText(QCoreApplication.translate("MainWindow", u"Ultra HD", None))
#if QT_CONFIG(tooltip)
        self.uhd_graphics_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Extreme HDR graphics feature\n"
"                                                not yet available in the game.</p></body></html>\n"
"                                            ", None))
#endif // QT_CONFIG(tooltip)
        self.uhd_graphics_btn.setText(QCoreApplication.translate("MainWindow", u"Extreme HDR", None))
        self.style_label.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.submit_gfx_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(tooltip)
        self.connect_gameloop_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to connect to Gameloop", None))
#endif // QT_CONFIG(tooltip)
        self.connect_gameloop_btn.setText(QCoreApplication.translate("MainWindow", u"Connect to Gameloop", None))
        self.resolution_label.setText(QCoreApplication.translate("MainWindow", u"Resolution PUBG KR", None))
        self.resolution_btn.setText(QCoreApplication.translate("MainWindow", u"1080p", None))
        self.pubgchoose_btn.setText(QCoreApplication.translate("MainWindow", u"Use", None))
        self.pubgchoose_label.setText(QCoreApplication.translate("MainWindow", u"Select the game version you need to use.", None))
        self.other_page_background.setText("")
#if QT_CONFIG(tooltip)
        self.tempcleaner_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Clean temporary files and boost system performance.", None))
#endif // QT_CONFIG(tooltip)
        self.tempcleaner_other_btn.setText(QCoreApplication.translate("MainWindow", u"Temp Cleaner", None))
#if QT_CONFIG(tooltip)
        self.glsmartsettings_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Get the perfect Gameloop settings for your PC hardware.", None))
#endif // QT_CONFIG(tooltip)
        self.glsmartsettings_other_btn.setText(QCoreApplication.translate("MainWindow", u"Gameloop Smart Settings (Beta)", None))
#if QT_CONFIG(tooltip)
        self.gloptimizer_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1- Optimize Gameloop Registry in\n"
"                                Windows. </p><p>2- Nvidia Optimizer (Nvidia GPU). </p><p>3- Add\n"
"                                to Exclusion List for faster game startup.</p></body></html>\n"
"                            ", None))
#endif // QT_CONFIG(tooltip)
        self.gloptimizer_other_btn.setText(QCoreApplication.translate("MainWindow", u"Gameloop Optimizer", None))
#if QT_CONFIG(tooltip)
        self.all_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Temp Cleaner</p><p\n"
"                                align=\"center\">Gameloop Smart Settings</p><p align=\"center\">Gameloop\n"
"                                Optimizer</p><p align=\"center\">&gt;&gt; One-click Magic\n"
"                                &lt;&lt;</p></body></html>\n"
"                            ", None))
#endif // QT_CONFIG(tooltip)
        self.all_other_btn.setText(QCoreApplication.translate("MainWindow", u"\u2b06\ufe0f All \u2b06\ufe0f", None))
#if QT_CONFIG(tooltip)
        self.forceclosegl_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Force Kill Gameloop Processes.", None))
#endif // QT_CONFIG(tooltip)
        self.forceclosegl_other_btn.setText(QCoreApplication.translate("MainWindow", u"Force Close Gameloop", None))
        self.dns_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Google DNS - 8.8.8.8", None))
        self.dns_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Cloudflare DNS - 1.1.1.1", None))
        self.dns_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Quad9 DNS - 9.9.9.9", None))
        self.dns_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Cisco Umbrella - 208.67.222.222", None))
        self.dns_dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Yandex DNS - 77.88.8.1", None))

        self.shortcut_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"PUBG Mobile Global", None))
        self.shortcut_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"PUBG Mobile VN", None))
        self.shortcut_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"PUBG Mobile TW", None))
        self.shortcut_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"PUBG Mobile KR", None))
        self.shortcut_dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Battlegrounds Mobile India", None))

        self.optimizer_label.setText(QCoreApplication.translate("MainWindow", u"Optimizer", None))
#if QT_CONFIG(tooltip)
        self.shortcut_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to create a shortcut for your game on the desktop", None))
#endif // QT_CONFIG(tooltip)
        self.shortcut_other_btn.setText(QCoreApplication.translate("MainWindow", u"Create Shortcut", None))
        self.shortcut_label.setText(QCoreApplication.translate("MainWindow", u"Shortcut Maker", None))
        self.dns_label.setText(QCoreApplication.translate("MainWindow", u"DNS Changer", None))
#if QT_CONFIG(tooltip)
        self.dns_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to change your DNS settings", None))
#endif // QT_CONFIG(tooltip)
        self.dns_other_btn.setText(QCoreApplication.translate("MainWindow", u"Change DNS", None))
        self.dns_status_label.setText("")
        self.ipad_label.setText(QCoreApplication.translate("MainWindow", u"IPad View", None))
#if QT_CONFIG(tooltip)
        self.ipad_other_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to change your DNS settings", None))
#endif // QT_CONFIG(tooltip)
        self.ipad_other_btn.setText(QCoreApplication.translate("MainWindow", u"Change Resolution", None))
        self.ipad_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"1920 x 1440", None))
        self.ipad_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"1600 x 1200", None))
        self.ipad_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"1440 x 1080", None))
        self.ipad_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"1280 x 960", None))

#if QT_CONFIG(tooltip)
        self.ipad_code.setToolTip(QCoreApplication.translate("MainWindow", u"The layout code is provided here", None))
#endif // QT_CONFIG(tooltip)
        self.ipad_code.setText("")
        self.ipad_code_label.setText("")
#if QT_CONFIG(tooltip)
        self.ipad_rest_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Click here to change your DNS settings", None))
#endif // QT_CONFIG(tooltip)
        self.ipad_rest_btn.setText(QCoreApplication.translate("MainWindow", u"Reset Resolution", None))
        self.label_8.setText("")
        self.about_label_text.setText(QCoreApplication.translate("MainWindow", u"<h2>Optimize Your PUBG Mobile Experience with MK PUBG Mobile Tool</h2>\n"
"\n"
"                                <h3>Features:</h3>\n"
"                                <ul>\n"
"                                <li>Universal compatibility for all PUBG Mobile versions.</li>\n"
"                                <li>Graphics enhancement for smoother visuals.</li>\n"
"                                <li>Unlock locked graphics settings for higher customization.</li>\n"
"                                <li>Gameloop and PC optimization for peak performance.</li>\n"
"                                <li>Quick desktop shortcut creation.</li>\n"
"                                <li>DNS changer for optimized network connectivity.</li>\n"
"                                <li>iPad view for an immersive gaming experience.</li>\n"
"                                </ul>\n"
"\n"
"                                <h3>Contact Me:</h3>\n"
"                                <ul>\n"
"                                <li>GitHub: <a href=\"ht"
                        "tps://github.com/MohamedKVIP\">https://github.com/MohamedKVIP</a></li>\n"
"                                <li>Discord: <a href=\"https://discordapp.com/users/414942438088769551\">https://discordapp.com/users/414942438088769551</a></li>\n"
"                                </ul>\n"
"                                <center>\n"
"                                <p>Level up your gaming experience today!</p>\n"
"                                </center>\n"
"                            ", None))
        self.appname_label.setText(QCoreApplication.translate("MainWindow", u"MK PUBG Mobile Tool v1.0.0", None))
        self.appstatus_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.appstatus_text_lable.setText("")
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.minimize_btn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.gfx_button.setText(QCoreApplication.translate("MainWindow", u"GFX", None))
        self.other_button.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi