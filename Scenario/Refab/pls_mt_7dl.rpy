﻿label alt_day6_mt_7dl_start:
    call alt_day6_mt_7dl_vars
    pause(1)
    call alt_day6_mt_7dl_begin
    pause(1)
    call alt_day6_mt_7dl_morning
    pause(1)
    if alt_day5_mt_7dl_hentai:
        call alt_day6_mt_7dl_dv_morning
    else:
        call alt_day6_mt_7dl_un_morning
    pause(1)
    call alt_day6_mt_7dl_retail
    pause(1)
    if alt_day5_mt_7dl_hentai:
        call alt_day6_mt_7dl_retail_px
        pause(1)
        call alt_day6_mt_7dl_declaration0
        pause(1)
        call alt_day6_mt_7dl_memento
    else:
        call alt_day6_mt_7dl_retail_vg
        pause(1)
        call alt_day6_mt_7dl_forgive
        pause(1)
        if alt_day4_neu_mt_diary and alt_day5_neu_mt_diary:
            call alt_day6_mt_7dl_diary3
        else:
            call alt_day6_mt_7dl_memento
    pause(1)
    call alt_day6_mt_7dl_dinner
    pause(1)
    call alt_day6_mt_7dl_concert
    pause(1)
    call alt_day6_mt_7dl_supper
    pause(1)
    if mt_pt <= 13:
        call alt_day6_mt_7dl_choice
        pause(1)
        if karma < 0 or not alt_day6_mt_7dl_lms:
           call alt_day6_mt_7dl_catha
           pause(1)
           return
        else:
            call alt_day6_mt_7dl_declare
    else:
        call alt_day6_mt_7dl_declare
    pause(1)
    call alt_day6_mt_7dl_nighttime
    pause(1)
    jump alt_day7_mt_7dl_start
    
label alt_day7_mt_7dl_start:
    call alt_day7_mt_7dl_begin
    pause(1)
    call alt_day7_mt_7dl_morning
    pause(1)
    call alt_day7_mt_7dl_conclude
    pause(1)
    call alt_day7_mt_7dl_byes
    pause(1)
    if alt_day5_mt_7dl_hentai:
        call alt_day7_mt_7dl_dv_bye
    else:
        if alt_day4_fz_sh == 1 or alt_day4_fz_sh == 4:
            call alt_day7_mt_7dl_un_fz_bye
        else:
            call alt_day7_mt_7dl_un_bye
    pause(1)
    call alt_day7_mt_7dl_departure
    pause(1)
    if alt_day7_mt_7dl_pt == 1:
        call alt_day7_mt_7dl_loopthru
        pause(1)
        if mt_pt >= 15 and (alt_day2_date == 6) and alt_day5_neu_mt_diary and alt_day4_neu_mt_diary:
            call alt_day7_mt_7dl_true
        else:
            call alt_day7_mt_7dl_ever_after
    elif alt_day7_mt_7dl_pt == 2 or alt_day7_mt_7dl_pt == 0:
        call alt_day7_mt_7dl_loopback
        pause(1)
        if (mt_pt >= 13) and (alt_day2_date == 6) and (alt_day3_dancing == 5) and alt_day4_neu_mt_fire:
            call alt_day7_mt_7dl_good
            pause(1)
            if alt_day_binder == 1:
                call alt_day7_mt_7dl_postscriptum  
        else:
            call alt_day7_mt_7dl_bad
    pause(1)
    return
