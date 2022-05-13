from operator import truediv


def is_twodigit_odd(number):
    return True if number % 2 != 0 and len(str(number)) == 2 else False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return True if (user == file_owner and writable_by_owner) or (file_group in users_groups and writable_by_group) or writable_by_others or sudo_mode else False


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year %100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def is_sunday(day, weekday_of_first):
    if day in range(1, 32):
        if weekday_of_first == "M" and day % 7 == 0:
            return True
        elif weekday_of_first == "Tu" and day % 6 == 0:
            return True
        elif weekday_of_first == "W" and day % 5 == 0:
            return True
        elif weekday_of_first == "Th" and day % 4 == 0:
            return True
        elif weekday_of_first == "F" and day % 3 == 0:
            return True
        elif weekday_of_first == "Sa" and day % 2 == 0:
            return True
        else: 
            return False
    else:
        return False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if wind_scale < 7:
        if rains:
            return True
        elif (cloudy and red_sky) or (cloudy and strong_flower_smell) or (cloudy and spiders_down) or (cloudy and lying_cattle):
            return True
        elif strong_sunshine:
            return True
        else:
            return False
    else:
        return False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if want_to and not trouble_sleeping and not after_4pm:
        if at_work and not mad_boss and (have_30m or have_10m):
            return True
        elif not at_work and (have_30m or have_10m):
            return True
        else:
            return False
    else:
        return False