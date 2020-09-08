function LED_loop () {
    while (remaining_button_presses == 0) {
        for (let index = 0; index <= 9; index++) {
            light.setPixelColor(index, 0xff0000)
            pause(randint(25, 150))
            if (input.buttonA.isPressed()) {
                if (index == 2) {
                    console.log("\"Button A correct push!\"")
                    music.powerUp.play()
                    light.showAnimation(light.rainbowAnimation, 1000)
                    light.setAll(0xffffff)
                    correct_button_presses += 1
                } else {
                    console.log("\"Button A incorrect push!\"")
                    music.powerDown.play()
                    light.setAll(0xffffff)
                    pause(1000)
                }
                remaining_button_presses += -1
                break;
            }
            light.setPixelColor(index, 0xffffff)
        }
        continue_game = false
    }
}
function show_result (correct_presses: number) {
    console.logValue("Your Score", correct_presses)
    for (let index_2 = 0; index_2 <= 9; index_2++) {
        if (0 > 0) {
            light.setPixelColor(index_2, 0x00ff00)
            correct_presses += -1
        }
    }
    pause(5000)
    light.setAll(0xffffff)
}
let correct_presses = 0
let continue_game = false
let remaining_button_presses = 0
remaining_button_presses = 10
let correct_button_presses = 0
continue_game = true
forever(function () {
    if (continue_game == true) {
        LED_loop()
    } else {
        show_result(correct_button_presses)
        correct_button_presses = 0
        remaining_button_presses = 10
        continue_game = true
    }
})
