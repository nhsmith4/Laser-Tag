##red_team:list = [[None, None] for i in range(20)]
red_hardware = [None for i in range(20)]
red_id = [None for i in range(20)]
red_nick = [None for i in range(20)]
red_team_scores:int = [i**i for i in range(20)]

##green_team:list = [[None, None] for i in range(20)]
green_team = {}
green_team_scores:int = [10**i for i in range(20)]

message_board_team = ["alice", "sleepy joe","bluey", "apple pie"]

game_time_remaining = "0:00"

time = None
timer = 7