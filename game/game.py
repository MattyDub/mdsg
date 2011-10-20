from models import *

P1_UNITS=[{'xpos':0,'ypos':0,'unit_type':'Inf'},
          {'xpos':1,'ypos':1,'unit_type':'Inf'}
    ]
P2_UNITS=[{'xpos':0,'ypos':1,'unit_type':'Inf'},
          {'xpos':1,'ypos':0,'unit_type':'Inf'}
    ]

def init_game_state(player1):
    state = GameState(active_player=player1, turn=1)
    state.save()
    #TODO: if we have multiple scenarios, how do we choose? this is just a short-term hack:
    for u in P1_UNITS:
        unit = Unit(player=player1,xpos=u['xpos'],ypos=u['ypos'],unit_type=u['unit_type'])
        unit.save()
        state.units.add(unit)
    state.save()
    return state
