from datetime import datetime


def int_comma(value):
    # check if number is greater than 999
    if abs(value) >= 1000:
        # divide the number by 1000 and round it to one decimal place
        formatted_num = round(value / 1000, 1)
        # check if the result is a whole number
        if formatted_num.is_integer():
            # convert formatted number to an integer if it's a whole number
            formatted_num = int(formatted_num)
        # append 'K' to the formatted number
        formatted_num = str(formatted_num) + 'K'
    else:
        # else just show only the value
        formatted_num = str(value)
    return formatted_num


def date_format(value):
    value_str = value.strftime('%Y-%m-%d')
    date = datetime.strptime(value_str, '%Y-%m-%d')

    if 10 <= date.day <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(date.day % 10, 'th')

    return date.strftime(f'%d{suffix} %b %Y')
