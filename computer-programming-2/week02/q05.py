element_agirliklari = {
    'H': 1.008,
    'C': 12.011,
    'O': 15.999,
    'N': 14.007,
}
formul = input("Molar kütlesi hesaplanacak kimyasal formulü giriniz: ")
molar_kutle= 0
formul = formul+'X'
for i in range(len(formul)):
    if formul[i].isalpha():
        if formul[i] == 'X':
            break
        temp_number = ''
        number = 1
        temp_i=i
        match formul[i]:
            case 'H':
                while formul[temp_i + 1].isdigit():
                    temp_number += formul[temp_i + 1]
                    temp_i += 1
            case 'C':
                while formul[temp_i + 1].isdigit():
                    temp_number += formul[temp_i + 1]
                    temp_i += 1
            case 'O':
                while formul[temp_i + 1].isdigit():
                    temp_number += formul[temp_i + 1]
                    temp_i += 1
            case 'N':
                while formul[temp_i + 1].isdigit():
                    temp_number += formul[temp_i + 1]
                    temp_i += 1
        number = 1 if len(temp_number) == 0 else int(temp_number)
        molar_kutle += number * element_agirliklari[formul[i]]
    else:
        i += 1
print(f"Molar kütlesi: {molar_kutle:.2f} g/mol")
