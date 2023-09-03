# Скрабл
k = 'ноут'
k_2 = k.upper()
def fun(x):
    for key in dct:
        if x in key:
            return dct.get(key)
 
dct = {
    'AEIOULNSTR' :1, 'DG' :2, 'BCMP' :3,
    'FHVWY' :4, 'K' :5, 'JX' :8, 'QZ' :10, 'АВЕИНОРСТ' :1, 'ДКЛМПУ' :2, 'БГЁЬЯ' :3, 'ЙЫ' : 4, 'ЖЗХЦЧ' :5, 'ШЭЮ' :8, 'ФЩЪ' :10
}
print(sum(map(fun, k_2)))
