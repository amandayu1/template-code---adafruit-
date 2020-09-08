def LED_loop_a():
    global correct_button_presses_a, remaining_button_presses_a, a_turn
    for index in range(10):
        light.set_pixel_color(index, 0xff0000)
        pause(randint(25, 150))
        if input.button_a.is_pressed():
            if index == 5:
                print("Button A correct push!")
                music.power_up.play()
                light.show_animation(light.rainbow_animation, 1000)
                light.set_all(0xffffff)
                correct_button_presses_a += 1
            else:
                print("Button A incorrect push!")
                music.power_down.play()
                light.set_all(0xffffff)
                pause(1000)
            remaining_button_presses_a += -1
            a_turn = False
            break
        light.set_pixel_color(index, 0xffffff)
    if correct_button_presses_a == 0:
        show_result("A", correct_button_presses_a)
        correct_button_presses_a = 0
def show_result(correctbutton_press: str, button: number):
    console.log_value(button, correctbutton_press)
    for index_2 in range(10):
        if button > 0:
            light.set_pixel_color(index_2, 0x00ff00)
            index_2 += 1
    pause(3000)
    light.set_all(0xffffff)
def LED_loop_b():
    global correct_button_presses_b, a_turn
    for index_3 in range(10):
        light.set_pixel_color(index_3, 0xff0000)
        pause(randint(25, 150))
        if input.button_b.is_pressed():
            if index_3 == 5:
                print("Button B correct push!")
                music.power_up.play()
                light.show_animation(light.rainbow_animation, 1000)
                light.set_all(0xffffff)
                correct_button_presses_b += 1
            else:
                print("Button B incorrect push!")
                music.power_down.play()
                light.set_all(0xffffff)
                pause(1000)
            correct_button_presses_b += -1
            a_turn = True
            break
        light.set_pixel_color(index_3, 0xffffff)
    if correct_button_presses_b == 0:
        show_result("A", correct_button_presses_b)
        correct_button_presses_b = 0
correct_button_presses_b = 0
a_turn = False
correct_button_presses_a = 0
remaining_button_presses_a = 10
remaining_button_presses_b = 10
correct_button_presses_a = 0
a_turn = True

def on_forever():
    global correct_button_presses_a, remaining_button_presses_b
    if a_turn == True and correct_button_presses_a > 0:
        LED_loop_a()
    elif a_turn == False and remaining_button_presses_b > 0:
        LED_loop_b()
    else:
        correct_button_presses_a = 10
        remaining_button_presses_b = 10
forever(on_forever)

