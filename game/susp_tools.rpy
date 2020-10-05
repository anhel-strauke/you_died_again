init -1:
    default SUSP = 0
    default SUSP_LIMIT = 3

init -1 python:
    def add_susp_or_jump(label):
        global SUSP, SUSP_LIMIT
        SUSP += 1
        if SUSP >= SUSP_LIMIT:
            renpy.jump(label)

    def reduce_susp(by=1):
        global SUSP
        SUSP -= by
        if SUSP < 0:
            SUSP = 0
    
    def reset_susp():
        global SUSP
        SUSP = 0
