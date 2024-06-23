from utils import get_last_5
from utils import remake_numb
from utils import remake_date
from utils import show_info


file = get_last_5()
file = remake_date(file)
file = remake_numb(file)
show_info(file)

