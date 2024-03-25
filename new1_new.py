#1
# a = [1,2,3,4,5,6,7,8,]
# for b in a:
#     if b < 5:
#         print(b)

 #2 a = [1,2,3,4,5,6,7,5]
# b = [1,2,3,4,6,7,8,99,9]
#
# new_chalange = []
#
# for item in a:
#     if item in b:
#         new_chalange.append(item)



#
# car_speed = 160
# is_town = True
# result_fine = 0
# is_camera = False
# is_musor =True
#
# fine_for_1_to_10 = 30
# fine_for_11_to_15 = 50
# fine_for_16_to_20 = 70
# fine_for_21_to_25 = 115
# fine_for_26_to_30 = 180
# fine_for_31_to_40 = 260
# fine_for_41_to_50 = 400
# fine_for_51_to_60 = 560
# fine_for_61_to_70 = 700
# fine_for_70_to_more = 800
#
# town_speed = 50
# country_speed = 70
#
# if is_town:
#   over_speed = car_speed - town_speed
# else:
#   over_speed = car_speed - country_speed
# if is_camera and  car_speed >=60:
#   print("Лешение прав")
# elif is_musor and car_speed >=60:
#   print("Давай Взятку Гусь ")
#
# if over_speed < 20:
#   print("Скорость не превышена или превышена незначительно")
# elif over_speed >= 1 and over_speed <= 10:
#   result_fine = fine_for_1_to_10
# elif over_speed >= 11 and over_speed <= 15:
#   result_fine = fine_for_11_to_15
# elif over_speed >= 16 and over_speed <= 20:
#   result_fine = fine_for_16_to_20
# elif over_speed >= 21 and over_speed <= 25:
#   result_fine = fine_for_21_to_25
# elif over_speed >= 26 and over_speed <= 30:
#   result_fine = fine_for_26_to_30
# elif over_speed >= 31 and over_speed <= 40:
#   result_fine = fine_for_31_to_40
# elif over_speed >= 41 and over_speed <= 50:
#   result_fine = fine_for_41_to_50
# elif over_speed >= 51 and over_speed <= 60:
#   result_fine = fine_for_51_to_60
# elif over_speed >= 61 and over_speed <= 70:
#   result_fine = fine_for_61_to_70
# elif over_speed > 70:
#   result_fine = fine_for_70_to_more
# if result_fine >0:
#   print("Штраф:" +str(result_fine))
# else:
#   print("Скорость не превышена или превышена незначительно")