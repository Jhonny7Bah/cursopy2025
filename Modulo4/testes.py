from datetime import datetime, timedelta
from pytz import timezone

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/05/2025 10:15:00', fmt)

import calendar
import locale 

from pathlib import Path
caminho_projeto = Path(__name__)
print(caminho_projeto.absolute())