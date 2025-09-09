import cart
import payment
cart_items={}

def main():
    ch=True
    while(ch):
        print("----------Ecommerce----------")
        print("1.add item \n2.remove item \n3.calculate total" 
              ,"\n4.Bill \n5.exit \n6.displaycart")
        choise=int(input("Enter choise: "))
        if choise==1:
            name=input("Enter product name:")
            quantity=int(input("Enter quantity: "))
            prize=float(input("Enter prize: "))
            cart.add_item(name,quantity,prize)
        elif choise==2:
            cart.display_elements()
            item=input("Enter the element to be removed: ")
            cart.remove_element(item)
        elif choise==3:
            total=cart.calculate_total()
            print(total)
        elif choise==4:
            cart.bill()
            total=cart.calculate_total()
            payment.pay(total)
        elif choise==6:
            cart.display_elements()    
if __name__=="__main__":
    main()