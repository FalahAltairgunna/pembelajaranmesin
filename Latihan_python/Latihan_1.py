#test menghitung berat badan ideal
import numpy as np

weight = [70, 80, 90]
height = [1.75, 1.80, 1.65]

bmi = np.array(weight) / (np.array(height) ** 2)
print(bmi)

#Kategori BMI (Menurut WHO):
#< 18.5 → Underweight (Kurus)
#18.5 - 24.9 → Normal
#25 - 29.9 → Overweight (Kelebihan berat badan)
#≥ 30 → Obese (Obesitas)