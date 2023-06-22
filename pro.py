medcine={
    'panadol':{
        'price':50,
        'quntity':5
    },
    'cipralec':{
        'price':80,
        'quntity':10
        
    }
}
while True:
    print('1-add item\n2-remove item\n3-update item\n4-is avalibile\n5-print informtion\n6-exit')
    choice= int(input('enter your choice:'))
    if choice==1:
        print('--------adding new item----------')
        it_name=input('enter item name:')
        it_price= int(input('enter item price:'))
        it_q= int(input('enter item qu:'))
        medcine.update({it_name:{'price':it_price,'quntity':it_q}})
        print('the add has succsufuly')
        
    elif choice==2:
      print('--------deleting item----------')  
      it_name=input('enter item name:')
      del medcine[it_name]
      print(f'{it_name} has been deleted')
      print('--------deleting item----------')  
    elif choice==3:
          print('--------updating item----------') 
          it_name=input('enter item name:')
          it_price= int(input('enter new  price:'))
          it_q= int(input('enter new qu:'))
          medcine[it_name]['price']=it_price
          medcine[it_name]['quntity']=it_q
          print(medcine)
         
          print('--------updating item----------') 
    elif choice==4:
                print('--------chekinging item----------')
                it_name=input('enter item name:')
                print(f'we have {medcine[it_name]["quntity"]} of {it_name}')
                print('--------chekinging item----------') 
    elif choice==5:
        it_name=input('enter item name:')
        print(f'name:{it_name}\n-qun:{medcine[it_name]["quntity"]}\n-price:{medcine[it_name]["price"]}')
    elif choice==6:
        break    
                    
          
        
      