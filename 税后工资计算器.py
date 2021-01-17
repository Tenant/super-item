def cal_wuxianyijin_monthly(month_salary):
    print("City: Shanghai")
    return month_salary * (8 + 2 + 0.5 + 12) / 100

def cal_wuxianyijin_yearly(month_salary):
    return cal_wuxianyijin_monthly(month_salary) * 12

def cal_zhufanggongjijin_monthly(month_salary):
    return month_salary * 0.12 * 2

def cal_zhufanggongjijin_yearly(month_salary):
    return cal_zhufanggongjijin_monthly(month_salary) * 12

def cal_tax(year_salary):
    year_salary -= 60000
    if year_salary <= 0:
        return 0
    elif 0 < year_salary <= 36000:
        return year_salary * 0.03 - 0
    elif 36000 < year_salary <= 144000:
        return year_salary * 0.10 - 2520
    elif 144000 < year_salary <= 300000:
        return year_salary * 0.20 - 16920
    elif 300000 < year_salary <= 420000:
        return year_salary * 0.25 - 31920
    elif 420000 < year_salary <= 660000:
        return year_salary * 0.30 - 52920
    elif 660000 < year_salary <= 960000:
        return year_salary * 0.35 - 85920
    else:
        return year_salary * 0.45 - 181920

if __name__ == '__main__':
    month_salary = 9999
    month_num = 15.5
    year_salary = month_salary * month_num
    year_salary_need_tax = year_salary - cal_wuxianyijin_yearly(month_salary)
    year_tax = cal_tax(year_salary_need_tax)
    year_salary_payed_tax = year_salary_need_tax - year_tax
    yearly_gongjijin = cal_zhufanggongjijin_yearly(month_salary)
    print("yearly tax: {}".format(year_tax))
    print("yearly neat earning: {}".format(year_salary_payed_tax))
    print("yearly 住房公积金: {}".format(yearly_gongjijin))
    print("yearly neat earning + gongjijin: {}".format(year_salary_payed_tax + yearly_gongjijin))
