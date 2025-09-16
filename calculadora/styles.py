# # QSS - QT Styles for Python
# # https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html
# # DarkStyles
# # https://pypi.org/project/QDarkStyle/

# import qdarkstyle
# from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)
 
# qss = f"""
#     PushButton[cssClass="specialButton"] {{
#         color: #fff;
#         background: {PRIMARY_COLOR};
#         border-radius: 5px;
#     }}
#     PushButton[cssClass="specialButton"]:hover {{
#         color: #fff;
#         background: {DARKER_PRIMARY_COLOR};
#     }}
#     PushButton[cssClass="specialButton"]:pressed {{
#         color: #fff;
#         background: {DARKEST_PRIMARY_COLOR};
#     }}
# """
 
 
# def setupTheme(app):
#     # Aplicar o estilo escuro do qdarkstyle
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
 
#     # Sobrepor com o QSS personalizado para estilização adicional
#     app.setStyleSheet(app.styleSheet() + qss)

import qdarkstyle
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)

# Seu QSS personalizado
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def setupTheme(app):
    # Carrega o estilo do qdarkstyle
    qdark_stylesheet = qdarkstyle.load_stylesheet_pyside6()
    
    # Combina o estilo do qdarkstyle com o seu estilo personalizado
    combined_stylesheet = qdark_stylesheet + qss
    
    # Aplica o estilo combinado de uma vez só
    app.setStyleSheet(combined_stylesheet)