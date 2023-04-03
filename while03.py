# 密碼輸入程式

password = 'a123456'
i = 3
while True :
	x = input('請輸入密碼')
	if x == password:
		print ('登入成功')
		break
	else:
		i = i - 1
		print ('輸入錯誤', i,'次機會')
		if i == 0:
			break
	
