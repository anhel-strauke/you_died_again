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
        print "SUSP is", SUSP
        SUSP -= SUSP
        print "Reset SUSP to", SUSP


init -1:
    default TIRED = 0
    default TIRED_LIMIT = 14

init -1 python:
    def add_tired_or_jump(label):
        global TIRED, TIRED_LIMIT
        TIRED += 1
        if TIRED >= TIRED_LIMIT:
            renpy.jump(label)

    def reset_susp():
        global TIRED
        TIRED = 0