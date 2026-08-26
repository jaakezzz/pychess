from pychess.Utils.Board import Board
from pychess.Utils.const import DRAGONANGA, VARIANTS_OTHER

class DragonangaBoard(Board):
    variant = DRAGONANGA
    cecp_name = "dragonanga"
    standard_rules = False
    variant_group = VARIANTS_OTHER
    name = "Dragonanga"
    __desc__ = "Custom Dragonanga variant"
    
    FENS = ["ehdqkdhe/iippppii/8/8/8/8/IIPPPPII/EHDQKDHE w - - 0 1"]