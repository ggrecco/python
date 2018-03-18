import re

texto = "Evaldo|Maria|Joaquina|Cirilo|Didi|Mussum|Tarzan"
print(re.split("\|",texto))
print(re.split("[|]",texto))


