print('密碼重試程式')

possword = 'a123456'
x = input ('請輸入密碼，您有3次輸入的機會')
while True :
	if possword == x:
		print('密碼正確')
		break
	elif possword != x :
		print ('輸入錯誤，還有2次機會')
		x = input ('請輸入密碼，您有2次輸入的機會')
		if possword == x:
			print('密碼正確')
			break
		elif possword != x :
			print ('輸入錯誤，還有1次機會')
			x = input ('請輸入密碼，您有1次輸入的機會')
			if possword == x:
				print('密碼正確')
				break
			elif possword != x :
				print ('輸入錯誤，明天再來')
			
				




