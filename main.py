import pyautogui
import time

global n_aux 
n_aux = 0
print(n_aux)


def go_to_gym():
    
    global n_aux 
    num_veces = 5

# Loop para segurar a tecla "I" sete vezes
    for _ in range(num_veces):
        pyautogui.keyDown('i')  # Pressiona a tecla "I"
        time.sleep(0.5)  # Espera meio segundo (ajuste conforme necessário)
        pyautogui.keyUp('i')  # Libera a tecla "I"
        time.sleep(0.5)
        print("chegou")
    
    for _ in range (num_veces +3):
        pyautogui.keyDown('z')  # Pressiona a tecla "I"
        time.sleep(0.5)  # Espera meio segundo (ajuste conforme necessário)
        pyautogui.keyUp('z')  # Libera a tecla "I"
        time.sleep(0.5)
        print("curou")
    for _ in range(num_veces):
        pyautogui.keyDown('k')
        time.sleep(0.5)
        pyautogui.keyUp('k')
        time.sleep(0.5)
        print("voltou")
    n_aux = 0    
    print(n_aux)
    fish()
    

def landed():
    global n_aux 
    while True:
        try:
            elemento = pyautogui.locateOnScreen('battle.png', confidence=0.8)
            if elemento is not None:
                
                
                print(n_aux)

                print("cena de luta encontrada!")
                pyautogui.press('z')
                time.sleep(1)
                pyautogui.press('z')
                print("indo ao pos_battle")
                time.sleep(5)
                pos_battle()
                
                                 
            else:
                print("cena de luta n encontrado.")
                print("indo ao pos_battle")
                pos_battle()
                pyautogui.press('z')
        except Exception as e:
            print("cena de luta n encontrada. exce", e)
            print("indo ao pos_battle")
            time.sleep(5)
            pos_battle()
            
        

def pos_battle():
    time.sleep(5)
    try:
        elemento2 = pyautogui.locateOnScreen('water.png', confidence=0.8)
        if elemento2 is not None:
            fish()
        else:
            return True
    except Exception as e:
        print('nao terminou a batalha')
        time.sleep(5)
        landed()


def fish():
    global n_aux 
    n_aux += 1
    if n_aux <= 5 :
        while True:
            pyautogui.press('1')
            time.sleep(1)
            pyautogui.press('z')

            try:
                elemento = pyautogui.locateOnScreen('landed.png', confidence=0.8)
                if elemento is not None:
                    print("Pokemon foi pego!")
                    pyautogui.press('z')
                    time.sleep(1)
                    print(n_aux)
                    landed()
               
                else:
                    print("Pokemon nao foi encontrado.")
                    pyautogui.press('z')
            except Exception as e:
                print("Pokemon nao foi encontrado. ex", e)
            
        
    else:
        print(n_aux)
        time.sleep(0.5)
        go_to_gym()

        



def main():
    global n_aux 
    n = 0
    time.sleep(2)
    n += 1 
    print("teste ",n )
    fish()



if __name__ == "__main__":
    main()