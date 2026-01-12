inventory = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'kiwi']
processed_items=[]
char_line=('a', 'e', 'i', 'o', 'u')
for index, item in enumerate(inventory, start=1):
    if index%2==0 and len(item)>5:
        processed_items.append(f'{index}. Удлиненный {item}')

    elif index%2==1 and item[0] in char_line:
        processed_items.append(f'{index}. Стартует с гласной: {item}')

    else: processed_items.append(f'{index}. {item}')
print(f"\nИсходный список: {inventory}")
print(f"Обработанные элементы: \n{'\n'.join(processed_items)}")
