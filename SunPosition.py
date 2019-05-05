import math
day = 0 # 日期
latitude = 34.72468 #纬度
# LayerNumber = 34 #层数
# LayerHeight = 2.9 #层高
# ChoseLayerNumber = 26
# FloorSpacing = 38 #楼间距
day_num1 = 0
day_num2 = 0
day_mov = 0.25560439
def GetSunSetDay(LayerNumber,FloorSpacing,LayerHeight,ChoseLayerNumber):#楼间距 层高 楼层
	print(LayerNumber+"   "+FloorSpacing+"   "+LayerHeight+"    "+ChoseLayerNumber)
	global day
	day = 0
	global day_num1
	day_num1 = 0
	global day_num2
	day_num2 = 0
	while day<91:
		day=day+1
		H = 90-(latitude-day_mov*day)
		FloorHeight = float(LayerHeight)*float(LayerNumber)
		FloorCal = float(FloorSpacing)*math.tan(math.pi*(H/180))
		LastCal = (float(FloorHeight)-float(FloorCal))/float(LayerHeight)
		if LastCal<float(ChoseLayerNumber):
			day_num1 = day_num1+1
	day = 0
	while day<91:
		day=day+1
		H = 90-(latitude+day_mov*day)
		FloorHeight = float(LayerHeight)*float(LayerNumber)
		FloorCal = float(FloorSpacing)*math.tan(math.pi*(H/180))
		LastCal = (float(FloorHeight)-float(FloorCal))/float(LayerHeight)
		if float(LastCal)<float(ChoseLayerNumber):
			day_num2 = day_num2+1
	print("sun_set_day in year " + str(day_num1*2+day_num2*2) + "\t no_sun_set in year " + str(364-(day_num1*2+day_num2*2)))
	return ("sun_set_day in year " + str(day_num1*2+day_num2*2) + "\t no_sun_set in year " + str(364-(day_num1*2+day_num2*2)))